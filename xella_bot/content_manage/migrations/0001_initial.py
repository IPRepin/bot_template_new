# Generated by Django 4.2.1 on 2023-05-15 05:49

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Services",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.TextField(verbose_name="Название Услуги")),
                ("description", models.TextField(verbose_name="Описание услуги")),
                (
                    "image",
                    models.TextField(verbose_name="ID или ссылка на изображение"),
                ),
            ],
            options={
                "verbose_name": "Услуга",
                "verbose_name_plural": "Услуги",
            },
        ),
        migrations.CreateModel(
            name="Stocks",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.TextField(verbose_name="Название акции")),
                ("description", models.TextField(verbose_name="Описание акции")),
                (
                    "image",
                    models.TextField(verbose_name="ID или ссылка на изображение"),
                ),
            ],
            options={
                "verbose_name": "Акция",
                "verbose_name_plural": "Акции",
            },
        ),
    ]
