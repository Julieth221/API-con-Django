from rest_framework import serializers
from .models import programmer, student

class ProgrammerSerializer(serializers.ModelSerializer):
    class Meta:
        model = programmer
        # fields = ('fulll_name',  'nickname', 'age')
        fields = '__all__'
        
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = '__all__'