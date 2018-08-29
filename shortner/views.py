from django.shortcuts import render
from django.http import JsonResponse,HttpResponseRedirect
from .utilities import gen
from .models import Link

# Create your views here.

def home(request):
    return render(request, 'shortner/master.html')


def makeurl(request):
    url = request.GET.get('url','')
    if url=='': return JsonResponse({'error':"BAD URL GIVEN"})
    if not url.startswith('http'): url = 'http://'+url
    d = Link.objects.first().short
    d = gen(d)
    Link(short=d, original=url).save()
    d = "{}/{}".format(request.META['HTTP_HOST'], d)
    return JsonResponse({'success':True, 'url':d})

def redirect(request,url):
    try: rurl = Link.objects.get(short=url).original
    except: return JsonResponse({'error': 'We do not have any entry for this url'})
    return HttpResponseRedirect(rurl)
