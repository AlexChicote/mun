# Generated by Django 2.1.2 on 2018-11-14 08:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('integrations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('integration_artist_id', models.CharField(max_length=256, null=True)),
                ('name', models.CharField(max_length=256)),
                ('integration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='integrations.Integration')),
            ],
        ),
    ]
