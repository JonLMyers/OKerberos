import argparse
from  okerberos.client import app as clientapp
from okerberos.authserver import app as authapp
from okerberos.server import app as webapp

parser = argparse.ArgumentParser()

list_of_services = {'authserver': authapp.run, 'client': clientapp.run, 'appserver' : webapp.run}

parser.add_argument('service', choices=list_of_services.keys(), help="start the app server" )

def execute():
    arguments = parser.parse_args()
    list_of_services[arguments.service]()
