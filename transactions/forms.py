from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Transaction


class TransactionForm(forms.ModelForm):
    """Form for creating and updating transactions with validation"""
    
    class Meta:
        model = Transaction
        fields = ['transaction_type', 'category', 'amount', 'description', 'date']
        widgets = {
            'transaction_type': forms.Select(attrs={
                'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 bg-gray-50'
            }),
            'category': forms.Select(attrs={
                'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 bg-gray-50'
            }),
            'amount': forms.NumberInput(attrs={
                'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 bg-gray-50',
                'placeholder': '0.00',
                'step': '0.01',
                'min': '0.01'
            }),
            'description': forms.Textarea(attrs={
                'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 bg-gray-50',
                'rows': 3,
                'placeholder': 'Add details about this transaction...'
            }),
            'date': forms.DateInput(attrs={
                'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 bg-gray-50',
                'type': 'date'
            }),
        }
    
    def clean_amount(self):
        """Validate that amount is positive"""
        amount = self.cleaned_data.get('amount')
        if amount and amount <= 0:
            raise forms.ValidationError("Amount must be greater than zero.")
        return amount


class SignUpForm(UserCreationForm):
    """Custom signup form with additional fields"""
    email = forms.EmailField(
        max_length=254,
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 bg-gray-50',
            'placeholder': 'email@example.com'
        })
    )
    first_name = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 bg-gray-50',
            'placeholder': 'First Name'
        })
    )
    last_name = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 bg-gray-50',
            'placeholder': 'Last Name'
        })
    )
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 bg-gray-50',
                'placeholder': 'Username'
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({
            'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 bg-gray-50'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 bg-gray-50'
        })


class BudgetUpdateForm(forms.Form):
    """Form for updating monthly budget"""
    monthly_budget = forms.DecimalField(
        max_digits=12,
        decimal_places=2,
        min_value=0,
        widget=forms.NumberInput(attrs={
            'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 bg-gray-50',
            'placeholder': '5000.00',
            'step': '0.01'
        })
    )
