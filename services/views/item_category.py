from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny

from services.models import ItemCategory
from services.serializers.item_category import ItemCategorySerializer


class ItemCategoryListCreateAPIView(ListCreateAPIView):
    serializer_class = ItemCategorySerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):

        return ItemCategory.objects.all()


class ItemCategoryRetrieveUpdateDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ItemCategorySerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):

        return ItemCategory.objects.all()

    def get_object(self):

        return self.get_queryset().get(id=self.kwargs.get("id"))
