
from django.shortcuts import render,redirect
from django.urls import reverse
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


    def user_form(request):
        if request.method == 'GET':
            context = {'title': 'User Form Page'}
            template = 'films/user_form.html'

            return render(request,
                        template,
                        context)
            
        elif request.method == 'POST':
            # it is good practice to send the data from a POST request to a different URL than the one where the form is located
            #save the data passed in the form  for every input field
            username = request.POST.get('username')
            country = request.POST.get('country')
            '''Then we can pass these values to another dictionary located in request.session, which is extremely helpful. It allows data to be stored in 
            the current browser session and be retrieved in different moments by our code'''
            request.session['username'] = username
            request.session['country'] = country

            return redirect(reverse('films:user_info'))
    
    def details(request, id):
        film = Film.objects.get(id=id)
        # other query option:
        # film = Film.objects.filter(id=id)[0] #can also be used to query for just a single element by id
        context = {'film': film}
        return render(request, 'films/details.html', context)