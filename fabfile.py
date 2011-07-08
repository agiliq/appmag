from __future__ import with_statement

from fabric.api import *
from fabric.operations import run, sudo
from fabric.context_managers import cd, settings
from fabric.api import env
from fabric.colors import green
HOST_NAME = ['www.appmag.in']
USER = "agiliq"
REPO_PATH = "/home/agiliq/Work/appsite/"

env.hosts = HOST_NAME
env.user = USER
env.directory = REPO_PATH

def restart():
    print(green("Restarting...\n"))
    sudo("/home/agiliq/scripts/appmag_restart.sh")
    print(green("Restarted\n"))

def deploy():
    with settings(user=USER):
        with cd(env.directory):
           print(green("Pulling the latest code...\n"))
           run("git pull")
           restart()
if __name__ == "__main__":
   deploy()

