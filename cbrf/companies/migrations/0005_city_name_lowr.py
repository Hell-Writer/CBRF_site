# Generated by Django 4.2.9 on 2024-06-20 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("companies", "0004_alter_organisationtype_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="city",
            name="name_lowr",
            field=models.CharField(
                default="sd", max_length=150, verbose_name="Город маленький"
            ),
            preserve_default=False,
        ),
    ]
