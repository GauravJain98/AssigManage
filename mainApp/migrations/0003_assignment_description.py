# Generated by Django 2.0.7 on 2018-07-14 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_auto_20180714_0011'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='description',
            field=models.CharField(default='fse', max_length=100),
            preserve_default=False,
        ),
    ]
