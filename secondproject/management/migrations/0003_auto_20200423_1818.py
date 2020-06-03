# Generated by Django 3.0.4 on 2020-04-23 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_auto_20200417_1426'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manageuser',
            name='nickname',
        ),
        migrations.AddField(
            model_name='manageuser',
            name='age',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hospital',
            name='contact',
            field=models.IntegerField(max_length=20),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='fees',
            field=models.IntegerField(max_length=20),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='referred_by',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
