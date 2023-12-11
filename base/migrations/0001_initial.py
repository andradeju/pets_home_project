# Generated by Django 4.2.6 on 2023-11-14 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnimalAdocao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=51)),
                ('email', models.EmailField(max_length=77)),
                ('cpf', models.CharField(max_length=11)),
                ('dataNascimento', models.DateField()),
                ('telefone', models.CharField(max_length=16)),
                ('profissao', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=255)),
                ('cidade', models.CharField(max_length=102)),
                ('estado', models.CharField(max_length=2)),
                ('cep', models.CharField(max_length=9)),
                ('motivoAdocao', models.TextField()),
                ('emCasoDeViagem', models.TextField()),
                ('experienciaAnterior', models.TextField()),
                ('temAnimal', models.BooleanField()),
                ('data', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
