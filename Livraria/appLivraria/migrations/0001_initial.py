# Generated by Django 3.1.1 on 2020-09-02 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=50)),
                ('isbn', models.CharField(max_length=50)),
                ('numeroPaginas', models.IntegerField()),
                ('titulo', models.CharField(max_length=50)),
                ('anoPublicacao', models.IntegerField()),
                ('emailEditora', models.EmailField(max_length=254)),
            ],
        ),
    ]
