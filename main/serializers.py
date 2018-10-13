from rest_framework import serializers
from .models import Student
from .models import Cab
from .models import Driver
from .models import Cab_History
from .models import Travel_History



class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('Name', 'Registration_Number', 'Email', 'Balance')



class CabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cab
        fields = '__all__'


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'


class Cab_HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Cab_History
        fields = '__all__'


class Travel_HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Travel_History
        fields = '__all__'



