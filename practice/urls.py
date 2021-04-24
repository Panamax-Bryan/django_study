from django.urls import path
from .views import Assign1View

urlpatterns = [
    path('/assign1', Assign1View.as_view()),
]
