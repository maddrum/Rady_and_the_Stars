# Generated by Django 2.0.2 on 2018-04-29 11:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=500, unique=True)),
                ('course_start_date', models.DateField()),
                ('course_end_date', models.DateField()),
                ('user_visited_course', models.ManyToManyField(related_name='user_visited', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CoursesVideoLinks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('URL_link', models.URLField()),
                ('video_is_about', models.CharField(max_length=150)),
                ('courseID_video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_video', to='user_content.Courses')),
            ],
        ),
        migrations.CreateModel(
            name='SiteUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthday', models.DateField(blank=True)),
                ('hour_of_birth', models.TimeField(blank=True)),
                ('phone', models.CharField(blank=True, max_length=50)),
                ('used_service', models.BooleanField(choices=[(True, 'Да'), (False, 'Не')], default=False)),
                ('profile_pic', models.ImageField(blank=True, upload_to='profile_pics')),
                ('horoscopes', models.TextField(blank=True)),
                ('city_of_birth', models.CharField(blank=True, max_length=250)),
                ('country_of_birth', models.CharField(blank=True, max_length=250)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
