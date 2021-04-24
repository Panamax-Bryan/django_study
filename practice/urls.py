from django.urls import path
from .views import Assign1View, Assign2View

urlpatterns = [
    path('/assign1', Assign1View.as_view()),
    path('/assign2', Assign2View.as_view()),
]
