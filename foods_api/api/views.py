from rest_framework import generics

from api.models import FoodCategory, FoodListSerializer


class FoodCategoriesAPIView(generics.ListAPIView):
    queryset = FoodCategory.objects.all()
    serializer_class = FoodListSerializer
