from rest_framework import serializers

from news.models import NewsModel


class NewsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsModel
        fields = ['id', 'title', 'content', 'created_at']
