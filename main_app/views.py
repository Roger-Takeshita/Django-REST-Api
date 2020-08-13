from django.http import HttpResponse, JsonResponse
from .models import *      #+ Import all models
from .serializers import * #+ Import all serializers

from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView

# = FUNCTION BASE VIEW
@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, article_id):
    try:
        article = Article.objects.get(pk=article_id)
    except Article.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# = CLASS BASE VIEW
class IndexAPIView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

class ArticleAPIView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ArticleSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArticleDetailsAPIView(APIView):
    def get_object(self, article_id):
        try:
            return Article.objects.get(id=article_id)
        except Article.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, article_id):
        article = self.get_object(article_id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def put(self, request, article_id):
        article = self.get_object(article_id)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, article_id):
        article = self.get_object(article_id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)