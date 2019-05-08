"""practica_project URL Configuration

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
from rest_framework import routers
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import TemplateView
from catalog import views
from catalog.views import likes
from exemple.views import article,articles, addlike,addcomment
from loginsys.views import login, logout

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet, base_name='users')
router.register(r'groups', views.GroupViewSet, base_name='groups')

admin.autodiscover(),


urlpatterns = [
    path('admin/', admin.site.urls),
# REST API
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('accounts/', include('django.contrib.auth.urls')),
#---------------------------------------------------------------

#EXEMPLE
    path('exemple/', articles),
    path('articles/all/', articles),
    path('articles/get/<int:article_id>/', article),
    path('articles/addlike/<int:article_id>/', addlike),
    path('articles/addcomment/<int:article_id>/', addcomment),

#-------------------------------------------------------------------

#LIGINSYS
    path('auth/login/',login),
    path('auth/logout/',logout),
#-----------------
]
#     path('home/', TemplateView.as_view(template_name='home.html'), name='home'),
#     path('like/',likes,name = 'like'),
#     path('', views.allblogs , name='allblogs'),
#     path('<int:blog_id>/', views.detail, name="detail"),
# ]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)