from django.views.generic import ListView

from apps.models import Product


class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'product/dashboard.html'
