from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny

from services.models import Tax
from services.serializers.tax import TaxSerializer


class TaxListCreateAPIView(ListCreateAPIView):
    serializer_class = TaxSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):

        return Tax.objects.all()


class TaxRetrieveUpdateDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = TaxSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):

        return Tax.objects.all()

    def get_object(self):

        return self.get_queryset().get(id=self.kwargs.get("id"))
