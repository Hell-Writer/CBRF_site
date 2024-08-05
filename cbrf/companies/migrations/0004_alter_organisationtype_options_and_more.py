# Generated by Django 4.2.9 on 2024-06-20 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "companies",
            "0003_alter_filial_options_rename_region_id_city_region_and_more",
        ),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="organisationtype",
            options={
                "ordering": ["name"],
                "verbose_name": "Тип организации",
                "verbose_name_plural": "Типы организаций",
            },
        ),
        migrations.AlterModelOptions(
            name="productclass",
            options={
                "ordering": ["name"],
                "verbose_name": "Класс продукта",
                "verbose_name_plural": "Классы продуктов",
            },
        ),
    ]