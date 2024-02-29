from rest_framework import serializers
from api.models import Words

class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Words
        fields = '__all__'


