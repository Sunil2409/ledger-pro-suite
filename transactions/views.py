from django.views.generic import ListView, CreateView, DeleteView, UpdateView, TemplateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Sum, Q
from django.contrib import messages
from django.shortcuts import redirect
from datetime import datetime, timedelta
from decimal import Decimal
from .models import Transaction, UserProfile
from .forms import TransactionForm, SignUpForm, BudgetUpdateForm


class DashboardView(LoginRequiredMixin, TemplateView):
    """Dashboard with financial overview and summary"""
    template_name = 'transactions/dashboard.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        
        # Get or create user profile
        profile, _ = UserProfile.objects.get_or_create(user=user)
        
        # Get current month transactions
        today = datetime.now()
        first_day = today.replace(day=1)
        
        current_month_transactions = Transaction.objects.filter(
            user=user,
            date__gte=first_day
        )
        
        # Calculate current month expenses and income
        monthly_expenses = current_month_transactions.filter(
            transaction_type='EXPENSE'
        ).aggregate(total=Sum('amount'))['total'] or Decimal('0.00')
        
        monthly_income = current_month_transactions.filter(
            transaction_type='INCOME'
        ).aggregate(total=Sum('amount'))['total'] or Decimal('0.00')
        
        # Calculate all-time totals
        all_transactions = Transaction.objects.filter(user=user)
        
        total_expenses = all_transactions.filter(
            transaction_type='EXPENSE'
        ).aggregate(total=Sum('amount'))['total'] or Decimal('0.00')
        
        total_income = all_transactions.filter(
            transaction_type='INCOME'
        ).aggregate(total=Sum('amount'))['total'] or Decimal('0.00')
        
        # Calculate budget progress
        budget_remaining = profile.monthly_budget - monthly_expenses
        budget_percentage = (monthly_expenses / profile.monthly_budget * 100) if profile.monthly_budget > 0 else 0
        
        # Get recent transactions
        recent_transactions = Transaction.objects.filter(user=user)[:5]
        
        # Calculate expense by category
        expense_by_category = current_month_transactions.filter(
            transaction_type='EXPENSE'
        ).values('category').annotate(
            total=Sum('amount')
        ).order_by('-total')[:5]
        
        context.update({
            'profile': profile,
            'total_balance': profile.total_balance,
            'monthly_budget': profile.monthly_budget,
            'monthly_expenses': monthly_expenses,
            'monthly_income': monthly_income,
            'budget_remaining': budget_remaining,
            'budget_percentage': budget_percentage,
            'total_expenses': total_expenses,
            'total_income': total_income,
            'recent_transactions': recent_transactions,
            'expense_by_category': expense_by_category,
            'current_month': today.strftime('%B %Y'),
        })
        
        return context


class TransactionListView(LoginRequiredMixin, ListView):
    """List all transactions for the logged-in user"""
    model = Transaction
    template_name = 'transactions/transaction_list.html'
    context_object_name = 'transactions'
    paginate_by = 20
    
    def get_queryset(self):
        queryset = Transaction.objects.filter(user=self.request.user)
        
        # Filter by type
        transaction_type = self.request.GET.get('type')
        if transaction_type in ['EXPENSE', 'INCOME']:
            queryset = queryset.filter(transaction_type=transaction_type)
        
        # Filter by category
        category = self.request.GET.get('category')
        if category:
            queryset = queryset.filter(category=category)
        
        # Search
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(
                Q(description__icontains=search) | 
                Q(category__icontains=search)
            )
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['transaction_types'] = Transaction.TRANSACTION_TYPES
        context['categories'] = Transaction.CATEGORY_CHOICES
        context['current_type'] = self.request.GET.get('type', '')
        context['current_category'] = self.request.GET.get('category', '')
        context['current_search'] = self.request.GET.get('search', '')
        return context


class TransactionCreateView(LoginRequiredMixin, CreateView):
    """Create a new transaction"""
    model = Transaction
    form_class = TransactionForm
    template_name = 'transactions/transaction_form.html'
    success_url = reverse_lazy('transaction_list')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Transaction added successfully!')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add New Transaction'
        context['button_text'] = 'Add Transaction'
        return context


class TransactionUpdateView(LoginRequiredMixin, UpdateView):
    """Update an existing transaction"""
    model = Transaction
    form_class = TransactionForm
    template_name = 'transactions/transaction_form.html'
    success_url = reverse_lazy('transaction_list')
    
    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)
    
    def form_valid(self, form):
        messages.success(self.request, 'Transaction updated successfully!')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit Transaction'
        context['button_text'] = 'Update Transaction'
        return context


class TransactionDeleteView(LoginRequiredMixin, DeleteView):
    """Delete a transaction"""
    model = Transaction
    template_name = 'transactions/transaction_confirm_delete.html'
    success_url = reverse_lazy('transaction_list')
    
    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Transaction deleted successfully!')
        return super().delete(request, *args, **kwargs)


class BudgetUpdateView(LoginRequiredMixin, FormView):
    """Update monthly budget"""
    form_class = BudgetUpdateForm
    template_name = 'transactions/budget_update.html'
    success_url = reverse_lazy('dashboard')
    
    def get_initial(self):
        profile, _ = UserProfile.objects.get_or_create(user=self.request.user)
        return {'monthly_budget': profile.monthly_budget}
    
    def form_valid(self, form):
        profile, _ = UserProfile.objects.get_or_create(user=self.request.user)
        profile.monthly_budget = form.cleaned_data['monthly_budget']
        profile.save()
        messages.success(self.request, 'Budget updated successfully!')
        return super().form_valid(form)


class SignUpView(CreateView):
    """User registration view"""
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        messages.success(self.request, 'Account created successfully! Please log in.')
        return super().form_valid(form)
