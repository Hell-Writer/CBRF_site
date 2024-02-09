# Generated by Django 4.2.9 on 2024-02-09 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Город')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Filial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_fact', models.CharField(max_length=500, verbose_name='Местонахождение филиала')),
                ('email', models.EmailField(max_length=254, verbose_name='Е-мейл')),
                ('schedule', models.JSONField(verbose_name='Расписание')),
                ('phone', models.IntegerField(verbose_name='Номер телефона')),
                ('city_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.city', verbose_name='Город')),
            ],
            options={
                'verbose_name': 'Филиал',
                'verbose_name_plural': 'Филиалы',
                'ordering': ['organisation_id'],
            },
        ),
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_short', models.CharField(max_length=50, verbose_name='Короткое наименование компании')),
                ('name_long', models.CharField(max_length=500, verbose_name='Полное наименование компании')),
                ('brand_name', models.CharField(max_length=250, verbose_name='Бренд')),
                ('inn', models.IntegerField(verbose_name='ИНН')),
                ('ogrn', models.IntegerField(verbose_name='ОГРН')),
                ('location_reg', models.CharField(max_length=550, verbose_name='Местонахождение')),
                ('date_reg', models.DateField(verbose_name='Дата регистрации')),
            ],
            options={
                'verbose_name': 'Организация',
                'verbose_name_plural': 'Организации',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='OrganisationType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название типа организации')),
            ],
            options={
                'verbose_name': 'Тип',
                'verbose_name_plural': 'Типы',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='Название продукта')),
                ('params', models.CharField(max_length=250, verbose_name='Другие параметры')),
                ('filial_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.filial', verbose_name='Филиал организации')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ProductClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название типа продукта')),
            ],
            options={
                'verbose_name': 'Тип продукта',
                'verbose_name_plural': 'Типы продуктов',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название типа продукта')),
                ('organisation_type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.organisationtype', verbose_name='Тип организации')),
                ('product_class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.productclass', verbose_name='Класс продукта')),
            ],
            options={
                'verbose_name': 'Тип продукта',
                'verbose_name_plural': 'Типы продуктов',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Город')),
            ],
            options={
                'verbose_name': 'Регион',
                'verbose_name_plural': 'Регионы',
                'ordering': ['name'],
            },
        ),
        migrations.DeleteModel(
            name='Company',
        ),
        migrations.AddField(
            model_name='product',
            name='product_type_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.producttype', verbose_name='Тип продукта'),
        ),
        migrations.AddField(
            model_name='organisation',
            name='organisation_type_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.organisationtype', verbose_name='Тип организации'),
        ),
        migrations.AddField(
            model_name='filial',
            name='organisation_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.organisation', verbose_name='Организация'),
        ),
        migrations.AddField(
            model_name='city',
            name='region_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.region', verbose_name='Регион'),
        ),
    ]
