from rest_framework import serializers

from django.db import transaction

from services.models import Item, UnitOfMeasure, Company, ItemCategory, Tax, MAX_DECIMAL_VALUE, DECIMAL_PLACES_VALUE
from services.serializers.unit_of_measure import UnitOfMeasureSerializer


class ItemSerializer(serializers.ModelSerializer):
    id                              = serializers.UUIDField(format="hex_verbose")
    my_company                      = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all())

    name                            = serializers.CharField(max_length=100)
    my_item_category                = serializers.PrimaryKeyRelatedField(queryset=ItemCategory.objects.all())
    item_code                       = serializers.CharField(max_length=100, allow_null=True)
    description                     = serializers.CharField(max_length=500, allow_null=True)

    minimum_stock_level             = serializers.DecimalField(max_digits=MAX_DECIMAL_VALUE, decimal_places=DECIMAL_PLACES_VALUE, allow_null=True)
    reorder_stock_level             = serializers.DecimalField(max_digits=MAX_DECIMAL_VALUE, decimal_places=DECIMAL_PLACES_VALUE, allow_null=True)
    maximum_stock_level             = serializers.DecimalField(max_digits=MAX_DECIMAL_VALUE, decimal_places=DECIMAL_PLACES_VALUE, allow_null=True)

    sale_price                      = serializers.DecimalField(max_digits=MAX_DECIMAL_VALUE, decimal_places=DECIMAL_PLACES_VALUE, allow_null=True)
    purchase_price                  = serializers.DecimalField(max_digits=MAX_DECIMAL_VALUE, decimal_places=DECIMAL_PLACES_VALUE, allow_null=True)
    mrp_price                       = serializers.DecimalField(max_digits=MAX_DECIMAL_VALUE, decimal_places=DECIMAL_PLACES_VALUE, allow_null=True)

    whole_sale_price                = serializers.DecimalField(max_digits=MAX_DECIMAL_VALUE, decimal_places=DECIMAL_PLACES_VALUE, allow_null=True)
    whole_sale_quantity             = serializers.DecimalField(max_digits=MAX_DECIMAL_VALUE, decimal_places=DECIMAL_PLACES_VALUE, allow_null=True)

    unit_of_measure                 = UnitOfMeasureSerializer(many=True)

    hsn_code                        = serializers.CharField(max_length=100, allow_null=True)
    my_tax                          = serializers.PrimaryKeyRelatedField(queryset=Tax.objects.all(), allow_null=True)

    created_at                      = serializers.DateTimeField(read_only=True)
    updated_at                      = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Item
        fields = [
            "id",
            "my_company",

            "name",
            "my_item_category",
            "item_code",
            "description",

            "minimum_stock_level",
            "reorder_stock_level",
            "maximum_stock_level",

            "sale_price",
            "purchase_price",
            "mrp_price",

            "whole_sale_price",
            "whole_sale_quantity",

            "unit_of_measure",

            "hsn_code",
            "my_tax",

            "created_at",
            "updated_at",
        ]

    def create(self, validated_data):

        with transaction.atomic():

            unit_of_measure_data = validated_data.pop("unit_of_measure")

            obj = Item.objects.create(**validated_data)

            unit_of_measure_list = []

            for uom_data in unit_of_measure_data:

                unit_of_measure_list.append(UnitOfMeasure(**uom_data))

            UnitOfMeasure.objects.bulk_create(unit_of_measure_list)

            return obj

    def update(self, validated_data, instance):

        with transaction.atomic():

            unit_of_measure_data = validated_data.pop("unit_of_measure")

            instance.unit_of_measure.all().delete()

            unit_of_measure_list = []

            for uom_data in unit_of_measure_data:

                unit_of_measure_list.append(UnitOfMeasure(**uom_data))

            UnitOfMeasure.objects.bulk_create(unit_of_measure_list)

            instance.name                   = validated_data.get("name", instance.name)
            instance.my_item_category       = validated_data.get("my_item_category", instance.my_item_category)
            instance.item_code              = validated_data.get("item_code", instance.item_code)
            instance.description            = validated_data.get("description", instance.description)
            instance.minimum_stock_level    = validated_data.get("minimum_stock_level", instance.minimum_stock_level)
            instance.reorder_stock_level    = validated_data.get("reorder_stock_level", instance.reorder_stock_level)
            instance.maximum_stock_level    = validated_data.get("maximum_stock_level", instance.maximum_stock_level)
            instance.sale_price             = validated_data.get("sale_price", instance.sale_price)
            instance.purchase_price         = validated_data.get("purchase_price", instance.purchase_price)
            instance.mrp_price              = validated_data.get("mrp_price", instance.mrp_price)
            instance.whole_sale_price       = validated_data.get("whole_sale_price", instance.whole_sale_price)
            instance.whole_sale_quantity    = validated_data.get("whole_sale_quantity", instance.whole_sale_quantity)
            instance.hsn_code               = validated_data.get("hsn_code", instance.hsn_code)
            instance.my_tax                 = validated_data.get("my_tax", instance.my_tax)

            instance.save()

            return instance
