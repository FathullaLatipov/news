from rest_framework.generics import ListAPIView, RetrieveAPIView

from api.serializers import NewsModelSerializer
from news.models import NewsModel




class NewsListAPIView(ListAPIView):
    serializer_class = NewsModelSerializer
    queryset = NewsModel.objects.order_by('-pk')


class NewsRetrieveAPIView(RetrieveAPIView):
    serializer_class = NewsModelSerializer
    queryset = NewsModel.objects.all()
