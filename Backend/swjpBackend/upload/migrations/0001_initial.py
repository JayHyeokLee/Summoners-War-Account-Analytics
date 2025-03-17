# Generated by Django 5.1.4 on 2025-03-17 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedJSONFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='json_files/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserAVG',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(max_length=15)),
                ('global_avg', models.DecimalField(decimal_places=2, max_digits=5)),
                ('vio_avg', models.DecimalField(decimal_places=2, max_digits=5)),
                ('will_avg', models.DecimalField(decimal_places=2, max_digits=5)),
                ('swift_avg', models.DecimalField(decimal_places=2, max_digits=5)),
                ('des_avg', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
