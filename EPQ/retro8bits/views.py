from django.shortcuts import render
from . import retro8bits
from django.http import HttpResponseRedirect as redirect
from django import forms# Create your views here.
class UploadFileForm(forms.Form):
    img = forms.ImageField()

def home(request):
    request.session.create()
    request.session.set_expiry(0)
    return render(request,"retro8bits/home.html")

def upload_file(request):
    if not request.session.session_key:
        return render(request,'retro8bits/no_active_session.html')
    if request.method == 'POST':
        form = UploadFileForm(request.POST,request.FILES)
        if form.is_valid():
            retro8bits.to_8bit(request, request.FILES['img'])
            return render(request, 'retro8bits/display.html', {'url': 'result_img/'})
    return redirect('/retro8bits/')

# def display_result(request):
#     if not request.session.session_key:
#         render(request,'retro8bits/no_active_session.html')
#     else:
#         render(request,'retro8bits/display.html')