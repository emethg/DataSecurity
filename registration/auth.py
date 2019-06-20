import requests
import os
from .encrypt import encryptWord, encryptPassword, CheckPassword, decryptWord
from .forms import RegisterForm

def log_in(request, id, password):
    encrypted_id = encryptWord(id)
    DB_KEY = os.environ.get('DB_KEY_DS')
    DB_LINK = os.environ.get('DB_LINK_DS')
    url = DB_LINK+'dataApi/User/Login'
    encrypted_id = encryptWord(id)
    payload = 'ID='+ encrypted_id
    headers = {
        'x-api-key': DB_KEY,
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.request('POST', url, headers = headers, data = payload, allow_redirects=False).json()
    if response['status']:
        chech_pass = response['userInfo']['Password']
        result = CheckPassword(password, chech_pass)
        if result:
            if not request.session.session_key:
                request.session.save()
                request.session['id'] = request.session.session_key
                test = request.session.session_key
                request.session.set_expiry(100000)
            request.session['ID'] = response['userInfo']['ID']
            request.session['RID'] = response['userInfo']['ID']
            request.session['type'] = response['userInfo']['Type']
            request.session['du'] = decryptWord(response['userInfo']['diabetes'])
            request.session['log'] = 1
            
            return True
        else:
            return False
    else:
        return False

def reg(request, form):
    if(form.is_valid()):
        DB_KEY = os.environ.get('DB_KEY_DS')
        DB_LINK = os.environ.get('DB_LINK_DS')
        url = DB_LINK+'dataApi/User/Register'
        d = int(form.cleaned_data['diabetes'])
        idp = encryptWord(form.data['RID'])
        pwd = encryptPassword(form.data['RPassword'])
        payload =   'ID='+ encryptWord(form.data['RID']) + \
                    '&Password='+ encryptPassword(form.data['RPassword']) + \
                    '&FirstName='+ encryptWord(form.data['RFirstName']) + \
                    '&LastName='+ encryptWord(form.data['RLastName']) + \
                    '&Email='+ encryptWord(form.data['email']) + \
                    '&DateOfBirth='+ encryptWord(form.data['RDateOfBirth'])+ \
                    '&diabetes='+ encryptWord(str(form.cleaned_data['diabetes']))
        headers = {
            'x-api-key': DB_KEY,
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        response = requests.request('POST', url, headers = headers, data = payload, allow_redirects=False).json()
        return response
