# Generated by Django 3.2 on 2021-04-19 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20210419_1839'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='publisher',
        ),
        migrations.AddField(
            model_name='author',
            name='email',
            field=models.EmailField(default='korea60@abv.bg', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='books.publisher'),
            preserve_default=False,
        ),
    ]
