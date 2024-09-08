# Generated by Django 5.0.6 on 2024-08-31 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("transactions", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transaction",
            name="transaction_type",
            field=models.IntegerField(
                choices=[
                    (1, "Deposite"),
                    (2, "Withdrawal"),
                    (3, "Loan"),
                    (4, "Loan Paid"),
                    (5, "Transfer"),
                    (6, "Received"),
                ],
                null=True,
            ),
        ),
    ]
