# Generated by Django 2.2.28 on 2022-08-16 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0015_problemcategory_problemcategorylist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problemcategory',
            name='id',
            field=models.AutoField(db_index=True, primary_key=True, serialize=False),
        ),
    ]