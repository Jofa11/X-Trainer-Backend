from rest_framework import serializers
from .models import Exercise
from django.contrib.auth.models import User


class ExerciseSerializer(serializers.ModelSerializer):

    exercise_url = serializers.ModelSerializer.serializer_url_field(
        view_name='exercise_detail'
    )

    class Meta:
        model = Exercise
        fields = ('id', 'name', 'description', 'photo_url', 'exercise_url')


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    email = serializers.CharField(write_only=True)
    username = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'password')

    def create(self, validated_data):

        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        user = User(email=email, username=username)
        # Sets the user’s password to the given raw string,
        # taking care of the password hashing. Doesn’t save the User object.

        user.set_password(password)

        # save() method to save the user object
        user.save()

        return user
