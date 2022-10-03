# Generated by Django 4.0rc1 on 2021-12-06 00:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shuttleBuddy', '0002_socialgame'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('court', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shuttleBuddy.court')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shuttleBuddy.player')),
                ('social_game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shuttleBuddy.socialgame')),
            ],
        ),
    ]