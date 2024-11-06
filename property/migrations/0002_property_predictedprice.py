
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='predictedprice',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
    ]
