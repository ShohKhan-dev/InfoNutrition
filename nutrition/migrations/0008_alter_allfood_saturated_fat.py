# Generated by Django 4.1.3 on 2022-12-28 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutrition', '0007_alter_userlog_calcium_alter_userlog_calories_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allfood',
            name='saturated_fat',
            field=models.CharField(max_length=100),
        ),
    ]