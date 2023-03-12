from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from . import models, serializers, parse
# Create your views here.
class ResourceViewSet(ModelViewSet):
    queryset = models.Resource.objects.all()
    serializer_class = serializers.ResourceSerializer


def parse_news_view(request):
    all_news = parse.parse_news()
    serialized_news = []

    for news_item in all_news:
        serializer = serializers.ItemSerializer(news_item)
        serialized_news.append(serializer.data)

    return JsonResponse(serialized_news, safe=False)