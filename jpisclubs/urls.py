
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from signin import views as viewsignin
from jpisclubs import common
from django.conf.urls.static import static
urlpatterns = [
    path('',include('signin.urls')),
    path('',include('dashboard.urls'),name='dashboard'),
    path('admin/', admin.site.urls),
]+ static(common.MEDIA_URL,document_root=common.MEDIA_ROOT)
