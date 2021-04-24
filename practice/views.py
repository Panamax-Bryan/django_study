import json

from django.views    import View
from django.http     import JsonResponse
from .models import MainCategory, Product, SubCategory

class GetView(View):
    def get(self, request):
        products = Product.objects.all()

        product_list = []

        for product in products:
            product_list.append({
                'name'   : product.name,
                'price'  : product.price,
                'detail' : product.detail
                    })
        return JsonResponse({'RESULT' : product_list}, status=200)


class FilterView(View):
    def get(self, request):
        a = MainCategory.objects.get(name='눈 건강')
        
        sub_list = []
        for i in SubCategory.objects.filter(main_category=a):
            sub_list.append({
                'name' : i.name,
                'main_category_id' : i.main_category_id
                })
        return JsonResponse({'RESULT' : sub_list}, status=200)
