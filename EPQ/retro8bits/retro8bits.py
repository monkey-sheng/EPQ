from django.http import HttpResponse
from django.shortcuts import render
img_dict={}


def resize(img,zoom):
    length = img.size[0]
    width = img.size[1]
    img=img.resize((int(length*float(zoom)),int(width*float(zoom))))
    return img


def to_8bit(request,img):
    from PIL import Image, ImageOps
    session_key=request.session.session_key
    img = Image.open(img)
    img = resize(img, 0.1)
    img = ImageOps.posterize(img, 3)
    retro_img = resize(img, 10)
    img_dict[session_key]=retro_img


def img_return(request):
    try:
        session_key=request.session.session_key
        if session_key is None:
            raise ValueError  # in case session_key is messed up and img results cannot be fetched using it
        img=img_dict[session_key]
        response=HttpResponse(content_type='img/png')
        img.save(response,'png')
        return response
    except ValueError:
        return render(request,'retro8bits/no_active_session.html')