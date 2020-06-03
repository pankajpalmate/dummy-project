# Generated by Django 3.0.4 on 2020-04-15 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('contact', models.IntegerField()),
                ('referred_by', models.IntegerField()),
                ('date', models.DateField()),
                ('fees', models.IntegerField()),
            ],
        ),
    ]
