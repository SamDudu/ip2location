from os import name
from subprocess import run
from colorama import Fore
from requests import get
from sys import exit , argv
from time import sleep
import json
import webbrowser
if name == 'nt':
	webbrowser.open('https://t.me/LizardSEC')
else:
	run('xdg-open https://t.me/LizardSEC',shell=True)
if name == 'nt':
	run('cls',shell=True)
else:
	run('clear',shell=True)
blue = Fore.BLUE
white = Fore.WHITE
if len(argv) == 1:
    if name == 'nt':
        run('cls',shell=True)
    else:
        run('clear',shell=True)
    print(blue+'''
ip2location script v 1.0
coded by bl4ckwin

usage:
python -i <ip address>
'''+white)
    exit()
else:
    pass
url = 'https://ipwhois.app/json/'
if argv[1] == '-i':
    pass
else:
    if name == 'nt':
        run('cls',shell=True)
    else:
        run('clear',shell=True)
    print(blue+'''
ip2location script v 1.0
coded by bl4ckwin

usage:
python -i <ip address>
'''+white)
    exit()
ip_address = argv[2]
data = get(url+str(ip_address))
data = json.loads(data.text)
msg = data['success']
if msg == 'false':
     print(blue+'[!] '+white+'Error , Please Check The IP Address Or Internet Connection !')
else:
    pass
lat = data['latitude']
lon = data['longitude']
continent = data['continent']
country = data['country']
region = data['region']
city = data['city']
isp = data['isp']
print('IP Address : '+str(ip_address))
print('Internet Service Pervoider : '+str(isp))
print('Continent : '+str(continent))
print('Country : '+str(country))
print('Region : '+str(region))
print('City : '+str(city))
print('Latitude : '+str(lat))
print('Longitude : '+str(lon))
print('Google Maps Link : https://maps.google.com/maps/search/'+str(lat)+'+'+str(lon))
