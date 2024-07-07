# Generated by Django 2.2.2 on 2022-03-16 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('sale_price', models.FloatField()),
                ('cost_price', models.FloatField()),
                ('weight', models.FloatField()),
                ('sort', models.IntegerField()),
                ('produce_date', models.DateField()),
                ('limit_date', models.DateField()),
                ('lower', models.FloatField(default=0)),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(max_length=20)),
                ('pwd', models.CharField(max_length=40)),
                ('name', models.CharField(max_length=20)),
                ('gender', models.IntegerField(default=0)),
                ('phone', models.CharField(max_length=11)),
                ('authority', models.IntegerField(default=0)),
                ('isDelete', models.BooleanField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now=True)),
                ('type', models.IntegerField()),
                ('content', models.TextField()),
                ('contact', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('isRead', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=40)),
                ('phone', models.CharField(max_length=11)),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.IntegerField()),
                ('date', models.DateField(auto_now=True)),
                ('purchase_num', models.IntegerField(null=True)),
                ('sale_num', models.IntegerField(null=True)),
                ('withdraw_num', models.IntegerField(null=True)),
                ('goods', models.ForeignKey(on_delete=True, to='app.Goods')),
            ],
        ),
        migrations.AddField(
            model_name='goods',
            name='provider',
            field=models.ForeignKey(on_delete=True, to='app.Provider'),
        ),
    ]
