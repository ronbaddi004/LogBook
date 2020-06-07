from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny

from services.models import BaseCountry, BaseState, BaseCity
from services.serializers.base_geolocations import BaseCountrySerializer, BaseStateSerializer, BaseCitySerializer


class BaseCountryListCreateAPIView(ListCreateAPIView):
    serializer_class = BaseCountrySerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):

        return BaseCountry.objects.all()


class BaseCountryRetrieveUpdateDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = BaseCountrySerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):

        return BaseCountry.objects.all()

    def get_object(self):

        return self.get_queryset().get(id=self.kwargs.get("id"))


class BaseStateListCreateAPIView(ListCreateAPIView):
    serializer_class = BaseStateSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):

        return BaseState.objects.all()


class BaseStateRetrieveUpdateDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = BaseStateSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):

        return BaseState.objects.all()

    def get_object(self):

        return self.get_queryset().get(id=self.kwargs.get("id"))


class BaseCityListCreateAPIView(ListCreateAPIView):
    serializer_class = BaseCitySerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):

        return BaseCity.objects.all()


class BaseCityRetrieveUpdateDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = BaseCitySerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):

        return BaseCity.objects.all()

    def get_object(self):

        return self.get_queryset().get(id=self.kwargs.get("id"))
