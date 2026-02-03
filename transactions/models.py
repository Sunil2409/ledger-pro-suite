from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from decimal import Decimal


class UserProfile(models.Model):
    """Extended user profile to track financial summary"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    total_balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    monthly_budget = models.DecimalField(max_digits=12, decimal_places=2, default=5000.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.username}'s Profile"
    
    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"


class Transaction(models.Model):
    """Transaction model for tracking expenses and income"""
    TRANSACTION_TYPES = [
        ('EXPENSE', 'Expense'),
        ('INCOME', 'Income'),
    ]
    
    CATEGORY_CHOICES = [
        ('FOOD', 'Food & Dining'),
        ('TRANSPORT', 'Transportation'),
        ('SHOPPING', 'Shopping'),
        ('ENTERTAINMENT', 'Entertainment'),
        ('BILLS', 'Bills & Utilities'),
        ('HEALTH', 'Healthcare'),
        ('EDUCATION', 'Education'),
        ('INVESTMENT', 'Investment'),
        ('SALARY', 'Salary'),
        ('OTHER', 'Other'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES, default='EXPENSE')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='OTHER')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-date', '-created_at']
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"
        indexes = [
            models.Index(fields=['-date', 'user']),
        ]
    
    def __str__(self):
        return f"{self.get_transaction_type_display()} - {self.amount} - {self.date}"
    
    def save(self, *args, **kwargs):
        """Override save to ensure amount is positive"""
        self.amount = abs(self.amount)
        super().save(*args, **kwargs)


# Django Signals to update user balance
@receiver(post_save, sender=Transaction)
def update_balance_on_transaction_save(sender, instance, created, **kwargs):
    """Update user's total balance when a transaction is created or updated"""
    profile, _ = UserProfile.objects.get_or_create(user=instance.user)
    
    # Recalculate total balance from all transactions
    transactions = Transaction.objects.filter(user=instance.user)
    
    income = transactions.filter(transaction_type='INCOME').aggregate(
        total=models.Sum('amount')
    )['total'] or Decimal('0.00')
    
    expenses = transactions.filter(transaction_type='EXPENSE').aggregate(
        total=models.Sum('amount')
    )['total'] or Decimal('0.00')
    
    profile.total_balance = income - expenses
    profile.save()


@receiver(post_delete, sender=Transaction)
def update_balance_on_transaction_delete(sender, instance, **kwargs):
    """Update user's total balance when a transaction is deleted"""
    try:
        profile = UserProfile.objects.get(user=instance.user)
        
        # Recalculate total balance from remaining transactions
        transactions = Transaction.objects.filter(user=instance.user)
        
        income = transactions.filter(transaction_type='INCOME').aggregate(
            total=models.Sum('amount')
        )['total'] or Decimal('0.00')
        
        expenses = transactions.filter(transaction_type='EXPENSE').aggregate(
            total=models.Sum('amount')
        )['total'] or Decimal('0.00')
        
        profile.total_balance = income - expenses
        profile.save()
    except UserProfile.DoesNotExist:
        pass


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Automatically create a UserProfile when a new User is created"""
    if created:
        UserProfile.objects.create(user=instance)
