from django.contrib import admin
from django.urls import path

from services.views.populating_csc import PopulatingCSCAPIView
from services.views.company import CompanyListCreateAPIView, CompanyRetrieveUpdateDetailAPIView
from services.views.item import ItemListCreateAPIView, ItemRetrieveUpdateDetailAPIView
from services.views.item_category import ItemCategoryListCreateAPIView, ItemCategoryRetrieveUpdateDetailAPIView
from services.views.unit import UnitListCreateAPIView, UnitRetrieveUpdateDetailAPIView
from services.views.base_geolocations import (
    BaseCityListCreateAPIView,
    BaseCityRetrieveUpdateDetailAPIView,
    BaseStateListCreateAPIView,
    BaseStateRetrieveUpdateDetailAPIView,
    BaseCountryListCreateAPIView,
    BaseCountryRetrieveUpdateDetailAPIView
)
from services.views.geolocations import (
    CityListCreateAPIView,
    CityRetrieveUpdateDetailAPIView,
    StateListCreateAPIView,
    StateRetrieveUpdateDetailAPIView,
    CountryListCreateAPIView,
    CountryRetrieveUpdateDetailAPIView
)
from services.views.party import PartyListCreateAPIView, PartyRetrieveUpdateDetailAPIView
from services.views.tax import TaxListCreateAPIView, TaxRetrieveUpdateDetailAPIView


urlpatterns = [
    ###########################################
    # Populating CSC
    ###########################################
    path('initialize_csc', PopulatingCSCAPIView.as_view(), name="populating-csc"),
    ###########################################
    # Base Geolocations
    ###########################################
    path('country_base', BaseCountryListCreateAPIView.as_view(), name="country-base-lc"),
    path('country_base/<str:id>', BaseCountryRetrieveUpdateDetailAPIView.as_view(), name="country-base-rud"),
    path('state_base', BaseStateListCreateAPIView.as_view(), name="state-base-lc"),
    path('state_base/<str:id>', BaseStateRetrieveUpdateDetailAPIView.as_view(), name="state-base-rud"),
    path('city_base', BaseCityListCreateAPIView.as_view(), name="city-base-lc"),
    path('city_base/<str:id>', BaseCityRetrieveUpdateDetailAPIView.as_view(), name="city-base-rud"),
    ###########################################
    # Geolocations
    ###########################################
    path('country', CountryListCreateAPIView.as_view(), name="country-lc"),
    path('country/<str:id>', CountryRetrieveUpdateDetailAPIView.as_view(), name="country-rud"),
    path('state', StateListCreateAPIView.as_view(), name="state-lc"),
    path('state/<str:id>', StateRetrieveUpdateDetailAPIView.as_view(), name="state-rud"),
    path('city', CityListCreateAPIView.as_view(), name="city-lc"),
    path('city/<str:id>', CityRetrieveUpdateDetailAPIView.as_view(), name="city-rud"),
    ###########################################
    # Masters
    ###########################################
    path('company', CompanyListCreateAPIView.as_view(), name="company-lc"),
    path('company/<str:id>', CompanyRetrieveUpdateDetailAPIView.as_view(), name="company-rud"),
    path('item', ItemListCreateAPIView.as_view(), name="item-lc"),
    path('item/<str:id>', ItemRetrieveUpdateDetailAPIView.as_view(), name="item-rud"),
    path('item_category', ItemCategoryListCreateAPIView.as_view(), name="item-category-lc"),
    path('item_category/<str:id>', ItemCategoryRetrieveUpdateDetailAPIView.as_view(), name="item-category-rud"),
    path('unit', UnitListCreateAPIView.as_view(), name="unit-lc"),
    path('unit/<str:id>', UnitRetrieveUpdateDetailAPIView.as_view(), name="unit-rud"),
    path('party', PartyListCreateAPIView.as_view(), name="party-lc"),
    path('party/<str:id>', PartyRetrieveUpdateDetailAPIView.as_view(), name="party-rud"),
    path('tax', TaxListCreateAPIView.as_view(), name="tax-lc"),
    path('tax/<str:id>', TaxRetrieveUpdateDetailAPIView.as_view(), name="tax-rud"),
]
