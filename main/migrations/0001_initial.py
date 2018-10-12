# Generated by Django 2.1.1 on 2018-10-11 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cab_Number', models.CharField(max_length=20)),
                ('Work_Time', models.IntegerField()),
                ('Start_Date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Cab_History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cab_Number', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.Cab')),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('Name', models.CharField(max_length=100)),
                ('Driver_ID', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('Work_Time', models.IntegerField()),
                ('Start_Date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='ID_Scan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateTimeField()),
                ('Cab_Number', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.Cab')),
                ('Driver_ID', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.Driver')),
            ],
        ),
        migrations.CreateModel(
            name='Payment_History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Payment', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('Name', models.CharField(max_length=100)),
                ('Registration_Number', models.CharField(max_length=9)),
                ('RFID', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('Email', models.EmailField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='payment_history',
            name='RFID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Student'),
        ),
        migrations.AddField(
            model_name='id_scan',
            name='RFID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Student'),
        ),
        migrations.AddField(
            model_name='cab_history',
            name='Driver_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.Driver'),
        ),
    ]
