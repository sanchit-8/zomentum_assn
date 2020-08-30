from rest_framework import serializers
from .models import ticket

class ticketSerializer(serializers.HyperlinkedModelSerializer):

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance


    class Meta:
        model = ticket
        fields = ['id', 'UserName', 'PhoneNo','timing','is_expired', 'booking_time']

