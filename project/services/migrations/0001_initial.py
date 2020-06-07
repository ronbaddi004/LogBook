# Generated by Django 3.0.6 on 2020-06-07 18:32

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseCountry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_code', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='BaseState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('my_country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.BaseCountry')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('logo', models.ImageField(max_length=254, null=True, upload_to='photos')),
                ('name', models.CharField(max_length=100)),
                ('alias_name', models.CharField(max_length=100, null=True)),
                ('gstin', models.CharField(max_length=15, null=True)),
                ('address', models.CharField(max_length=600, null=True)),
                ('bank_account_number', models.CharField(max_length=50, null=True)),
                ('beneficiary_name', models.CharField(max_length=100, null=True)),
                ('ifsc_code', models.CharField(max_length=100, null=True)),
                ('bank_and_branch_name', models.CharField(max_length=100, null=True)),
                ('upi_id', models.CharField(max_length=100, null=True)),
                ('terms_and_conditions', models.CharField(max_length=2000, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('my_state', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='services.BaseState')),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('my_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('alias_name', models.CharField(max_length=100, null=True)),
                ('item_code', models.CharField(max_length=100, null=True)),
                ('description', models.CharField(max_length=500, null=True)),
                ('image', models.ImageField(max_length=254, null=True, upload_to='photos/item')),
                ('minimum_stock_level', models.DecimalField(decimal_places=10, max_digits=20, null=True)),
                ('reorder_stock_level', models.DecimalField(decimal_places=10, max_digits=20, null=True)),
                ('maximum_stock_level', models.DecimalField(decimal_places=10, max_digits=20, null=True)),
                ('sales_price', models.DecimalField(decimal_places=10, max_digits=20, null=True)),
                ('purchase_price', models.DecimalField(decimal_places=10, max_digits=20, null=True)),
                ('mrp_price', models.DecimalField(decimal_places=10, max_digits=20, null=True)),
                ('wholesale_price', models.DecimalField(decimal_places=10, max_digits=20, null=True)),
                ('wholesale_quantity', models.DecimalField(decimal_places=10, max_digits=20, null=True)),
                ('hsn_code', models.CharField(max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('my_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('alias_name', models.CharField(max_length=100, null=True)),
                ('mobile_number', models.CharField(max_length=17, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('email_id', models.EmailField(max_length=254, null=True)),
                ('logo', models.ImageField(max_length=254, null=True, upload_to='photos')),
                ('party_type', models.IntegerField(choices=[(0, 'Customer'), (1, 'Supplier')])),
                ('billing_address', models.CharField(max_length=1000, null=True)),
                ('shipping_address', models.CharField(max_length=1000, null=True)),
                ('gst_registration_type', models.IntegerField(choices=[(0, 'Registered'), (1, 'Unregistered')])),
                ('gstin', models.CharField(max_length=15, null=True)),
                ('credit_days', models.DecimalField(decimal_places=10, max_digits=20, null=True)),
                ('credit_limit', models.DecimalField(decimal_places=10, max_digits=20, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('my_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('alias_name', models.CharField(max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('my_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.Company')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, null=True, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('mobile_number', models.CharField(max_length=17, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('active', models.BooleanField(default=True)),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UnitOfMeasure',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('alias_name', models.CharField(max_length=100, null=True)),
                ('value', models.DecimalField(decimal_places=10, max_digits=20)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('my_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.Company')),
                ('my_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='unit_of_measure', to='services.Item')),
                ('my_unit', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='services.Unit')),
            ],
        ),
        migrations.CreateModel(
            name='Tax',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('tax_type', models.IntegerField(choices=[(0, 'Gst'), (1, 'Vat')])),
                ('name', models.CharField(max_length=100)),
                ('alias_name', models.CharField(max_length=100, null=True)),
                ('igst_rate', models.DecimalField(decimal_places=10, max_digits=20, null=True)),
                ('cgst_rate', models.DecimalField(decimal_places=10, max_digits=20, null=True)),
                ('sgst_rate', models.DecimalField(decimal_places=10, max_digits=20, null=True)),
                ('rate', models.DecimalField(decimal_places=10, max_digits=20, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('my_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.Company')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('my_country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.Country')),
            ],
        ),
        migrations.CreateModel(
            name='PartyBillDetail',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('amount', models.DecimalField(decimal_places=10, max_digits=20)),
                ('nature', models.IntegerField(choices=[(0, 'I Received'), (1, 'I Paid')])),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('my_party', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='services.Party')),
            ],
        ),
        migrations.AddField(
            model_name='party',
            name='my_state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='services.State'),
        ),
        migrations.CreateModel(
            name='ItemCategory',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('alias_name', models.CharField(max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('my_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.Company')),
            ],
        ),
        migrations.CreateModel(
            name='ItemBillDetail',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('quantity', models.DecimalField(decimal_places=10, max_digits=20)),
                ('price', models.DecimalField(decimal_places=10, max_digits=20)),
                ('discount_basis', models.IntegerField(choices=[(0, 'Absolute Amount'), (1, 'Percentage')], null=True)),
                ('discount', models.DecimalField(decimal_places=10, max_digits=20, null=True)),
                ('tax', models.DecimalField(decimal_places=10, max_digits=20, null=True)),
                ('amount', models.DecimalField(decimal_places=10, max_digits=20)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('my_item', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='services.Item')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='my_item_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='services.ItemCategory'),
        ),
        migrations.AddField(
            model_name='item',
            name='my_tax',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='services.Tax'),
        ),
        migrations.AddField(
            model_name='company',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.User'),
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('my_state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.State')),
            ],
        ),
        migrations.CreateModel(
            name='BaseCity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('my_state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.BaseState')),
            ],
        ),
    ]
