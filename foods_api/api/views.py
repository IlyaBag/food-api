from django.db.models import Prefetch
from rest_framework import generics

from api.models import Food, FoodCategory, FoodListSerializer


class FoodCategoriesAPIView(generics.ListAPIView):
    prefetch = Prefetch('food', queryset=Food.objects.filter(is_publish=True))
    queryset = FoodCategory.objects.prefetch_related(prefetch). \
        filter(food__is_publish=True).distinct()
    serializer_class = FoodListSerializer
