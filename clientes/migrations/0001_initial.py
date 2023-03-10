# Generated by Django 4.1.7 on 2023-03-06 03:53

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cliente",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nomeCliente", models.CharField(max_length=255)),
                ("sexo", models.CharField(max_length=20, null=True)),
                ("pessoa_fisica", models.BooleanField(default=True)),
                ("documento", models.CharField(max_length=20)),
                ("telefone", models.CharField(max_length=20)),
                ("celular", models.CharField(max_length=20, null=True)),
                ("email", models.EmailField(max_length=100)),
                ("dataCadastro", models.DateField(auto_now_add=True)),
                ("rua", models.CharField(max_length=70, null=True)),
                ("numero", models.CharField(max_length=15, null=True)),
                ("bairro", models.CharField(max_length=45, null=True)),
                ("cidade", models.CharField(max_length=45, null=True)),
                ("estado", models.CharField(max_length=20, null=True)),
                ("cep", models.CharField(max_length=20, null=True)),
                ("contato", models.CharField(max_length=45, null=True)),
                ("complemento", models.CharField(max_length=45, null=True)),
                ("fornecedor", models.BooleanField(default=False)),
            ],
        ),
    ]
