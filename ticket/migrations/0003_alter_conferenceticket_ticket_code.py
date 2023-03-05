# Generated by Django 4.1.5 on 2023-03-01 10:34

from django.db import migrations, models
import ticket.models


class Migration(migrations.Migration):
    dependencies = [
        ("ticket", "0002_alter_conferencetickettype_min_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="conferenceticket",
            name="ticket_code",
            field=models.CharField(
                db_index=True,
                default=ticket.models.make_ticket_code,
                max_length=25,
                unique=True,
            ),
        ),
    ]
