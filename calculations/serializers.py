from rest_framework import serializers
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import BillShare


# class BillShareSerializer(serializers.ModelSerializer):
class BillShareSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    member = serializers.IntegerField()
    apartment = serializers.IntegerField()
    share_percentage = serializers.DecimalField(max_digits=5, decimal_places=2,validators=[MinValueValidator(0), MaxValueValidator(100)])
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    # model = BillShare
    # fields = ['id', 'member', 'apartment', 'share_percentage', 'created_at', 'updated_at']

    # fields = '__all__'
    def create(self, validated_data):
        """
        Create and return a new BillShare instance given the validate data
        """
        return BillShare.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `BillShare` instance, given the validated data.
        """

        instance.member = validated_data.get('member', instance.member)
        instance.apartment = validated_data.get('apartment', instance.apartment)
        instance.share_percentage = validated_data.get('share_percentage', instance.share_percentage)
        instance.save()
        return instance
    