from django.db import models
from django.contrib.auth.models import User


class Watchlist(models.Model):
    """Model for tracking investment watchlist items"""
    
    STATUS_CHOICES = [
        ('BUY', 'Buy'),
        ('HOLD', 'Hold'),
        ('SELL', 'Sell'),
    ]
    
    ASSET_TYPE_CHOICES = [
        ('STOCK', 'Stock'),
        ('ETF', 'ETF'),
        ('CRYPTO', 'Cryptocurrency'),
        ('MUTUAL_FUND', 'Mutual Fund'),
        ('BOND', 'Bond'),
        ('OTHER', 'Other'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='watchlist_items')
    symbol = models.CharField(max_length=10, help_text="Stock symbol (e.g., AAPL, MSFT)")
    name = models.CharField(max_length=200, blank=True, help_text="Company/Asset name")
    asset_type = models.CharField(max_length=20, choices=ASSET_TYPE_CHOICES, default='STOCK')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='HOLD')
    target_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    current_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    quantity = models.DecimalField(max_digits=10, decimal_places=4, default=0, help_text="Quantity owned")
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    notes = models.TextField(blank=True, help_text="Investment thesis or notes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Watchlist Item"
        verbose_name_plural = "Watchlist Items"
        unique_together = ['user', 'symbol']
        indexes = [
            models.Index(fields=['user', 'status']),
        ]
    
    def __str__(self):
        return f"{self.symbol} - {self.get_status_display()}"
    
    @property
    def gain_loss(self):
        """Calculate gain/loss if quantity and prices are available"""
        if self.quantity and self.purchase_price and self.current_price:
            return (self.current_price - self.purchase_price) * self.quantity
        return None
    
    @property
    def gain_loss_percentage(self):
        """Calculate gain/loss percentage"""
        if self.purchase_price and self.current_price and self.purchase_price > 0:
            return ((self.current_price - self.purchase_price) / self.purchase_price) * 100
        return None
    
    @property
    def total_value(self):
        """Calculate total current value"""
        if self.quantity and self.current_price:
            return self.quantity * self.current_price
        return None
    
    @property
    def total_cost(self):
        """Calculate total purchase cost"""
        if self.quantity and self.purchase_price:
            return self.quantity * self.purchase_price
        return None
