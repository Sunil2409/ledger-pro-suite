from django.contrib import admin
from .models import Transaction, UserProfile


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'transaction_type', 'category', 'amount', 'date', 'created_at')
    list_filter = ('transaction_type', 'category', 'date', 'user')
    search_fields = ('description', 'user__username')
    date_hierarchy = 'date'
    ordering = ('-date', '-created_at')
    
    fieldsets = (
        ('Transaction Details', {
            'fields': ('user', 'transaction_type', 'category', 'amount', 'date')
        }),
        ('Additional Information', {
            'fields': ('description',)
        }),
    )


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_balance', 'monthly_budget', 'updated_at')
    search_fields = ('user__username', 'user__email')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('User', {
            'fields': ('user',)
        }),
        ('Financial Information', {
            'fields': ('total_balance', 'monthly_budget')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
