from rest_framework import serializers
from .models import sale_upload

class sale_uploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = sale_upload
        fields = ('id',
                  'createdate',
                  'salesname',
                  'amount',
                  'imageurl',
                  'checkif',
                  )