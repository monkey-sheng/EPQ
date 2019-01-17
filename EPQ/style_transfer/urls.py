from django.urls import path

from . import views

urlpatterns = [
    path('result_img/', views.img_return),
    path('',views.home,name='home'),
    path('<str:style_name>/',views.HomeOfStyles),
    path('<str:style_name>/proc/',views.proc),
    path('result_img/<str:download>/',views.img_return)
]

# ALERT - MIGHT BE A BUG
# WHEN path('result_img/') is not at the first position (possibly other positions as well) in urlpatterns,
# even if it is commented out, an automatic url redirect 302 occurs and redirects to /style_transfer/
