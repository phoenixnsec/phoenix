# Generated by Django 3.2.7 on 2022-04-20 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PhoenixApp', '0006_backenddevelopment'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvanceBackendDevelopment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=100)),
                ('email', models.CharField(default='', max_length=100)),
                ('department', models.CharField(default='', max_length=100)),
                ('contact', models.CharField(default='', max_length=100)),
                ('college', models.CharField(default='', max_length=100)),
                ('session', models.CharField(default='', max_length=100)),
                ('prior', models.CharField(default='', max_length=100)),
                ('date', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'An Advanced Workshop in Backend Development',
            },
        ),
    ]
