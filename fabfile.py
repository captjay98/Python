from fabric.api import *
from fabric.colors import *

webs = '3.238.73.163'
webss = '3.236.138.26'
weblb = '3.236.251.41'

env.user = 'ubuntu'
env.roledefs['webservers'] = [webs, webss]
env.roledefs['loadbalancers']= 'weblb'


@roles('webservers', 'loadbalancers')
def uptodate():
    run('sudo apt update')
    run('sudo apt upgrade')


@roles('webservers')
def serverstatus():
    output =run('sudo service nginx status')
    print(output)
    print(green('Server status check done'))


@roles('webervers')
def restartServer():
    run(' sudo service nginx restart')
    print(red('Server Restarted'))

@roles('loadbalancers')
def lbstatus():
    sudo('service haproxy status')

@hosts(webs)
def movefile():
    pdirname = prompt("Enter path of file to move:- ")
    ndirname = prompt("Enter path to move file to:- ")
    with cd('ndirname'):
        req = put(pdirname, ndirname)
    print(req.succeeded)


@hosts(webs)
def download():
    rdirname = prompt('Enter path of file you want to download:- ')
    ldirname = prompt("Enter where you want to put it:- ")
    with lcd('ldirname'):
        req = get(rdirname, ldirname)
    print(req.succeeded)


@hosts(webs, webss)
def makedir():
    dir = prompt('enter path to create Dir:- ')
    with cd(dir):
        sudo('mkdir play')


@hosts(webs)
def search():
    path = prompt('Enter Path to search')
    with cd(path):
        comm = prompt('Enter Find command')
        sudo(comm)


@roles('webservers')
def getWebLog():
    dir = prompt("Enter path to save file to:-")
    get('/var/log/nginx/access.log', dir)

def startDjango():
    path = prompt("Enter path to start project")
    with lcd(path):
        env = prompt("Enter environment name")
        run(f"python3 -m venv {env}")
        run(f"source {env}/bin/activate")

    ppath = prompt("Enter path to create project")
    with lcd(path):
        pname = prompt("Enter project name")
        run(f"django-admin startproject {pname}")

    apath = prompt("Enter path to create app")
    with lcd(apath):
        aname = prompt("Enter app name")
        run(f"Python3 manage.py startapp {aname}")
