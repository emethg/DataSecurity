import requests
import json
from .forms import RegisterForm, LoginForm
import os


def encryptWord(request):
    DB_KEY = os.environ.get('DB_KEY_DS')
    url = 'http://securedata.rubnet.fr/sercureApi/encrypVar'
    payload = 'word=' + request
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'x-api-key': DB_KEY
    }
    response = requests.request('POST', url, headers = headers, data = payload, allow_redirects=False).json()
    encryption = response['value']
    return encryption


def decryptWord(request):
    DB_KEY = os.environ.get('DB_KEY_DS')
    url = 'http://securedata.rubnet.fr/sercureApi/decrypVar'
    payload = 'word=' + request
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'x-api-key': DB_KEY
    }
    response = requests.request('POST', url, headers = headers, data = payload, allow_redirects=False).json()
    decryption = response['value']
    return decryption


def encryptPassword(request):
    DB_KEY = os.environ.get('DB_KEY_DS')
    url = 'http://securedata.rubnet.fr/sercureApi/encrypPassword'
    payload = 'pass='+request
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'x-api-key': DB_KEY
    }
    response = requests.request('POST', url, headers=headers, data=payload, allow_redirects=False).json()
    encryption = response['PasswordEncy']
    return encryption


def CheckPassword(decyrpt_pass, encrypt_pass):
    DB_KEY = os.environ.get('DB_KEY_DS')
    url = 'http://securedata.rubnet.fr/sercureApi/checkpassword'
    payload = 'pass='+decyrpt_pass+'&encryPass='+encrypt_pass
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'x-api-key': DB_KEY
    }
    response = requests.request('POST', url, headers = headers, data = payload, allow_redirects=False).json()
    return response['PasswordMatch']


def checkSignIn(request):
    DB_KEY = os.environ.get('DB_KEY_DS')
    form = LoginForm(request.POST)
    if(form.is_valid()):
        url = 'http://securedata.rubnet.fr/dataApi/User/Login'
        payload = 'email=' + form.data['RID']
        headers = {
            'x-api-key': DB_KEY,
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        response = requests.request('POST', url, headers = headers, data = payload, allow_redirects=False)
        flag = CheckPassword(form.data['RPassword'])

