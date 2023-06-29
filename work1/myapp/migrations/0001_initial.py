# Generated by Django 4.2.2 on 2023-06-28 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('order_date', models.DateField()),
                ('company_name', models.CharField(max_length=100)),
                ('owner_name', models.CharField(max_length=100)),
                ('item', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('weight', models.FloatField()),
                ('shipment_request', models.CharField(max_length=100)),
                ('tracking_id', models.CharField(max_length=100)),
                ('length', models.IntegerField()),
                ('breadth', models.IntegerField()),
                ('height', models.IntegerField()),
                ('box_count', models.IntegerField()),
                ('specification', models.CharField(max_length=100)),
                ('quality_checklist', models.CharField(max_length=100)),
            ],
        ),
    ]