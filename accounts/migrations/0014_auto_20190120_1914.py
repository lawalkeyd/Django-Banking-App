# Generated by Django 2.1 on 2019-01-20 19:14

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('accounts', '0013_remove_transactions_account_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accounts',
            name='user',
        ),
        migrations.DeleteModel(
            name='Accounts',
        ),
    ]