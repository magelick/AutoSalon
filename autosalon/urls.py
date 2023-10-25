"""
URL configuration for autosalon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .views import NotFoundTemplateView
# Обрабатываем 404 ошибку
handler = NotFoundTemplateView.as_view()
# Найстраиваем пути к остальным приложениям
urlpatterns = [
    path('admin/', admin.site.urls),  # Путь к админ-панели
    path('api/', include('api.urls')),  # Путь к API
    path('', include('shop.urls')),  # Путь к основным страницам сайта
    path('search/', include('transport.urls')),  # Путь к данным о транспорте
    path('users/', include('users.urls')),  # Путь к даным о пользователях
]
if settings.DEBUG:  # Если нахожимся в DEBUG-режиме, подключаем static-файлы
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
