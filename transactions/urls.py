from django.urls import path
from .views import (
    TransactionListView,
    TransactionCreateView,
    TransactionUpdateView,
    TransactionDeleteView,
    BudgetUpdateView,
    SignUpView,
)

urlpatterns = [
    path('', TransactionListView.as_view(), name='transaction_list'),
    path('add/', TransactionCreateView.as_view(), name='transaction_create'),
    path('<int:pk>/edit/', TransactionUpdateView.as_view(), name='transaction_update'),
    path('<int:pk>/delete/', TransactionDeleteView.as_view(), name='transaction_delete'),
    path('budget/', BudgetUpdateView.as_view(), name='budget_update'),
    path('signup/', SignUpView.as_view(), name='signup'),
]
