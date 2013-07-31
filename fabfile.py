from __future__ import with_statement

from fabric.api import *
from fabric.operations import run
from fabric.context_managers import cd, settings
from fabric.api import env
from fabric.colors import green


HOST_NAME = ['apps.in']
USER = "appmag"
REPO_PATH = "/home/appmag"

env.hosts = HOST_NAME
env.user = USER
env.directory = REPO_PATH
env.port = 49169


def restart():
    print(green("Restarting...\n"))
    run("/home/agiliq/scripts/appmag_restart.sh")
    print(green("Restarted\n"))


def syncdb():
    print(green("syncdb is running...\n"))
    run("python manage.py syncdb")


def migrate():
    print(green("Migrating database...\n"))
    run("python manage.py migrate")


def pull():
    print(green("Pulling the latest code...\n"))
    run("git pull")


def deploy():
    with settings(user=USER):
        with cd(env.directory):
            pull()
            run("source ../bin/activate")
            migrate()
            syncdb()
            restart()
if __name__ == "__main__":
    deploy()
