from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ShortURL
from .serializers import ShortURLSerializer
import random
import string

class ShortURLView(APIView):
    def post(self, request):
        data = request.data.copy()

        if not data.get('shortcode'):
            data['shortcode'] = ''.join(random.choices(string.ascii_letters + string.digits, k=6))

        serializer = ShortURLSerializer(data=data, context={'request': request})
        if serializer.is_valid():
            shorturl = serializer.save()
            response_data = ShortURLSerializer(shorturl, context={'request': request}).data
            return Response(response_data, status=201)
        return Response(serializer.errors, status=400)

