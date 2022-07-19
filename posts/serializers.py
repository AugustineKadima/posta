from pickle import FALSE
from rest_framework import serializers
from .models import *


class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title =serializers.CharField(required=True, allow_blank=FALSE, max_length=30)
    content =serializers.CharField(style={"base_template" : "textarea.html"})
    author =serializers.CharField(required=True, allow_blank=FALSE, max_length=30)

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.content = validated_data.get("content", instance.content)
        instance.author = validated_data.get("author", instance.author)
        instance.save()
        return instance
