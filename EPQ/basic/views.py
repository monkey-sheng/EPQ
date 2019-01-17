from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect as redirect
from django import forms

ContrastDict={}
retro_dict={}
BrightnessDict={}
SharpnessDict={}
ColorBalanceDict={}
AspectRatioDict={}

# Create your views here.
class ImageOnlyForm(forms.Form):
    img = forms.ImageField()


class ContrastForm(forms.Form):
    contrast = forms.DecimalField(max_value=99,min_value=1)
    img=forms.ImageField()

class BrightnessForm(forms.Form):
    brightness=forms.FloatField(min_value=0.0,max_value=10.0)
    img=forms.ImageField()

class SharpnessForm(forms.Form):
    sharpness=forms.FloatField(min_value=-20.0,max_value=20.0)
    img=forms.ImageField()

class ColorBalanceForm(forms.Form):
    color_balance=forms.FloatField()
    img=forms.ImageField()


#  session should be created individually when each operation's page is accessed
def home(request):
    return render(request,'basic/home.html')

def Contrast(request):
    request.session.create()
    request.session.set_expiry(600)
    return render(request,'basic/contrast.html')

def ContrastProc(request):
    if request.method=='POST':
        form=ContrastForm(request.POST,request.FILES)

        if form.is_valid():
            contrast = int(request.POST['contrast']) / 2
            from PIL import Image, ImageOps
            img=Image.open(request.FILES['img'])
            new_img=ImageOps.autocontrast(img,contrast)
            response=HttpResponse(content_type='img/png')
            new_img.save(response,'png')
            ContrastDict[request.session.session_key]=response
            return render(request,'generic/one_img_display.html',{'url':'/basic/contrast/result_img/','contrast':'active'}) #  this is a generic template for showing 1 image
    return redirect('/basic/contrast/')


def ContrastResult(request,download=None):
    session_key=request.session.session_key
    if not session_key:
        return render(request,'generic/no_active_session.html')
    try:
        ContrastDict[session_key]
    except:
        return render(request, 'generic/no_active_session.html')
    if not download:
        return ContrastDict[session_key]
    else:  # for download purpose
        response=ContrastDict
        response[session_key]['Content-Disposition']='attachment; filename="result.png"'
        return response

def retro8bits(request):
    request.session.create()
    request.session.set_expiry(600)
    return render(request,"basic/retro8bits.html")


def retro8bitsProc(request):
    if not request.session.session_key:
        return render(request,'generic/no_active_session.html')
    if request.method == 'POST':
        form = ImageOnlyForm(request.POST,request.FILES)
        if form.is_valid():
            img=request.FILES['img']
            from PIL import Image, ImageOps
            session_key = request.session.session_key
            img = Image.open(img)
            length = img.size[0]
            width = img.size[1]
            img = img.resize((int(length * 0.1), int(width * 0.1)))
            img = ImageOps.posterize(img, 3)
            img = img.resize((int(img.size[0]*10),int(img.size[1]*10)))
            response=HttpResponse(content_type='img/png')
            img.save(response,'png')
            retro_dict[session_key] = response
            return render(request, 'generic/one_img_display.html',
                          {'url': '/basic/retro8bits/result_img/','retro8bits':'active'})
    return redirect('/retro8bits/')

def retro8bitsResult(request,download=None):
    session_key = request.session.session_key
    if not session_key:
        return render(request, 'generic/no_active_session.html')
    try:
        retro_dict[session_key]
    except:
        return render(request, 'generic/no_active_session.html')
    if not download:
        return retro_dict[session_key]
    else:  # for download purpose
        response=retro_dict[session_key]
        response['Content-Disposition'] = 'attachment; filename="result.png"'
        return response

def Brightness(request):
    request.session.create()
    request.session.set_expiry(600)
    return render(request, "basic/brightness.html")

def BrightnessProc(request):
    if not request.session.session_key:
        return render(request,'generic/no_active_session.html')
    if request.method == 'POST':
        form = BrightnessForm(request.POST,request.FILES)
        if form.is_valid():
            session_key = request.session.session_key
            from PIL import Image,ImageEnhance
            img=Image.open(request.FILES['img'])
            brightness=form.cleaned_data['brightness']
            img=ImageEnhance.Brightness(img).enhance(brightness)
            response=HttpResponse(content_type='img/png')
            img.save(response,'png')
            BrightnessDict[session_key]=response
            return render(request,'generic/one_img_display.html',
                          {'url':'/basic/brightness/result_img/','brightness':'active'})
    return redirect('/basic/brightness/')

def BrightnessResult(request,download=None):
    session_key = request.session.session_key
    if not session_key:
        return render(request, 'generic/no_active_session.html')
    try:
        BrightnessDict[session_key]
    except:
        return render(request, 'generic/no_active_session.html')
    if not download:
        return BrightnessDict[session_key]
    else:  # for download purpose
        response = BrightnessDict[session_key]
        response['Content-Disposition'] = 'attachment; filename="result.png"'
        return response

def Sharpness(request):
    request.session.create()
    request.session.set_expiry(600)
    return render(request, "basic/sharpness.html")

def SharpnessProc(request):
    if not request.session.session_key:
        return render(request,'generic/no_active_session.html')
    if request.method == 'POST':
        form = SharpnessForm(request.POST,request.FILES)
        if form.is_valid():
            session_key = request.session.session_key
            from PIL import Image, ImageEnhance
            img = Image.open(request.FILES['img'])
            sharpness=form.cleaned_data['sharpness']
            img=ImageEnhance.Sharpness(img).enhance(sharpness)
            response = HttpResponse(content_type='img/png')
            img.save(response, 'png')
            SharpnessDict[session_key] = response
            return render(request, 'generic/one_img_display.html',
                          {'url': '/basic/sharpness/result_img/', 'sharpness': 'active'})
    return redirect('/basic/sharpness/')

def SharpnessResult(request,download=None):
    session_key = request.session.session_key
    if not session_key:
        return render(request, 'generic/no_active_session.html')
    try:
        SharpnessDict[session_key]
    except:
        return render(request, 'generic/no_active_session.html')
    if not download:
        return SharpnessDict[session_key]
    else:  # for download purpose
        response = SharpnessDict[session_key]
        response['Content-Disposition'] = 'attachment; filename="result.png"'
        return response

def ColorBalance(request):
    request.session.create()
    request.session.set_expiry(600)
    return render(request, "basic/color_balance.html")

def ColorBalanceProc(request):
    if not request.session.session_key:
        return render(request,'generic/no_active_session.html')
    if request.method == 'POST':
        form = ColorBalanceForm(request.POST,request.FILES)
        if form.is_valid():
            session_key = request.session.session_key
            from PIL import Image, ImageEnhance
            img = Image.open(request.FILES['img'])
            color_balance=form.cleaned_data['color_balance']
            img=ImageEnhance.Color(img).enhance(color_balance)
            response = HttpResponse(content_type='img/png')
            img.save(response, 'png')
            ColorBalanceDict[session_key] = response
            return render(request, 'generic/one_img_display.html',
                          {'url': '/basic/color_balance/result_img/', 'color_balance': 'active'})
    return redirect('/basic/color_balance/')

def ColorBalanceResult(request,download=None):
    session_key = request.session.session_key
    if not session_key:
        return render(request, 'generic/no_active_session.html')
    try:
        ColorBalanceDict[session_key]
    except:
        return render(request, 'generic/no_active_session.html')
    if not download:
        return ColorBalanceDict[session_key]
    else:  # for download purpose
        response = ColorBalanceDict[session_key]
        response['Content-Disposition'] = 'attachment; filename="result.png"'
        return response

def _aspect_ratio(img,ar_h,ar_v):
    h = int(img.size[0])
    v = int(img.size[1])
    if ar_h < ar_v:
        h_new = int(v * ar_h / ar_v)
        img=img.crop(((h - h_new) / 2, 0, h - (h - h_new) / 2, v))
        return img
    else:
        v_new = int(h * ar_v / ar_h)
        img=img.crop((0, (v - v_new) / 2, h, v - (v - v_new) / 2))
        return img

def _resize(img,ar_h,ar_v):
    h = int(img.size[0])
    v = int(img.size[1])
    if ar_h < ar_v:
        new_h=v*ar_h/ar_v
        img=img.resize((new_h,v))
        return img
    else:
        new_v=h*ar_v/ar_h
        img=img.resize(h,new_v)
        return img

def AspectRatio(request):
    request.session.create()
    request.session.set_expiry(600)
    return render(request, "basic/aspect_ratio.html")

def AspectRatioProc(request):
    if not request.session.session_key:
        return render(request,'generic/no_active_session.html')
    session_key=request.session.session_key
    if request.method == 'POST':
        try:
            aspect_ratio_h=float(request.POST['aspect_ratio_h'])
            aspect_ratio_v=float(request.POST['aspect_ratio_v'])
        except:
            try:
                aspect_ratio=str(request.POST['aspect_ratio'])  # this is a str, split(':') and get a list containing 2 values
            except:
                return redirect('/basic/aspect_ratio/')
        type=str(request.POST['type'])
        from PIL import Image
        try:
            img=Image.open(request.FILES['img'])
        except:
            return redirect('/basic/aspect_ratio/')
        if type is None:
            return redirect('/basic/aspect_ratio/')

        try:
            if (aspect_ratio_h and aspect_ratio_v):  # entered custom aspect ratio value
                if type=='crop':
                    img=_aspect_ratio(img,aspect_ratio_h,aspect_ratio_v)
                    response=HttpResponse(content_type='img/png')
                    img.save(response,'png')
                    AspectRatioDict[session_key]=response
                else:
                    img=_resize(img,aspect_ratio_h,aspect_ratio_v)
                    response = HttpResponse(content_type='img/png')
                    img.save(response, 'png')
                    AspectRatioDict[session_key] = response
                return render(request, 'generic/one_img_display.html', {'url': '/basic/aspect_ratio/result_img/',
                                                                        'aspect_ratio': 'active'})
            return redirect('/basic/aspect_ratio/')
        except:
            try:
                if aspect_ratio:  # split and get values
                    val_list=aspect_ratio.split(':')
                    aspect_ratio_h=float(val_list[0])
                    aspect_ratio_v=float(val_list[1])
                    if (aspect_ratio_h and aspect_ratio_v):  # entered custom aspect ratio value
                        if type == 'crop':
                            img = _aspect_ratio(img, aspect_ratio_h, aspect_ratio_v)
                            response = HttpResponse(content_type='img/png')
                            img.save(response, 'png')
                            AspectRatioDict[session_key] = response
                        else:
                            img = _resize(img, aspect_ratio_h, aspect_ratio_v)
                            response = HttpResponse(content_type='img/png')
                            img.save(response, 'png')
                            AspectRatioDict[session_key] = response
                    return render(request,'generic/one_img_display.html',{'url':'/basic/aspect_ratio/result_img/',
                                                                      'aspect_ratio':'active'})
            except:
                return redirect('/basic/aspect_ratio/')

def AspectRatioResult(request,download=None):
    session_key = request.session.session_key
    if not session_key:
        return render(request, 'generic/no_active_session.html')
    try:
        AspectRatioDict[session_key]
    except:
        return render(request, 'generic/no_active_session.html')
    if not download:
        return AspectRatioDict[session_key]
    else:  # for download purpose
        response = AspectRatioDict[session_key]
        response['Content-Disposition'] = 'attachment; filename="result.png"'
        return response
