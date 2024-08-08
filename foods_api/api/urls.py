from django.urls import path

from api.views import FoodCategoriesAPIView


urlpatterns = [
    path('v1/foods/', FoodCategoriesAPIView.as_view(), name='food_categories'),
]
