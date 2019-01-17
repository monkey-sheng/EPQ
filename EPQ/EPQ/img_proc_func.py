from django.http import HttpResponse
from django.shortcuts import render
from PIL import Image


img_dict = {}

def img_proc(request,img,size):
    session_key=request.session.session_key
    img_dict[session_key]=[]  # create a list to store the img for this session
    size=int(size)
    img=Image.open(img)
    length = size
    width = size
    img1=img.resize((width,length))
    img_dict[session_key].append(img1)
    img2=img.resize((2*width,2*length))
    img_dict[session_key].append(img2)


def img_return(request,img_id): #except is to handle the case of direct access
    try:
        session_key=request.session.session_key
        if session_key is None:
            raise ValueError  # in case session_key is messed up and img results cannot be fetched using it

        img_list=img_dict[session_key]  # get the list of img from the dict for this session
        img_id=int(img_id)
        response=HttpResponse(content_type='img/png')
        img_list[img_id-1].save(response,'png')  # img_id starts from 1 for better url understanding
        return response
    except IndexError:
        return render(request,'testproject/error_page.html')
    except ValueError:
        return HttpResponse("Session error: no active session")
