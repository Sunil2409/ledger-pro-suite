from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Sum, Q
from decimal import Decimal
from .models import Watchlist
from .forms import WatchlistForm


class WatchlistListView(LoginRequiredMixin, ListView):
    """List all watchlist items for the logged-in user"""
    model = Watchlist
    template_name = 'watchlist/watchlist_list.html'
    context_object_name = 'watchlist_items'
    paginate_by = 20
    
    def get_queryset(self):
        queryset = Watchlist.objects.filter(user=self.request.user)
        
        # Filter by status
        status = self.request.GET.get('status')
        if status in ['BUY', 'HOLD', 'SELL']:
            queryset = queryset.filter(status=status)
        
        # Filter by asset type
        asset_type = self.request.GET.get('asset_type')
        if asset_type:
            queryset = queryset.filter(asset_type=asset_type)
        
        # Search
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(
                Q(symbol__icontains=search) | 
                Q(name__icontains=search) |
                Q(notes__icontains=search)
            )
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Calculate portfolio statistics
        all_items = Watchlist.objects.filter(
            user=self.request.user,
            quantity__gt=0
        )
        
        total_value = sum([item.total_value for item in all_items if item.total_value])
        total_cost = sum([item.total_cost for item in all_items if item.total_cost])
        total_gain_loss = total_value - total_cost if total_value and total_cost else 0
        
        context.update({
            'statuses': Watchlist.STATUS_CHOICES,
            'asset_types': Watchlist.ASSET_TYPE_CHOICES,
            'current_status': self.request.GET.get('status', ''),
            'current_asset_type': self.request.GET.get('asset_type', ''),
            'current_search': self.request.GET.get('search', ''),
            'total_portfolio_value': total_value,
            'total_portfolio_cost': total_cost,
            'total_gain_loss': total_gain_loss,
        })
        
        return context


class WatchlistCreateView(LoginRequiredMixin, CreateView):
    """Create a new watchlist item"""
    model = Watchlist
    form_class = WatchlistForm
    template_name = 'watchlist/watchlist_form.html'
    success_url = reverse_lazy('watchlist_list')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, f'Added {form.instance.symbol} to your watchlist!')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add to Watchlist'
        context['button_text'] = 'Add to Watchlist'
        return context


class WatchlistUpdateView(LoginRequiredMixin, UpdateView):
    """Update an existing watchlist item"""
    model = Watchlist
    form_class = WatchlistForm
    template_name = 'watchlist/watchlist_form.html'
    success_url = reverse_lazy('watchlist_list')
    
    def get_queryset(self):
        return Watchlist.objects.filter(user=self.request.user)
    
    def form_valid(self, form):
        messages.success(self.request, f'Updated {form.instance.symbol} successfully!')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Edit {self.object.symbol}'
        context['button_text'] = 'Update Watchlist Item'
        return context


class WatchlistDeleteView(LoginRequiredMixin, DeleteView):
    """Delete a watchlist item"""
    model = Watchlist
    template_name = 'watchlist/watchlist_confirm_delete.html'
    success_url = reverse_lazy('watchlist_list')
    
    def get_queryset(self):
        return Watchlist.objects.filter(user=self.request.user)
    
    def delete(self, request, *args, **kwargs):
        symbol = self.get_object().symbol
        messages.success(request, f'Removed {symbol} from your watchlist!')
        return super().delete(request, *args, **kwargs)


class WatchlistDetailView(LoginRequiredMixin, DetailView):
    """View details of a watchlist item"""
    model = Watchlist
    template_name = 'watchlist/watchlist_detail.html'
    context_object_name = 'item'
    
    def get_queryset(self):
        return Watchlist.objects.filter(user=self.request.user)
