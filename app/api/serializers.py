from rest_framework import serializers
from .models import WildfireReport


class WildfireReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = WildfireReport
        fields = '__all__'
