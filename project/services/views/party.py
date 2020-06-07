from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny

from services.models import Party
from services.serializers.party import PartySerializer


class PartyListCreateAPIView(ListCreateAPIView):
    serializer_class = PartySerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):

        return Party.objects.all()


class PartyRetrieveUpdateDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = PartySerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):

        return Party.objects.all()

    def get_object(self):

        return self.get_queryset().get(id=self.kwargs.get("id"))
