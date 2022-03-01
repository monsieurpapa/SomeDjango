
from django.shortcuts import render
from .models import Film


def home(request):
    return render(request, 'home.html')


def main(request):
    title = 'Main Page'
    films_list = Film.objects.all()
    context = {'title':title,
                'films_list':films_list
    }
    return render(request,
                  'films/main.html',context)


def user_info(request):
    # userinfo = {
    #     'username': 'Fabrício', # Put your name here
    #     'country': 'Brazil', # Put your country here
    # }
    # context = {'userinfo': userinfo,
    #            'title': 'User Info Page'}
    
    # return render(request,
    #               'films/user_info.html',
    #               context)
    if request.method == 'GET':
        # remove this print later
        print('\n\nrequest.GET ==>>',
              request.GET,
              '\n\n')
    
        userinfo = {
            'username': request.GET.get('username'),
            'country': request.GET.get('country'),
        }
        context = {'userinfo': userinfo,
                   'title': 'User Info Page'}
        template = 'films/user_info.html'
        return render(request,
                      template,
                      context)
    # elif request.method == 'POST':
    #     return HttpResponse('POST request here.')