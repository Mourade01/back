# Generated by Django 4.1 on 2023-01-03 12:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='KycInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('surname', models.CharField(max_length=200)),
                ('sex', models.CharField(max_length=2)),
                ('dateofbirth', models.DateField()),
                ('placeofbirth', models.CharField(max_length=200)),
                ('expirationdate', models.DateField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('mkz', models.TextField()),
                ('description', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
