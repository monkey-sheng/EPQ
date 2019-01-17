from django.urls import path

from . import views,retro8bits

urlpatterns = [
    path('',views.home,name='home'),
    path('display_result/',views.upload_file,name='upload_file'),
    #path('result/',views.)
    path('result_img/',retro8bits.img_return,name='result')
]
