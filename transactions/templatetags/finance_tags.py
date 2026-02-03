from django import template
from django.db.models import Sum
from decimal import Decimal
from datetime import datetime

register = template.Library()


@register.simple_tag
def calculate_total_spend(user, month=None, year=None):
    """Calculate total spending for a user, optionally filtered by month/year"""
    from transactions.models import Transaction
    
    queryset = Transaction.objects.filter(
        user=user,
        transaction_type='EXPENSE'
    )
    
    if month and year:
        queryset = queryset.filter(date__month=month, date__year=year)
    
    total = queryset.aggregate(total=Sum('amount'))['total']
    return total or Decimal('0.00')


@register.simple_tag
def calculate_total_income(user, month=None, year=None):
    """Calculate total income for a user, optionally filtered by month/year"""
    from transactions.models import Transaction
    
    queryset = Transaction.objects.filter(
        user=user,
        transaction_type='INCOME'
    )
    
    if month and year:
        queryset = queryset.filter(date__month=month, date__year=year)
    
    total = queryset.aggregate(total=Sum('amount'))['total']
    return total or Decimal('0.00')


@register.simple_tag
def budget_status(spent, budget):
    """Return budget status based on spending"""
    if budget == 0:
        return 'no-budget'
    
    percentage = (spent / budget) * 100
    
    if percentage < 70:
        return 'safe'
    elif percentage < 90:
        return 'warning'
    else:
        return 'danger'


@register.filter
def percentage(value, total):
    """Calculate percentage of value relative to total"""
    if total == 0:
        return 0
    try:
        return round((float(value) / float(total)) * 100, 1)
    except (ValueError, TypeError, ZeroDivisionError):
        return 0


@register.filter
def abs_value(value):
    """Return absolute value"""
    try:
        return abs(float(value))
    except (ValueError, TypeError):
        return 0


@register.filter
def format_currency(value):
    """Format number as currency"""
    try:
        return f"${float(value):,.2f}"
    except (ValueError, TypeError):
        return "$0.00"
