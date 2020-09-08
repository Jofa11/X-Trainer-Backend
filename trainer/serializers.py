from rest_framework import serializers
from .models import Exercise, User


class ExerciseSerializer(serializers.ModelSerializer):

    exercise_url = serializers.ModelSerializer.serializer_url_field(
        view_name='exercise_detail'
    )

    class Meta:
        model = Exercise
        fields = ('id', 'name', 'description', 'photo_url', 'exercise_url')


class UserSerializer(serializers.ModelSerializer):

    user_url = serializers.ModelSerializer.serializer_url_field(
        view_name='user_detail'
    )

    class Meta:
        model = User
        fields = ('id', 'name', 'user_url')
