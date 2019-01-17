from os import getcwd
from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect as redirect
from . import evaluate
# Create your views here.

available_style={'child_of_light':'child_of_light.ckpt','wave':'wave.ckpt','la_muse':'la_muse.ckpt',
                     'monalisa':'monalisa.ckpt','starry_night':'starry_night.ckpt'}

class UploadFileForm(forms.Form):
    img = forms.ImageField()

def home(request):
    return render(request,'style_transfer/home.html')


def HomeOfStyles(request,style_name):  # homepage for each style transfer
    try:
        available_style[style_name]
    except:
        return redirect('/style_transfer/')

    if not request.session.session_key:
        request.session.create()
        request.session.set_expiry(600)
    return render(request,'style_transfer/'+str(style_name)+'.html')


def proc(request,style_name):  # style_name should come from the url display_result/<str:style_name>

    cwd=getcwd()
    # stores the style_name and checkpoint name(should be like /.../checkpoint.ckpt) mapping

    try:
        available_style[style_name]
    except:
        return redirect('/style_transfer/')
    #  no such style transfer page, go back to home page

    if not request.session.session_key:
        return render(request,'generic/no_active_session.html')
    if request.method == 'POST':
        try:
            evaluate.img_dict[request.session.session_key]
            return render(request, 'generic/one_img_display.html', {'url': '/style_transfer/result_img/',
                                                                    style_name: 'active'})
        except:
            pass
        form = UploadFileForm(request.POST,request.FILES)
        if form.is_valid():
            evaluate.evaluate(request,request.FILES['img'],cwd+'/style_transfer/checkpoint_models/'+available_style[style_name])
            return render(request,'generic/one_img_display.html',{'url':'/style_transfer/result_img/',
                                                                  style_name:'active'})
    return redirect('/style_transfer/')

def img_return(request,download=None):
    from .evaluate import img_dict
    session_key=request.session.session_key
    if not session_key:
        return render(request,'generic/no_active_session.html') # no active session
    try:
        response = img_dict[session_key]
    except:
        return redirect('/style_transfer/')
    if not download:
        return response
    else:
        response['Content-Disposition'] = 'attachment; filename="result.png"'
        return response