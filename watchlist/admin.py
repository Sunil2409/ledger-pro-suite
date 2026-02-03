from django.contrib import admin
from .models import Watchlist


@admin.register(Watchlist)
class WatchlistAdmin(admin.ModelAdmin):
    list_display = ('symbol', 'name', 'user', 'asset_type', 'status', 
                    'current_price', 'target_price', 'quantity', 'updated_at')
    list_filter = ('status', 'asset_type', 'user')
    search_fields = ('symbol', 'name', 'user__username', 'notes')
    ordering = ('-updated_at',)
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('user', 'symbol', 'name', 'asset_type')
        }),
        ('Trading Information', {
            'fields': ('status', 'current_price', 'target_price')
        }),
        ('Position Details', {
            'fields': ('quantity', 'purchase_price'),
            'description': 'Enter quantity and purchase price if you own this asset'
        }),
        ('Notes', {
            'fields': ('notes',),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ('created_at', 'updated_at')
