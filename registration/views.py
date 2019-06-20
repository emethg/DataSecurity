from django.shortcuts import render, HttpResponse, redirect
import requests
from .forms import RegisterForm, LoginForm, SetBloodForm, SetUrineForm, SetDiabeteForm
from .auth import log_in, reg
from .encrypt import encryptWord, encryptPassword, CheckPassword, decryptWord
from .getpost import setblood, getblood, seturine, geturine, getdiabete, setdiabete, getid
from django.contrib.auth import authenticate



def index_view(request):
    return render(request, 'html/index.html', {})

def register_view(request):
    if request.method == 'GET':
        form = RegisterForm()
        args = {'form' : form}
        return render(request, 'html/register.html', args)
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if(form.is_valid()):
            response = reg(request, form)
            return render(request, 'html/login.html', {})
        else:
            return HttpResponse("form is not valid")


def signin_view(request):
    if not request.session.has_key('id'):
        if request.method == 'GET':
            form = LoginForm()
            args = {'form': form}
            return render(request, 'html/login.html', args)
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if(form.is_valid()):
                red = log_in(request, form.data['RID'], form.data['RPassword'])
                if red:
                    if request.session['type'] == '0':
                        return redirect(select_view)
                    else:
                        return redirect(set_view)
                else:
                    return HttpResponse("failed to connect")
            return HttpResponse("The form is not valid")
    else:
        return redirect(index_view)
            

def formView(request):
    if request.session.has_key('id'):
        id = request.session['id']
        return HttpResponse("Your are logged in for session : {}".format(id))
    else:
        return render(request, 'html/login.html', {})
    
def logout_view(request):
    if request.session.has_key('log'):
        try:
            del request.session['id']
        except:
            pass
        try:
            del request.session['pwd']
        except:
            pass
        try:
            del request.session['log']
        except:
            pass
        try:
            del request.session['type']
        except:
            pass
        return redirect('/')
    else:
        return HttpResponse('You can not acces this page, you are already logged in')
        

def data_pass(request, id):
    return HttpResponse("return data pass info")

def test_session_id(request):
    return HttpResponse(request.session.session_key)

def setblood_view(request):
    if request.session.has_key('type'):
        if request.session['type'] == '1':
            if request.method == 'GET':
                form = SetBloodForm()
                datacrypt = getid(request)
                datadecrypt = []
                form.fields['RID'].choices = datacrypt
                args = {'form' : form}
                return render(request, 'html/setblood.html', args)
            if request.method == 'POST':
                form = SetBloodForm(request.POST)
                if(form.is_valid()):
                    response = setblood(request, form)
                    return HttpResponse(response['status'])
                return HttpResponse('Post information failed')
        else:
            return redirect(index_view)
    else:
        return redirect(index_view)

def getblood_view(request):
    response = getblood(request)
    if response:
        new_response = []
        for x in response:
            print(x)
            for k, v in x.items():
                if k == 'DateOfDemand':
                    pass
                else:
                    x[k] = decryptWord(v)
            new_response.append(x)
        args = {'data' : new_response}
    else:
        args = {'data' : response}
    return render(request, 'html/getblood.html', args)

def seturine_view(request):
    if request.session.has_key('type'):
        if request.session['type'] == '1':
            if request.method == 'GET':
                form = SetUrineForm()
                
                datacrypt = getid(request)
                form.fields['RID'].choices = datacrypt
                datadecrypt = []
            
                args = {'form' : form}
                return render(request, 'html/seturine.html', args)
            if request.method == 'POST':
                form = SetUrineForm(request.POST)
                if(form.is_valid()):
                    response = seturine(request, form)
                    return HttpResponse(response['status'])
                return HttpResponse('Post information failed')
        else:
            return redirect(index_view)
    else:
        return redirect(index_view)


def geturine_view(request):
    response = geturine(request)
    if response:
        new_response = []
        for x in response:
            print(x)
            for k, v in x.items():
                if k == 'DateOfDemand':
                    pass
                else:
                    x[k] = decryptWord(v)
            new_response.append(x)
        args = {'data' : new_response}
    else:
        args = {'data' : response}
    return render(request, 'html/geturine.html', args)

def setdiabete_view(request):
    if request.session.has_key('type'):
        if request.session['type'] == '1':
            if request.method == 'GET':
                form = SetDiabeteForm()
                choice=getid(request)
                datacrypt = getid(request)
                datadecrypt = []
                for id in datacrypt:
                    datadecrypt.append(decryptWord(id))
                args = {'form' : form, 'data' : datadecrypt}
                return render(request, 'html/setdiabete.html', args)
            if request.method == 'POST':
                form = SetDiabeteForm(request.POST)
                if(form.is_valid()):
                    response = setdiabete(request, form)
                    return HttpResponse(response['status'])
                return HttpResponse('Post information failed')
        else:
            return redirect(index_view)
    else:
        return redirect(index_view)

def getdiabete_view(request):
    response = getdiabete(request)
    if response:
        new_response = []
        for x in response:
            print(x)
            for k, v in x.items():
                if k == 'DateOfDemand':
                    pass
                else:
                    x[k] = decryptWord(v)
            new_response.append(x)
        args = {'data' : new_response}
    else:
        args = {'data' : response}
    return render(request, 'html/getblood.html', args)

def index2_view(request):
    return render(request, 'html/index2.html', {})

def select_view(request):
    if request.session['type'] == '0':
        return render(request, 'html/select.html', {})
    else:
        return redirect(index_view)   

def set_view(request):
    if request.session['type'] == '1':
        return render(request, 'html/set.html', {})
    else:
        return redirect(index_view)
