from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny

from services.models import Unit
from services.serializers.unit import UnitSerializer


class UnitListCreateAPIView(ListCreateAPIView):
    serializer_class = UnitSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):

        return Unit.objects.all()


class UnitRetrieveUpdateDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = UnitSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):

        return Unit.objects.all()

    def get_object(self):

        return self.get_queryset().get(id=self.kwargs.get("id"))
