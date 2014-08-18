# -*- coding: utf-8 -*- 
from django.shortcuts import render

# Create your views here.


from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from models import *
from django.template import loader, RequestContext
from django.views.decorators.csrf import csrf_protect,csrf_exempt
from datetime import datetime
from django.db import transaction
from django.utils import simplejson
import base64

from datetime import datetime

def talk(request):
    #post to get !
    res = {}
    nick  = request.POST.get('nick','')
    message = request.POST.get('message','')
    if nick == '' or message  == '':
        res['1']='失败了。。。'
        return HttpResponse(simplejson.dumps(res, ensure_ascii=False)) 
    
   
    #try to save...
    try:
        pos = request.POST.get('pos','')
        lan = request.POST.get('lan','')
        lon = request.POST.get('lon','')
        if pos == '':
            mes = TalkMessage(nick = nick, message = message, create_at = datetime.now(),status = 1,pos='',lat= 0.0,lon = 0.0)
            mes.save()
        else:
            mes = TalkMessage(nick = nick, message = message, create_at = datetime.now(),status = 1,pos= pos,lat=lan,lon=lon)
            mes.save()
    except:
        print 'error'
        res['3']='create failed'
        return HttpResponse(simplejson.dumps(res, ensure_ascii=False)) 
    
    res['0']='ok'
    return HttpResponse(simplejson.dumps(res, ensure_ascii=False)) 




def show(request):
    #post to get !
    res={}
    l1 = TalkMessage.objects.filter(status = 1).order_by('-create_at')
    outl=[]
    
    for i in l1:
        
        outl.append({'id':i.id,'nick':i.nick,'message':i.message,'time':i.create_at.strftime('%Y-%m-%d %H:%M'),'pos':i.pos,
                     'lat':str(i.lat),'lon':str(i.lon)})
    
    res['0']= outl
    return HttpResponse(simplejson.dumps(res, ensure_ascii=False)) 

def delete(request):
    
    res={}
    
    itemid = request.POST.get('itemid','')
    if itemid == '':
        res['1'] = '操作失败'
        return HttpResponse(simplejson.dumps(res, ensure_ascii=False)) 
    try:
        item = TalkMessage.objects.get(id = itemid)
        item.status = False

        item.save()
        res['0'] = '操作成功'
        return HttpResponse(simplejson.dumps(res, ensure_ascii=False)) 
    except:
        pass
        res['1'] = '操作失败'
        return HttpResponse(simplejson.dumps(res, ensure_ascii=False)) 
    
        
    
    
    #return HttpResponse(simplejson.dumps(res, ensure_ascii=False)) 

    