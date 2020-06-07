from django.contrib import admin

# Register your models here.
from services.models import (
    BaseCountry,
    BaseState,
    BaseCity,
    User,
    Company,
    Unit,
    UnitOfMeasure,
    Country,
    State,
    City,
    Party,
    ItemCategory,
    Tax,
    Item,
    PartyBillDetail,
    ItemBillDetail
)

admin.site.register(BaseCountry)
admin.site.register(BaseState)
admin.site.register(BaseCity)
admin.site.register(Company)
admin.site.register(User)
admin.site.register(Unit)
admin.site.register(UnitOfMeasure)
admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Party)
admin.site.register(ItemCategory)
admin.site.register(Item)
admin.site.register(Tax)
admin.site.register(PartyBillDetail)
admin.site.register(ItemBillDetail)
