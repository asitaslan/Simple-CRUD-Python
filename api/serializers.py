from rest_framework import serializers

from api.models import Practice


class PracticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Practice
        fields = ('id','title','problem','point','level','language','input','expected_output')

