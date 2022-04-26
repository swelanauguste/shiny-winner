from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView

from .models import Category, Product


def product_list(request, category_slug=None):
    category = None
    category_list = Category.objects.all()
    product_list = Product.objects.filter(is_available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        product_list = product_list.filter(category=category)
    return render(
        request,
        "shop/product_list.html",
        {
            "category": category,
            "category_list": category_list,
            "product_list": product_list,
        },
    )


class ProductDetailView(DetailView):
    model = Product
    # template_name = "shop/product_detail.html"

    # def get_context_data(self, **kwargs):
    #     context = super(ProductDetailView, self).get_context_data(**kwargs)
    #     context["related_products"] = Product.objects.filter(category=self.object.category).exclude(pk=self.object.pk)
    #     return context
