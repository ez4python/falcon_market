from django.urls import path

from apps.views.product import ProductListView

urlpatterns = (
    path('', ProductListView.as_view(), name='products_dashboard_page'),
)
