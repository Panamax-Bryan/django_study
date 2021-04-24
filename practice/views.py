import json

from django.views    import View
from django.http     import JsonResponse
from .models import MainCategory, SubCategory

class Assign1View(View):
    def get(self, request):
        subcategories = SubCategory.objects.all()

        sub_list = []

        for sub in subcategories:
            sub_list.append({
                'name'   : sub.name,
                'main_category_id' : sub.main_category_id
                    })
        return JsonResponse({'RESULT' : sub_list}, status=200)


#class assignment_2(View):
#    def get(self, request):
#        a = MainCategory.objects.get(name='눈 건강')
#        
#        sub_list = []
#        for i in SubCategory.objects.filter(main_category=a):
#            sub_list.append({
#                'name' : i.name,
#                'main_category_id' : i.main_category_id
#                })
#        return JsonResponse({'RESULT' : sub_list}, status=200)
