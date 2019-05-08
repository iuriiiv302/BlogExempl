from django.shortcuts import render

from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from django.template.context_processors import csrf

def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('http://127.0.0.1:8000/articles/all/')
        else:
            args["login_error"] = "User is not found"
            return render_to_response('login.html',args)
    else:
        return render_to_response('login.html',args)
def logout(request):
    auth.logout(request)
    return redirect('http://127.0.0.1:8000/articles/all/')
