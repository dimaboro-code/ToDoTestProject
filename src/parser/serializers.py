from rest_framework import serializers
from .models import TechParkCompany


class TechParkCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = TechParkCompany
        fields = "__all__"
