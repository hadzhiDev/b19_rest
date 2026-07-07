from rest_framework import serializers

from .models import Apartment, Block


class ApartmentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = "__all__"


class ApartmentSerializer(serializers.Serializer):
    number = serializers.IntegerField()
    area = serializers.FloatField()
    floor = serializers.IntegerField()
    rooms_count = serializers.IntegerField()
    deadline = serializers.DateField()
    type = serializers.ChoiceField(choices=Apartment.TYPE_CHOICES)
    block = serializers.PrimaryKeyRelatedField(queryset=Block.objects.all())

    def create(self, validated_data):
        print(validated_data)
        return Apartment.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.number = validated_data.get('number', instance.number)
        instance.area = validated_data.get('area', instance.area)
        instance.floor = validated_data.get('floor', instance.floor)
        instance.rooms_count = validated_data.get('rooms_count', instance.rooms_count)
        instance.deadline = validated_data.get('deadline', instance.deadline)
        instance.type = validated_data.get('type', instance.type)
        instance.block = validated_data.get('block', instance.block)
        instance.save()
        return instance


# class LoginSerializer(serializers.Serializer):
#     phone_number = serializers.CharField()
#     password = serializers.CharField()


