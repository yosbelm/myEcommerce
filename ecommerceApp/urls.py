from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.productItem, name='login'),
    path('cart', views.cart, name='cart'),
    path('signin', views.signin, name='signin'),
    path('signup', views.create_user, name='signup'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)