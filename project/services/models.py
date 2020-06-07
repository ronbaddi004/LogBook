from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import (
    AbstractBaseUser
)

# Create your models here.
phone_regex = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
)


MAX_DECIMAL_VALUE = 20
DECIMAL_PLACES_VALUE = 10


BASIS_CHOICES = (
    ("0", "Absolute Amount"),
    ("1", "Percentage")
)


PARTY_TYPE_CHOICES = (
    ("0", "Customer"),
    ("1", "Supplier")
)


NATURE_CHOICES = (
    ("0", "I Received"),
    ("1", "I Paid")
)


GST_REGISTRATION_TYPE_CHOICES = (
    ("0", "Registered"),
    ("1", "Unregistered")
)


class TaxTypeChoices(models.IntegerChoices):
    GST = 0
    VAT = 1


class BasisChoices(models.IntegerChoices):
    ABSOLUTE_AMOUNT = 0
    PERCENTAGE = 1


class PartyTypeChoices(models.IntegerChoices):
    CUSTOMER = 0
    SUPPLIER = 1


class NatureChoices(models.IntegerChoices):
    I_RECEIVED = 0
    I_PAID = 1


class GSTRegistrationTypeChoices(models.IntegerChoices):
    REGISTERED = 0
    UNREGISTERED = 1


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        null=True
    )
    first_name                  = models.CharField(max_length=100)
    last_name                   = models.CharField(max_length=100)
    mobile_number               = models.CharField(validators=[phone_regex], max_length=17, unique=True)
    active                      = models.BooleanField(default=True)
    staff                       = models.BooleanField(default=False) # a admin user; non super-user
    admin                       = models.BooleanField(default=False) # a superuser
    # notice the absence of a "Password field", that is built in.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # Email & Password are required by default.

    def get_full_name(self):
        """User's Full Name"""
        # The user is identified by their email address
        return self.first_name + " " + self.last_name

    def get_short_name(self):
        """User's Short name"""
        # The user is identified by their email address
        return self.first_name

    def __str__(self):              # __unicode__ on Python 2
        return f"{self.email}"

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        "Is the user active?"
        return self.active


class BaseCountry(models.Model):
    """BaseCountry"""
    name                = models.CharField(max_length=100)
    phone_code          = models.CharField(max_length=100)

    created_at          = models.DateTimeField(auto_now=True)
    updated_at          = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"


class BaseState(models.Model):
    """BaseState"""
    name                = models.CharField(max_length=100)
    my_country          = models.ForeignKey(BaseCountry, on_delete=models.CASCADE)

    created_at          = models.DateTimeField(auto_now=True)
    updated_at          = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"


class BaseCity(models.Model):
    """BaseCity"""
    name                = models.CharField(max_length=100)
    my_state            = models.ForeignKey(BaseState, on_delete=models.CASCADE)

    created_at          = models.DateTimeField(auto_now=True)
    updated_at          = models.DateTimeField(auto_now_add=True)

    created_at          = models.DateTimeField(auto_now=True)
    updated_at          = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"


class Company(models.Model):
    """Company"""
    id                      = models.UUIDField(primary_key=True, editable=False)

    owner                   = models.ForeignKey(User, on_delete=models.CASCADE)

    logo                    = models.ImageField(upload_to="photos", max_length=254, null=True)
    name                    = models.CharField(max_length=100)
    alias_name              = models.CharField(max_length=100, null=True)
    gstin                   = models.CharField(max_length=15, null=True)
    address                 = models.CharField(max_length=600, null=True)
    my_state                = models.ForeignKey(BaseState, on_delete=models.PROTECT, null=True)

    bank_account_number     = models.CharField(max_length=50, null=True)
    beneficiary_name        = models.CharField(max_length=100, null=True)
    ifsc_code               = models.CharField(max_length=100, null=True)
    bank_and_branch_name    = models.CharField(max_length=100, null=True)

    upi_id                  = models.CharField(max_length=100, null=True)
    terms_and_conditions    = models.CharField(max_length=2000, null=True)

    created_at              = models.DateTimeField(auto_now=True)
    updated_at              = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        # Changing upload_to on save
        for field in self._meta.fields:

            if field.name == 'logo':

                field.upload_to = f"photos/{self.owner.id}/company"

        super(Company, self).save(*args, **kwargs)


class Country(models.Model):
    """Country"""
    id                  = models.UUIDField(primary_key=True, editable=False)
    my_company          = models.ForeignKey(Company, on_delete=models.CASCADE)
    name                = models.CharField(max_length=100)

    created_at          = models.DateTimeField(auto_now=True)
    updated_at          = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"


class State(models.Model):
    """State"""
    id                  = models.UUIDField(primary_key=True, editable=False)
    name                = models.CharField(max_length=100)
    my_country          = models.ForeignKey(Country, on_delete=models.CASCADE)

    created_at          = models.DateTimeField(auto_now=True)
    updated_at          = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"


class City(models.Model):
    """City"""
    id                  = models.UUIDField(primary_key=True, editable=False)
    name                = models.CharField(max_length=100)
    my_state            = models.ForeignKey(State, on_delete=models.CASCADE)

    created_at          = models.DateTimeField(auto_now=True)
    updated_at          = models.DateTimeField(auto_now_add=True)

    created_at          = models.DateTimeField(auto_now=True)
    updated_at          = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"


class Party(models.Model):
    """Party"""
    id                          = models.UUIDField(primary_key=True, editable=False)
    my_company                  = models.ForeignKey(Company, on_delete=models.CASCADE)
    name                        = models.CharField(max_length=100)
    alias_name                  = models.CharField(max_length=100, null=True)
    mobile_number               = models.CharField(validators=[phone_regex], max_length=17, null=True)
    email_id                    = models.EmailField(max_length=254, null=True)

    logo                        = models.ImageField(upload_to='photos', max_length=254, null=True)
    party_type                  = models.IntegerField(choices=PartyTypeChoices.choices)
    billing_address             = models.CharField(max_length=1000, null=True)
    shipping_address            = models.CharField(max_length=1000, null=True)

    my_state                    = models.ForeignKey(State, on_delete=models.PROTECT, null=True)

    # GST Details
    gst_registration_type       = models.IntegerField(choices=GSTRegistrationTypeChoices.choices)
    gstin                       = models.CharField(max_length=15, null=True)

    # Credit Days Detail
    credit_days                 = models.DecimalField(max_digits=MAX_DECIMAL_VALUE, decimal_places=DECIMAL_PLACES_VALUE, null=True)
    credit_limit                = models.DecimalField(max_digits=MAX_DECIMAL_VALUE, decimal_places=DECIMAL_PLACES_VALUE, null=True)

    created_at                  = models.DateTimeField(auto_now=True)
    updated_at                  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        # Changing upload_to on save
        for field in self._meta.fields:

            if field.name == 'logo':

                field.upload_to = f"photos/{self.my_company.owner_id}/party"

        super(Party, self).save(*args, **kwargs)


class Tax(models.Model):
    id                          = models.UUIDField(primary_key=True, editable=False)
    my_company                  = models.ForeignKey(Company, on_delete=models.CASCADE)

    tax_type                    = models.IntegerField(choices=TaxTypeChoices.choices)

    name                        = models.CharField(max_length=100)
    alias_name                  = models.CharField(max_length=100, null=True)

    # GST
    igst_rate                   = models.DecimalField(max_digits=MAX_DECIMAL_VALUE, decimal_places=DECIMAL_PLACES_VALUE, null=True)
    cgst_rate                   = models.DecimalField(max_digits=MAX_DECIMAL_VALUE, decimal_places=DECIMAL_PLACES_VALUE, null=True)
    sgst_rate                   = models.DecimalField(max_digits=MAX_DECIMAL_VALUE, decimal_places=DECIMAL_PLACES_VALUE, null=True)

    # VAT
    rate                        = models.DecimalField(max_digits=MAX_DECIMAL_VALUE, decimal_places=DECIMAL_PLACES_VALUE, null=True)

    created_at                  = models.DateTimeField(auto_now=True)
    updated_at                  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"


class ItemCategory(models.Model):
    id                          = models.UUIDField(primary_key=True, editable=False)
    my_company                  = models.ForeignKey(Company, on_delete=models.CASCADE)

    name                        = models.CharField(max_length=100)
    alias_name                  = models.CharField(max_length=100, null=True)

    created_at                  = models.DateTimeField(auto_now=True)
    updated_at                  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"


class Unit(models.Model):
    id                          = models.UUIDField(primary_key=True, editable=False)
    my_company                  = models.ForeignKey(Company, on_delete=models.CASCADE)

    name                        = models.CharField(max_length=100)
    alias_name                  = models.CharField(max_length=100, null=True)

    created_at                  = models.DateTimeField(auto_now=True)
    updated_at                  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"


class Item(models.Model):
    """Item"""
    id                          = models.UUIDField(primary_key=True, editable=False)
    my_company                  = models.ForeignKey(Company, on_delete=models.CASCADE)

    name                        = models.CharField(max_length=100)
    alias_name                  = models.CharField(max_length=100, null=True)
    my_item_category            = models.ForeignKey(ItemCategory, on_delete=models.SET_NULL, null=True)
    item_code                   = models.CharField(max_length=100, null=True)
    description                 = models.CharField(max_length=500, null=True)

    image                       = models.ImageField(upload_to='photos/item', max_length=254, null=True)
    # Reorder Stock Detail
    minimum_stock_level         = models.DecimalField(max_digits=MAX_DECIMAL_VALUE, decimal_places=DECIMAL_PLACES_VALUE, null=True)
    reorder_stock_level         = models.DecimalField(max_digits=MAX_DECIMAL_VALUE, decimal_places=DECIMAL_PLACES_VALUE, null=True)
    maximum_stock_level         = models.DecimalField(max_digits=MAX_DECIMAL_VALUE, decimal_places=DECIMAL_PLACES_VALUE, null=True)

    # Price Detail
    sales_price                 = models.DecimalField(max_digits=MAX_DECIMAL_VALUE, decimal_places=DECIMAL_PLACES_VALUE, null=True)
    purchase_price              = models.DecimalField(max_digits=MAX_DECIMAL_VALUE, decimal_places=DECIMAL_PLACES_VALUE, null=True)
    mrp_price                   = models.DecimalField(max_digits=MAX_DECIMAL_VALUE, decimal_places=DECIMAL_PLACES_VALUE, null=True)

    # Wholesale rate
    wholesale_price             = models.DecimalField(max_digits=MAX_DECIMAL_VALUE, decimal_places=DECIMAL_PLACES_VALUE, null=True)
    wholesale_quantity          = models.DecimalField(max_digits=MAX_DECIMAL_VALUE, decimal_places=DECIMAL_PLACES_VALUE, null=True)

    # GST Detail
    hsn_code                    = models.CharField(max_length=100, null=True)
    my_tax                      = models.ForeignKey(Tax, on_delete=models.PROTECT)

    created_at                  = models.DateTimeField(auto_now=True)
    updated_at                  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        # Changing upload_to on save
        for field in self._meta.fields:

            if field.name == 'image':

                field.upload_to = f"photos/{self.my_company.owner_id}/item"

        super(Item, self).save(*args, **kwargs)


class UnitOfMeasure(models.Model):
    id                          = models.UUIDField(primary_key=True, editable=False)
    my_company                  = models.ForeignKey(Company, on_delete=models.CASCADE)

    name                        = models.CharField(max_length=100)
    alias_name                  = models.CharField(max_length=100, null=True)
    my_item                     = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="unit_of_measure")
    my_unit                     = models.ForeignKey(Unit, on_delete=models.PROTECT)
    value                       = models.DecimalField(max_digits=MAX_DECIMAL_VALUE, decimal_places=DECIMAL_PLACES_VALUE)

    created_at                  = models.DateTimeField(auto_now=True)
    updated_at                  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"


# class Bill(models.Model):
#     """Voucher"""
#     id                          = models.UUIDField(primary_key=True, editable=False)




class ItemBillDetail(models.Model):
    id                          = models.UUIDField(primary_key=True, editable=False)

    my_item                     = models.ForeignKey(Item, on_delete=models.PROTECT)
    quantity                    = models.DecimalField(max_digits=MAX_DECIMAL_VALUE, decimal_places=DECIMAL_PLACES_VALUE)
    price                       = models.DecimalField(max_digits=MAX_DECIMAL_VALUE, decimal_places=DECIMAL_PLACES_VALUE)
    discount_basis              = models.IntegerField(choices=BasisChoices.choices, null=True)
    discount                    = models.DecimalField(max_digits=MAX_DECIMAL_VALUE, decimal_places=DECIMAL_PLACES_VALUE, null=True)
    tax                         = models.DecimalField(max_digits=MAX_DECIMAL_VALUE, decimal_places=DECIMAL_PLACES_VALUE, null=True)
    amount                      = models.DecimalField(max_digits=MAX_DECIMAL_VALUE, decimal_places=DECIMAL_PLACES_VALUE)

    created_at                  = models.DateTimeField(auto_now=True)
    updated_at                  = models.DateTimeField(auto_now_add=True)


class PartyBillDetail(models.Model):
    """Voucher Party Row"""
    id                          = models.UUIDField(primary_key=True, editable=False)

    my_party                    = models.ForeignKey(Party, on_delete=models.PROTECT)

    amount                      = models.DecimalField(max_digits=MAX_DECIMAL_VALUE, decimal_places=DECIMAL_PLACES_VALUE)
    nature                      = models.IntegerField(choices=NatureChoices.choices)

    created_at                  = models.DateTimeField(auto_now=True)
    updated_at                  = models.DateTimeField(auto_now_add=True)
