from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny

from services.models import Company
from services.serializers.company import CompanySerializer


class CompanyListCreateAPIView(ListCreateAPIView):
    serializer_class = CompanySerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):

        return Company.objects.all()


class CompanyRetrieveUpdateDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CompanySerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):

        return Company.objects.all()

    def get_object(self):

        return self.get_queryset().get(id=self.kwargs.get("id"))
