# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-28 05:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Postagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('briefing', models.CharField(max_length=50)),
                ('texto', models.TextField()),
                ('imagem', models.ImageField(blank=True, default=b'noimage.png', null=True, upload_to=b'media')),
                ('dataCriacao', models.DateTimeField(verbose_name=b'Data da Criacao')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
