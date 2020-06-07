from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny

from services.models import Item
from services.serializers.item import ItemSerializer


class ItemListCreateAPIView(ListCreateAPIView):
    serializer_class = ItemSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):

        return Item.objects.all()


class ItemRetrieveUpdateDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ItemSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):

        return Item.objects.all()

    def get_object(self):

        return self.get_queryset().get(id=self.kwargs.get("id"))
