# Generated by Django 3.2.5 on 2021-07-15 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nature_club', '0005_slider'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slider',
            name='Images',
        ),
        migrations.AddField(
            model_name='slider',
            name='Full_image',
            field=models.FileField(default='uu', upload_to='Slider'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='slider',
            name='Small_image',
            field=models.FileField(default='j', upload_to='Slider'),
            preserve_default=False,
        ),
    ]