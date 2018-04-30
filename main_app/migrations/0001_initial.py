# Generated by Django 2.0.2 on 2018-04-29 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItems',
            fields=[
                ('menu_number', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('menu_item', models.CharField(max_length=50)),
                ('menu_link', models.CharField(max_length=200)),
                ('logged_in', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='SiteContacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=300)),
                ('email', models.EmailField(blank=True, max_length=100)),
                ('phone', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=1000)),
                ('message_replied', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='SiteOrders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=300)),
                ('email', models.EmailField(blank=True, max_length=100)),
                ('phone', models.CharField(max_length=50)),
                ('service_requested', models.CharField(choices=[('пълен', 'Пълен астрологичен пакет'), ('единичен', 'Хороскоп на един човек и прогноза'), ('по тема', 'Разглеждане на една тема в хороскопа и прогноза'), ('таро', 'Отговор на до 4 въпроса с таро')], max_length=300)),
                ('add_info', models.CharField(blank=True, max_length=1000)),
                ('request_finished', models.BooleanField(default=False)),
            ],
        ),
    ]