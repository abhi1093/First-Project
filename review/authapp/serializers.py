from rest_framework import serializers
from authapp.models import PostImage


class IMAGEPostSerailizer(serializers.ModelSerializer):
    class Meta:
        model =PostImage
        fields = '__all__'