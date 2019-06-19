import requests
import os
from .encrypt import encryptWord


def setblood(request, form):
    if(form.is_valid()):
        DB_KEY = os.environ.get('DB_KEY_DS')
        DB_LINK = os.environ.get('DB_LINK_DS')
        url = DB_LINK+'dataApi/dataMedical/Blood'
        payload =   'ID='+encryptWord(form.data['RID']) + \
                    '&Glucose='+encryptWord(form.data['Glucose']) + \
                    '&Urea='+encryptWord(form.data['Urea']) + \
                    '&Creatinine='+encryptWord(form.data['Creatinine']) + \
                    '&eGFR='+encryptWord(form.data['eGFR']) + \
                    '&UricAcid='+encryptWord(form.data['UricAcid']) + \
                    '&Potassium='+encryptWord(form.data['Potassium']) + \
                    '&Sodium='+encryptWord(form.data['Sodium']) + \
                    '&Calcium='+encryptWord(form.data['Calcium'])+ \
                    '&Phosphore='+encryptWord(form.data['Phosphore'])+ \
                    '&Magnesium='+encryptWord(form.data['Magnesium']) + \
                    '&Cholesterol='+encryptWord(form.data['Cholesterol']) + \
                    '&Triglycerides='+encryptWord(form.data['Triglycerides']) + \
                    '&Protein='+encryptWord(form.data['Protein']) + \
                    '&Bilirubin_b='+encryptWord(form.data['Bilirubin_b']) + \
                    '&Alkaline_Phosphatase='+encryptWord(form.data['Alkaline_Phosphatase']) + \
                    '&ALT='+ encryptWord(form.data['ALT'])                
        headers = {
            'x-api-key': DB_KEY,
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        response = requests.request('POST', url, headers = headers, data = payload, allow_redirects=False).json()
        return response

def getblood(request):
    DB_KEY = os.environ.get('DB_KEY_DS')
    if 'log' in request.session:
        url = 'http://securedata.rubnet.fr/dataApi/dataMedical/Blood?ID=' + request.session['id']
        payload = {}
        headers = {
            'x-api-key': DB_KEY
        }
        response = requests.request('GET', url, headers = headers, data = payload, allow_redirects=False).json()
        if len(response['msg']):
            return response['msg'][0]
        else:
            return False
    else:
        return False

def seturine(request, form):
    DB_KEY = os.environ.get('DB_KEY_DS')
    url = 'http://securedata.rubnet.fr/dataApi/dataMedical/Urine'
    payload =   'ID='+encryptWord(form.data['RID']) + \
                '&PH=' + encryptWord(form.data['PH']) + \
                '&Nitrit='+encryptWord(form.data['Nitrit']) + \
                '&Ketone='+encryptWord(form.data['Ketone']) + \
                '&Urobilinogen='+encryptWord(form.data['Urobilinogen']) + \
                '&Bilirubin='+encryptWord(form.data['Bilirubin']) + \
                '&Leucocytes='+encryptWord(form.data['Leucocytes']) + \
                '&Erythrocytes='+encryptWord(form.data['Erythrocytes']) + \
                '&Albumin='+encryptWord(form.data['Albumin'])
    headers = {
        'x-api-key':  DB_KEY,
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.request('POST', url, headers = headers, data = payload, allow_redirects=False).json()
    return response

def geturine(request):
    DB_KEY = os.environ.get('DB_KEY_DS')
    if 'log' in request.session:
        url = 'http://securedata.rubnet.fr/dataApi/dataMedical/Urine?ID='+request.session['id']
        payload = {}
        headers = {
            'x-api-key': DB_KEY
        }
        response = requests.request('GET', url, headers = headers, data = payload, allow_redirects=False).json()
        return response
    else:
        return False

def setdiabete(request, form):
    DB_KEY = os.environ.get('DB_KEY_DS')
    url = 'http://securedata.rubnet.fr/dataApi/dataMedical/diabetes'
    payload =   'ID='+encryptWord(form.data['RID']) + \
                '&Glucose='+encryptWord(form.data['Glucose']) + \
                '&Albumin='+encryptWord(form.data['Albumin']) + \
                '&FGP='+encryptWord(form.data['FGP']) + \
                '&RPG='+encryptWord(form.data['RPG']) + \
                '&CGTT='+encryptWord(form.data['CGTT']) + \
                '&CapillaryGlucose='+encryptWord(form.data['CapillaryGlucose']) + \
                '&HBA1C='+encryptWord(form.data['HBA1C'])
    headers = {
        'x-api-key': DB_KEY,
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.request('POST', url, headers = headers, data = payload, allow_redirects=False).json()
    return response

def getdiabete(request):
    DB_KEY = os.environ.get('DB_KEY_DS')
    if request.session['log']:
        url = 'http://securedata.rubnet.fr/dataApi/dataMedical/diabetes?ID='+request.session['id']
        payload = {}
        headers = {
            'x-api-key': DB_KEY
        }
        response = requests.request('GET', url, headers = headers, data = payload, allow_redirects=False).json()
        return response
    else:
        False

def getid(request):
    DB_KEY = os.environ.get('DB_KEY_DS')
    if request.session['log']:
        url = 'http://securedata.rubnet.fr/dataApi/User/Allid'
        payload = {}
        headers = {
            'x-api-key': DB_KEY
        }
        response = requests.request('GET', url, headers = headers, data = payload, allow_redirects=False).json()
        return response['msg']
    else:
        return False