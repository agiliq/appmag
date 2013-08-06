import os

bind = "0.0.0.0:8000"
workers = (os.sysconf("SC_NPROCESSORS_ONLN") * 2) + 1
loglevel = "info"
proc_name = "appmag"
# pythonpath = /usr/lib/python2.7
pythonpath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
