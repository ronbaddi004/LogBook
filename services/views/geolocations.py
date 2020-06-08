from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny

from services.models import Country, State, City
from services.serializers.geolocations import CountrySerializer, StateSerializer, CitySerializer


class CountryListCreateAPIView(ListCreateAPIView):
    serializer_class = CountrySerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):

        return Country.objects.all()


class CountryRetrieveUpdateDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CountrySerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):

        return Country.objects.all()

    def get_object(self):

        return self.get_queryset().get(id=self.kwargs.get("id"))


class StateListCreateAPIView(ListCreateAPIView):
    serializer_class = StateSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):

        return State.objects.all()


class StateRetrieveUpdateDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = StateSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):

        return State.objects.all()

    def get_object(self):

        return self.get_queryset().get(id=self.kwargs.get("id"))


class CityListCreateAPIView(ListCreateAPIView):
    serializer_class = CitySerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):

        return City.objects.all()


class CityRetrieveUpdateDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CitySerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):

        return City.objects.all()

    def get_object(self):

        return self.get_queryset().get(id=self.kwargs.get("id"))
