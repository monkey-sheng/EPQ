from django.shortcuts import render
from django import forms
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
# DON'T USE reverse() UNLESS ALL OTHERS FAILED!! EASILY CAUSES URL NO MATCH EXCEPTION

# class UploadFileForm(forms.Form):
#     img = forms.ImageField()
#     size=forms.DecimalField(max_value=999)


def home(request):
    return render(request,"EPQ/home.html")

# def upload_file(request):
#     request.session.set_expiry(0)  # session expires after browser closes
#     if not request.session.session_key:
#         request.session.create()
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             img_proc(request,request.FILES['img'],request.POST['size']) # dict key is the same as in html
#             return render(request,'EPQ/img.html',{'url1':'/get_result/1/',
#                                               'url2':'/get_result/2/'})

# get_results/1/ would pend it after the current url, but /get_results/1/ would make it
# 127.0.0.1/get_results/1/

# DON'T USE request.session TO STORE TEMP IMG
#
# def upload_file(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             img_proc(request,request.FILES['img'],request.POST['size'])
#             return HttpResponse(request.session['img_response'])
#     else:
#         form = UploadFileForm()
#     return render(request, 'upload.html', {'form': form})