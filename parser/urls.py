from django.urls import path, include
from rest_framework import routers

from parser.views import ResourceViewSet, parse_news_view

router = routers.DefaultRouter()
router.register(r'resources', ResourceViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('news', parse_news_view),
]