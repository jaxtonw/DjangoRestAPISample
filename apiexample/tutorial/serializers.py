from rest_framework import serializers
from tutorial.models import Tutorial

class TutorialSerializer(serializers.ModelSerializer):
    # TODO: Fix serializers
    class Meta:
        model = Tutorial
        fields = (
            'id',
            'title',
            'description',
            'published',
            )
