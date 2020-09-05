# Generated by Django 3.1.1 on 2020-09-05 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShirtModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('shirt_size', models.CharField(choices=[('P', 'Pequeno'), ('M', 'Medio'), ('G', 'Grande')], max_length=1)),
            ],
        ),
    ]
