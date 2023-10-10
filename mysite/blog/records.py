from django.contrib import admin

from models import Post

Post.published.filter(tittle_start_with='Who')
