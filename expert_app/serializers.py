from .models import *
from rest_framework import serializers

class MediaSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Media
        fields = [
            'id',
            'file',
            'created_at',
            'deleted_at',
            'updated_at'
        ]