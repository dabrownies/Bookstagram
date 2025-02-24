# Generated by Django 5.1.6 on 2025-02-22 22:14

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("library", "0002_genres_bookauthor_bookgenre_book_genre"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bookauthor",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="related_author_books",
                to="library.author",
            ),
        ),
        migrations.AlterField(
            model_name="bookauthor",
            name="book",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="related_book_authors",
                to="library.book",
            ),
        ),
        migrations.CreateModel(
            name="Edition",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("isbn", models.CharField(max_length=13, unique=True)),
                (
                    "kind",
                    models.CharField(
                        choices=[
                            ("Hardcover", "Hardcover"),
                            ("Paperback", "Paperback"),
                            ("ebook", "ebook"),
                            ("Audiobook", "Audiobook"),
                        ],
                        max_length=10,
                    ),
                ),
                (
                    "publication_year",
                    models.PositiveBigIntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(1500),
                            django.core.validators.MaxValueValidator(2025),
                        ]
                    ),
                ),
                ("language", models.CharField(max_length=50)),
                (
                    "book",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="related_editions",
                        to="library.book",
                    ),
                ),
                (
                    "publisher",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="related_publisher_editions",
                        to="library.publisher",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CoverImage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image_url", models.TextField()),
                ("is_primary", models.BooleanField(default=False)),
                (
                    "edition",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="related_edition_image",
                        to="library.edition",
                    ),
                ),
            ],
        ),
    ]
