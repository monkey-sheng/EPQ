from django.urls import path
from . import views,retro8bits

urlpatterns = [
    path('',views.home,name='home'),
    path('contrast/',views.Contrast),
    path('contrast/proc/',views.ContrastProc),
    path('contrast/result_img/',views.ContrastResult),
    path('contrast/result_img/<str:download>/',views.ContrastResult),
    path('retro8bits/',views.retro8bits),
    path('retro8bits/proc/',views.retro8bitsProc),
    path('retro8bits/result_img/',views.retro8bitsResult),
    path('retro8bits/result_img/<str:download>/',views.retro8bitsResult),
    path('brightness/',views.Brightness),
    path('brightness/proc/',views.BrightnessProc),
    path('brightness/result_img/',views.BrightnessResult),
    path('brightness/result_img/<str:download>/',views.BrightnessResult),
    path('sharpness/',views.Sharpness),
    path('sharpness/proc/',views.SharpnessProc),
    path('sharpness/result_img/',views.SharpnessResult),
    path('sharpness/result_img/<str:download>/',views.SharpnessResult),
    path('color_balance/',views.ColorBalance),
    path('color_balance/proc/',views.ColorBalanceProc),
    path('color_balance/result_img/',views.ColorBalanceResult),
    path('color_balance/result_img/<str:download>/',views.ColorBalanceResult),
    path('aspect_ratio/',views.AspectRatio),
    path('aspect_ratio/proc/',views.AspectRatioProc),
    path('aspect_ratio/result_img/',views.AspectRatioResult),
    path('aspect_ratio/result_img/<str:download>/',views.AspectRatioResult)
]