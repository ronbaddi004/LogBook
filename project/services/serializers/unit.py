from rest_framework import serializers

from services.models import Unit, Company


class UnitSerializer(serializers.ModelSerializer):

    id                      = serializers.UUIDField(format="hex_verbose")
    my_company              = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all())

    name                    = serializers.CharField(max_length=100)

    created_at              = serializers.DateTimeField(read_only=True)
    updated_at              = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Unit
        fields = [
            'id',
            'my_company',

            'name',

            'created_at',
            'updated_at'
        ]
