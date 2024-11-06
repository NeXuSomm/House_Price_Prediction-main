
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.FloatField()),
                ('bedrooms', models.IntegerField()),
                ('bathrooms', models.IntegerField()),
                ('stories', models.IntegerField()),
                ('mainroad', models.BooleanField()),
                ('guestroom', models.BooleanField()),
                ('basement', models.BooleanField()),
                ('hotwaterheating', models.BooleanField()),
                ('airconditioning', models.BooleanField()),
                ('parking', models.IntegerField()),
                ('prefarea', models.BooleanField()),
                ('furnishingstatus', models.CharField(max_length=255)),
            ],
        ),
    ]
