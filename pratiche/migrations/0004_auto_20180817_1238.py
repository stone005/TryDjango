# Generated by Django 2.1 on 2018-08-17 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pratiche', '0003_auto_20180817_1218'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fncr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descrizione', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descrizione', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='pratica',
            name='fncr',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pratiche.Fncr'),
        ),
        migrations.AlterField(
            model_name='pratica',
            name='magistrato',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pratiche.Magistrato'),
        ),
        migrations.AlterField(
            model_name='pratica',
            name='tipologia',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pratiche.Tipo'),
        ),
    ]