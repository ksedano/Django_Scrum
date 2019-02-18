# Generated by Django 2.1.7 on 2019-02-11 16:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Projecte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(default='Nou projecte...', max_length=200)),
                ('descripcio', models.TextField(blank=True, default='Nou projecte...', null=True)),
                ('grup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
                ('product_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_owner', to=settings.AUTH_USER_MODEL)),
                ('scrum_master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scrum_master', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Spec',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcio', models.TextField()),
                ('dificultat', models.CharField(choices=[('D', 'Desconeguda'), ('B', 'Baixa'), ('M', 'Mitjana'), ('A', 'Alta')], default='D', max_length=1)),
                ('hores', models.IntegerField(default=0)),
                ('developer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('projecte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Projecte')),
            ],
        ),
        migrations.CreateModel(
            name='Sprint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inici', models.DateField()),
                ('data_final', models.DateField()),
                ('hores', models.IntegerField(default=0, help_text='Hores disponibles per Sprint...')),
                ('projecte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Projecte')),
            ],
        ),
        migrations.AddField(
            model_name='spec',
            name='sprint',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Sprint'),
        ),
    ]