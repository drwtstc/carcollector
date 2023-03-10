# Generated by Django 4.1.3 on 2023-01-19 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_maint_options_alter_maint_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('purpose', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='parts',
            field=models.ManyToManyField(to='main_app.part'),
        ),
    ]
