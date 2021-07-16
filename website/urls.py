from django.urls import path
from .views import home,detail,nepse

urlpatterns = [
    path('', home, name='home'),
    path('blog/<slug>',detail,name='detail'),
    path('nepse/',nepse,name='nepse')
]
