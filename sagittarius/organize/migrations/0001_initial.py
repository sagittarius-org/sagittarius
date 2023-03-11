# Generated by Django 4.1.7 on 2023-03-11 15:25

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import django_extensions.db.fields
import sagittarius.organize.models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("rules", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Club",
            fields=[
                ("uuid", models.UUIDField(primary_key=True, serialize=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(blank=True, max_length=128)),
                (
                    "country",
                    django_countries.fields.CountryField(blank=True, max_length=2),
                ),
            ],
            options={
                "abstract": False,
                "default_permissions": [],
            },
        ),
        migrations.CreateModel(
            name="Competition",
            fields=[
                ("uuid", models.UUIDField(primary_key=True, serialize=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(blank=True, max_length=128)),
            ],
            options={
                "abstract": False,
                "default_permissions": [],
            },
        ),
        migrations.CreateModel(
            name="Event",
            fields=[
                ("uuid", models.UUIDField(primary_key=True, serialize=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "competition",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="organize.competition",
                    ),
                ),
                (
                    "rule_set",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="rules.ruleset"
                    ),
                ),
            ],
            options={
                "abstract": False,
                "default_permissions": [],
            },
        ),
        migrations.CreateModel(
            name="Level",
            fields=[
                ("uuid", models.UUIDField(primary_key=True, serialize=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "stars",
                    models.SmallIntegerField(
                        choices=[
                            (1, "One Star"),
                            (2, "Two Stars"),
                            (3, "Three Stars"),
                            (4, "Four Stars"),
                            (5, "Five Stars"),
                        ],
                        null=True,
                    ),
                ),
                (
                    "country",
                    django_countries.fields.CountryField(blank=True, max_length=2),
                ),
                ("name", models.CharField(blank=True, max_length=128)),
                ("active", models.BooleanField(default=True)),
            ],
            options={
                "abstract": False,
                "default_permissions": [],
            },
        ),
        migrations.CreateModel(
            name="RecurringMeeting",
            fields=[
                ("uuid", models.UUIDField(primary_key=True, serialize=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=128)),
            ],
            options={
                "abstract": False,
                "default_permissions": [],
            },
        ),
        migrations.CreateModel(
            name="Team",
            fields=[
                ("uuid", models.UUIDField(primary_key=True, serialize=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(blank=True, max_length=128)),
                (
                    "country",
                    django_countries.fields.CountryField(blank=True, max_length=2),
                ),
                (
                    "competition",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="organize.competition",
                    ),
                ),
            ],
            options={
                "abstract": False,
                "default_permissions": [],
            },
        ),
        migrations.CreateModel(
            name="Rider",
            fields=[
                ("uuid", models.UUIDField(primary_key=True, serialize=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("left_handed", models.BooleanField(default=False)),
                (
                    "birth_year",
                    models.IntegerField(
                        default=sagittarius.organize.models.thirty_years_ago,
                        validators=[
                            django.core.validators.MinValueValidator(1900),
                            django.core.validators.MaxValueValidator(2050),
                        ],
                    ),
                ),
                (
                    "country",
                    django_countries.fields.CountryField(blank=True, max_length=2),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
                "default_permissions": [],
            },
        ),
        migrations.CreateModel(
            name="Registration",
            fields=[
                ("uuid", models.UUIDField(primary_key=True, serialize=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "country",
                    django_countries.fields.CountryField(blank=True, max_length=2),
                ),
                (
                    "competition",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="organize.competition",
                    ),
                ),
                (
                    "rider",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="organize.rider"
                    ),
                ),
                (
                    "team",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="organize.team",
                    ),
                ),
            ],
            options={
                "abstract": False,
                "default_permissions": [],
            },
        ),
        migrations.CreateModel(
            name="Organizer",
            fields=[
                ("uuid", models.UUIDField(primary_key=True, serialize=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "competition",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="organize.competition",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
                "default_permissions": [],
            },
        ),
        migrations.CreateModel(
            name="Meeting",
            fields=[
                ("uuid", models.UUIDField(primary_key=True, serialize=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=128)),
                (
                    "slug",
                    django_extensions.db.fields.AutoSlugField(
                        blank=True, editable=False, overwrite=True, populate_from="name"
                    ),
                ),
                ("is_international", models.BooleanField(default=False)),
                ("location", models.CharField(blank=True, max_length=128)),
                (
                    "country",
                    django_countries.fields.CountryField(blank=True, max_length=2),
                ),
                ("website", models.URLField(blank=True)),
                ("date", models.DateField()),
                (
                    "contact",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
                "default_permissions": [],
            },
        ),
        migrations.CreateModel(
            name="Horse",
            fields=[
                ("uuid", models.UUIDField(primary_key=True, serialize=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(blank=True, max_length=128)),
                (
                    "club",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="organize.club",
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
                "default_permissions": [],
            },
        ),
        migrations.CreateModel(
            name="Group",
            fields=[
                (
                    "order",
                    models.PositiveIntegerField(
                        db_index=True, editable=False, verbose_name="order"
                    ),
                ),
                ("uuid", models.UUIDField(primary_key=True, serialize=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="organize.event"
                    ),
                ),
            ],
            options={
                "ordering": ("order",),
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="competition",
            name="level",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="organize.level"
            ),
        ),
        migrations.AddField(
            model_name="competition",
            name="meeting",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="organize.meeting"
            ),
        ),
    ]