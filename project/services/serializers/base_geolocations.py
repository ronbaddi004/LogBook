from rest_framework import serializers

from services.models import BaseCountry, BaseState, BaseCity


class BaseCountrySerializer(serializers.ModelSerializer):
    name                = serializers.CharField(max_length=100)
    phone_code          = serializers.CharField(max_length=100)

    created_at          = serializers.DateTimeField(read_only=True)
    updated_at          = serializers.DateTimeField(read_only=True)

    class Meta:
        model = BaseCountry
        fields = [
            'id',

            'name',
            'phone_code',

            'created_at',
            'updated_at'
        ]


class BaseStateSerializer(serializers.ModelSerializer):
    name                = serializers.CharField(max_length=100)
    my_country          = serializers.PrimaryKeyRelatedField(queryset=BaseCountry.objects.all())

    created_at          = serializers.DateTimeField(read_only=True)
    updated_at          = serializers.DateTimeField(read_only=True)

    class Meta:
        model = BaseState
        fields = [
            'id',

            'name',
            'my_country',

            'created_at',
            'updated_at'
        ]


class BaseCitySerializer(serializers.ModelSerializer):
    name                = serializers.CharField(max_length=100)
    my_state            = serializers.PrimaryKeyRelatedField(queryset=BaseState.objects.all())

    created_at          = serializers.DateTimeField(read_only=True)
    updated_at          = serializers.DateTimeField(read_only=True)

    class Meta:
        model = BaseCity
        fields = [
            'id',

            'name',
            'my_state',

            'created_at',
            'updated_at'
        ]
