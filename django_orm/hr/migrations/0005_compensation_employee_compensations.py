# Generated by Django 4.2.14 on 2024-07-13 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0004_department_employee_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compensation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='compensations',
            field=models.ManyToManyField(to='hr.compensation'),
        ),
    ]
