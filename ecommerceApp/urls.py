from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.productItem, name='products'),
    path('carr', views.cart, name='carr'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.create_user, name='signup'),
    path('dlete_item/<int:id>', views.delete_item, name='dlete_item'),
    path('updateitem', views.updateItem, name='updateitem'),
    path('checkout', views.checkout, name='checkout'),
    path('details/<int:id>/', views.details, name='details'),
    path('home', views.home, name='home'),
    path('logout', views.signout, name='logout'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)