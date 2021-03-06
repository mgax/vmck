# Generated by Django 2.1.5 on 2019-02-14 00:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artifact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=4096)),
                ('data', models.BinaryField()),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('new', 'New'), ('running', 'Running'), ('done', 'Done')], default='new', max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='artifact',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vmck.Job'),
        ),
    ]
