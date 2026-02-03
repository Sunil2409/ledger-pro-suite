from django import forms
from .models import Watchlist


class WatchlistForm(forms.ModelForm):
    """Form for creating and updating watchlist items"""
    
    class Meta:
        model = Watchlist
        fields = ['symbol', 'name', 'asset_type', 'status', 'target_price', 
                  'current_price', 'quantity', 'purchase_price', 'notes']
        widgets = {
            'symbol': forms.TextInput(attrs={
                'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 bg-gray-50 uppercase',
                'placeholder': 'e.g., AAPL, MSFT, BTC',
                'maxlength': '10'
            }),
            'name': forms.TextInput(attrs={
                'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 bg-gray-50',
                'placeholder': 'e.g., Apple Inc.'
            }),
            'asset_type': forms.Select(attrs={
                'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 bg-gray-50'
            }),
            'status': forms.Select(attrs={
                'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 bg-gray-50'
            }),
            'target_price': forms.NumberInput(attrs={
                'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 bg-gray-50',
                'placeholder': '0.00',
                'step': '0.01'
            }),
            'current_price': forms.NumberInput(attrs={
                'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 bg-gray-50',
                'placeholder': '0.00',
                'step': '0.01'
            }),
            'quantity': forms.NumberInput(attrs={
                'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 bg-gray-50',
                'placeholder': '0.0000',
                'step': '0.0001'
            }),
            'purchase_price': forms.NumberInput(attrs={
                'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 bg-gray-50',
                'placeholder': '0.00',
                'step': '0.01'
            }),
            'notes': forms.Textarea(attrs={
                'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 bg-gray-50',
                'rows': 4,
                'placeholder': 'Investment thesis, research notes, or analysis...'
            }),
        }
    
    def clean_symbol(self):
        """Convert symbol to uppercase"""
        symbol = self.cleaned_data.get('symbol')
        if symbol:
            return symbol.upper()
        return symbol
    
    def clean(self):
        """Validate price and quantity combinations"""
        cleaned_data = super().clean()
        quantity = cleaned_data.get('quantity')
        purchase_price = cleaned_data.get('purchase_price')
        
        if quantity and quantity > 0 and not purchase_price:
            self.add_error('purchase_price', 
                          'Purchase price is required when quantity is specified.')
        
        return cleaned_data
