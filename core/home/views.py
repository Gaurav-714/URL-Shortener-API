from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from .models import URL
from .serializers import URLSerializer
import pyshorteners
#import hashlib

class URLShortenView(generics.CreateAPIView):

    serializer_class = URLSerializer
    
    def post(self, request):
        url = request.data.get('url')
        if not url:
            return Response({
                "status" : status.HTTP_400_BAD_REQUEST,
                "error" : "please provide a url"
            })
        
        # Generate short URL using pyshorteners
        shortener = pyshorteners.Shortener()
        short_url = shortener.tinyurl.short(url)

        # Shorten URL using hashlib
        #hash_object = hashlib.md5(original_url.encode())
        #short_url = hash_object.hexdigest()[:8]
        
        # Save to database
        url_object, created = URL.objects.get_or_create(url=url, defaults={'short_url':short_url})

        serializer = self.get_serializer(url_object)

        return Response({
            "status" : status.HTTP_201_CREATED,
            "message" : "URL is Shortened",
            "data" : serializer.data
        })