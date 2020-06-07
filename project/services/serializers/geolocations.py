from rest_framework import serializers

from services.models import Country, State, City


class CountrySerializer(serializers.ModelSerializer):
    id                  = serializers.UUIDField(format="hex_verbose")
    name                = serializers.CharField(max_length=100)
    phone_code          = serializers.CharField(max_length=100)

    created_at          = serializers.DateTimeField(read_only=True)
    updated_at          = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Country
        fields = [
            'id',

            'name',
            'phone_code',

            'created_at',
            'updated_at'
        ]


class StateSerializer(serializers.ModelSerializer):
    id                  = serializers.UUIDField(format="hex_verbose")
    name                = serializers.CharField(max_length=100)
    my_country          = serializers.PrimaryKeyRelatedField(queryset=Country.objects.all())

    created_at          = serializers.DateTimeField(read_only=True)
    updated_at          = serializers.DateTimeField(read_only=True)

    class Meta:
        model = State
        fields = [
            'id',

            'name',
            'my_country',

            'created_at',
            'updated_at'
        ]


class CitySerializer(serializers.ModelSerializer):
    id                  = serializers.UUIDField(format="hex_verbose")
    name                = serializers.CharField(max_length=100)
    my_state            = serializers.PrimaryKeyRelatedField(queryset=State.objects.all())

    created_at          = serializers.DateTimeField(read_only=True)
    updated_at          = serializers.DateTimeField(read_only=True)

    class Meta:
        model = City
        fields = [
            'id',

            'name',
            'my_state',

            'created_at',
            'updated_at'
        ]
