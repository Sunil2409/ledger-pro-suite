from django.urls import path
from .views import (
    WatchlistListView,
    WatchlistCreateView,
    WatchlistUpdateView,
    WatchlistDeleteView,
    WatchlistDetailView,
)

urlpatterns = [
    path('', WatchlistListView.as_view(), name='watchlist_list'),
    path('add/', WatchlistCreateView.as_view(), name='watchlist_create'),
    path('<int:pk>/', WatchlistDetailView.as_view(), name='watchlist_detail'),
    path('<int:pk>/edit/', WatchlistUpdateView.as_view(), name='watchlist_update'),
    path('<int:pk>/delete/', WatchlistDeleteView.as_view(), name='watchlist_delete'),
]
