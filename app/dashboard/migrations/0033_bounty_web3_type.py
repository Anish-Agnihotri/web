# Generated by Django 2.0 on 2018-01-19 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0032_auto_20180116_0746'),
    ]

    operations = [
        migrations.AddField(
            model_name='bounty',
            name='web3_type',
            field=models.CharField(default='legacy_gitcoin', max_length=50),
        ),
    ]
