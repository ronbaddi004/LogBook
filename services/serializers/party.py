from rest_framework import serializers

from services.models import Party, PartyTypeChoices, phone_regex, Company, State, GSTRegistrationTypeChoices, MAX_DECIMAL_VALUE, DECIMAL_PLACES_VALUE


class PartySerializer(serializers.ModelSerializer):
    id                              = serializers.UUIDField(format="hex_verbose")

    my_company                      = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all())
    name                            = serializers.CharField(max_length=100)
    alias_name                      = serializers.CharField(max_length=100, allow_null=True)
    mobile_number                   = serializers.CharField(validators=[phone_regex], max_length=17, allow_null=True)
    email_id                        = serializers.EmailField(allow_null=True)

    party_type                      = serializers.ChoiceField(choices=PartyTypeChoices.choices)
    billing_address                 = serializers.CharField(max_length=1000, allow_null=True)
    shipping_address                = serializers.CharField(max_length=1000, allow_null=True)

    my_state                        = serializers.PrimaryKeyRelatedField(queryset=State.objects.all())

    # GST Details
    gst_registration_type           = serializers.ChoiceField(choices=GSTRegistrationTypeChoices.choices)
    gstin                           = serializers.CharField(max_length=15, allow_null=True)

    credit_days                     = serializers.DecimalField(max_digits=MAX_DECIMAL_VALUE, decimal_places=DECIMAL_PLACES_VALUE, allow_null=True)
    credit_limit                    = serializers.DecimalField(max_digits=MAX_DECIMAL_VALUE, decimal_places=DECIMAL_PLACES_VALUE, allow_null=True)

    created_at                      = serializers.DateTimeField(read_only=True)
    updated_at                      = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Party
        fields = [
            'id',

            'my_company',
            'name',
            'alias_name',
            'mobile_number',
            'email_id',

            'party_type',
            'billing_address',
            'shipping_address',

            'my_state',

            'gst_registration_type',
            'gstin',

            'credit_days',
            'credit_limit',

            'created_at',
            'updated_at'
        ]
