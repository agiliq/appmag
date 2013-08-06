from __future__ import with_statement

from fabric.api import *
from fabric.operations import run
from fabric.context_managers import cd, settings
from fabric.api import env
from fabric.colors import green


HOST_NAME = ['apps.in']
USER = "appmag"
REPO_PATH = "/home/appmag/env_appmag/appmag"
env.activate = 'source /home/appmag/env_appmag/bin/activate'

env.hosts = HOST_NAME
env.user = USER
env.directory = REPO_PATH
env.port = 49254


def restart():
    print(green("Restarting...\n"))
    run("/home/appmag/scripts/appmag_restart.sh")
    print(green("Restarted\n"))


def syncdb():
    print(green("syncdb is running...\n"))
    run("python manage.py syncdb")


def deploy():
    with settings(user=USER):
        with cd(env.directory):
            with prefix(env.activate):
                print(green("Pulling the latest code...\n"))
                run("git pull")
                print(green("Migrating database...\n"))
                run("python manage.py migrate")

            restart()

if __name__ == "__main__":
    deploy()
