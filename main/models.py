from django.db import models

# Create your models here.
class Student(models.Model):
    Name=models.CharField(max_length=100)
    Registration_Number=models.CharField(max_length=9)
    RFID=models.CharField(max_length=15,primary_key=True)
    Email=models.EmailField(max_length=100)


    def __str__(self):
        return self.Registration_Number

class Driver(models.Model):
    Name=models.CharField(max_length=100)
    Driver_ID=models.CharField(max_length=25, primary_key=True)
    Work_Time=models.IntegerField()
    Start_Date=models.DateField()

    def __str__(self):
        return self.Driver_ID

class Cab(models.Model):
    Cab_Number=models.CharField(max_length=20)
    Work_Time = models.IntegerField()
    Start_Date = models.DateField()

    def __str__(self):
        return self.Cab_Number

class Cab_History(models.Model):
    Driver_ID = models.ForeignKey(Driver, on_delete=models.DO_NOTHING)
    Cab_Number=models.ForeignKey(Cab, on_delete=models.DO_NOTHING)


class Payment_History(models.Model):
    RFID = models.ForeignKey(Student, on_delete=models.CASCADE)
    Payment = models.IntegerField()


class Travel_History(models.Model):
    RFID = models.ForeignKey(Student, on_delete=models.CASCADE)
    Driver_ID = models.ForeignKey(Driver, on_delete=models.DO_NOTHING)
    Cab_Number = models.ForeignKey(Cab, on_delete=models.DO_NOTHING)
    Date = models.DateTimeField()
