
from django.urls import path,include
from . import views
urlpatterns = {
    path('',views.hello,name='hello'),
    path('hello',include('greet.urls'))
}

# the main 