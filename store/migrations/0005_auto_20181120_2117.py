# Generated by Django 2.1.1 on 2018-11-20 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20181117_2254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aricleimage',
            name='article',
        ),
        migrations.RemoveField(
            model_name='product',
            name='images',
        ),
        migrations.AddField(
            model_name='primage',
            name='product',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='store.Product'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='AricleImage',
        ),
        migrations.DeleteModel(
            name='Article',
        ),
    ]
