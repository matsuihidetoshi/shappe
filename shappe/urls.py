"""shappe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
"""Commented out for graphql
from django.contrib import admin
from django.urls import path, include

from restapi.urls import router as restapi_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(restapi_router.urls)),
]
"""

from django.conf.urls import include, url
from django.contrib import admin
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    url(r'^graphql', csrf_exempt(GraphQLView.as_view(graphiql=True))),  # <- graphql_sample
    url(r'^admin/', admin.site.urls),
]