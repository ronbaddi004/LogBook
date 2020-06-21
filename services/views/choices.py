from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status

from services.models import TaxTypeChoices, BasisChoices, PartyTypeChoices, NatureChoices, GSTRegistrationTypeChoices


class ChoicesAPIView(RetrieveAPIView):

    def get(self, request, *args, **kwargs):
        """Return Choices"""
        choices = {}

        choices["TaxTypeChoices"] = dict(TaxTypeChoices.choices)
        choices["BasisChoices"] = dict(BasisChoices.choices)
        choices["PartyTypeChoices"] = dict(PartyTypeChoices.choices)
        choices["NatureChoices"] = dict(NatureChoices.choices)
        choices["GSTRegistrationTypeChoices"] = dict(GSTRegistrationTypeChoices.choices)

        return Response(data=choices, status=status.HTTP_200_OK)
