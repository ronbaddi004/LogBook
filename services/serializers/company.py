from rest_framework import serializers

from services.models import Company, User, BaseState


class CompanySerializer(serializers.ModelSerializer):
    id                      = serializers.UUIDField(format="hex_verbose")

    owner                   = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    name                    = serializers.CharField(max_length=100)
    gstin                   = serializers.CharField(max_length=15, allow_null=True)
    address                 = serializers.CharField(max_length=600, allow_null=True)
    my_state                = serializers.PrimaryKeyRelatedField(queryset=BaseState.objects.all())

    bank_account_number     = serializers.CharField(max_length=50, allow_null=True)
    beneficiary_name        = serializers.CharField(max_length=100, allow_null=True)
    ifsc_code               = serializers.CharField(max_length=100, allow_null=True)
    bank_and_branch_name    = serializers.CharField(max_length=100, allow_null=True)

    upi_id                  = serializers.CharField(max_length=100, allow_null=True)
    terms_and_conditions    = serializers.CharField(max_length=2000, allow_null=True)

    created_at              = serializers.DateTimeField(read_only=True)
    updated_at              = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Company
        fields = [
            "id",

            "owner",
            # "logo",
            "name",
            "gstin",
            "address",
            "my_state",
            "bank_account_number",
            "beneficiary_name",
            "ifsc_code",
            "bank_and_branch_name",
            "upi_id",
            "terms_and_conditions",

            "created_at",
            "updated_at",
        ]
