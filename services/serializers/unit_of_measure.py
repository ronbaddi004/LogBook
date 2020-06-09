from rest_framework import serializers

from services.models import Company, Unit, UnitOfMeasure, MAX_DECIMAL_VALUE, DECIMAL_PLACES_VALUE


class UnitOfMeasureSerializer(serializers.ModelSerializer):

    id                      = serializers.UUIDField(format="hex_verbose")
    my_company              = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all())

    name                    = serializers.CharField(max_length=100)
    my_unit                 = serializers.PrimaryKeyRelatedField(queryset=Unit.objects.all())
    value                   = serializers.DecimalField(max_digits=MAX_DECIMAL_VALUE, decimal_places=DECIMAL_PLACES_VALUE)

    created_at              = serializers.DateTimeField(read_only=True)
    updated_at              = serializers.DateTimeField(read_only=True)

    class Meta:
        model = UnitOfMeasure
        fields = [
            'id',
            'my_company',

            'name',
            'my_unit',
            'value',

            'created_at',
            'updated_at'
        ]
