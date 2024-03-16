from django.contrib import admin
from django.urls import path
from home.views import URLShortenView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', URLShortenView.as_view())
]
