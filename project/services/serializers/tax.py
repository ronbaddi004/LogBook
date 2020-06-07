from rest_framework import serializers

from services.models import Tax, TaxTypeChoices, Company, MAX_DECIMAL_VALUE, DECIMAL_PLACES_VALUE


class TaxSerializer(serializers.ModelSerializer):
    id                          = serializers.UUIDField(format="hex_verbose")

    my_company                  = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all())

    tax_type                    = serializers.ChoiceField(choices=TaxTypeChoices.choices)

    name                        = serializers.CharField(max_length=100)
    alias_name                  = serializers.CharField(max_length=100, allow_null=True)

    # GST
    igst_rate                   = serializers.DecimalField(max_digits=MAX_DECIMAL_VALUE, decimal_places=DECIMAL_PLACES_VALUE, allow_null=True)
    cgst_rate                   = serializers.DecimalField(max_digits=MAX_DECIMAL_VALUE, decimal_places=DECIMAL_PLACES_VALUE, allow_null=True)
    sgst_rate                   = serializers.DecimalField(max_digits=MAX_DECIMAL_VALUE, decimal_places=DECIMAL_PLACES_VALUE, allow_null=True)

    # VAT
    rate                        = serializers.DecimalField(max_digits=MAX_DECIMAL_VALUE, decimal_places=DECIMAL_PLACES_VALUE, allow_null=True)

    created_at                  = serializers.DateTimeField(read_only=True)
    updated_at                  = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Tax
        fields = [
            'id',

            'my_company',

            'tax_type',

            'name',
            'alias_name',

            'igst_rate',
            'cgst_rate',
            'sgst_rate',

            'rate',

            'created_at',
            'updated_at'
        ]
