# Generated by Django 3.1.4 on 2022-01-16 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_invcategories'),
    ]

    operations = [
        migrations.CreateModel(
            name='Industryactivitymaterials',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('activityid', models.IntegerField(db_column='activityID')),
                ('quantity', models.IntegerField()),
            ],
            options={
                'db_table': 'industryactivitymaterials',
                'managed': False,
            },
        ),
    ]
