import os
import string
import glob
import subprocess
from subprocess import Popen
import shutil
import time
import datetime
from datetime import datetime
import pandas as pd
import requests
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
	
def get_current_path():
    path_id = str(os.getcwd())
    if " "in path_id :
        ll=path_id.split('\\')
        pa = ""
        for i in range(len(ll)):
            if " " in ll[i] :
                pa += '"'+ll[i]+'"/'
            else :
                pa+=ll[i]+"/"
                path_idg = pa[:-1]
        return path_id, path_idg
    else:
        path_idg = path_id
        return path_id, path_idg
		
def check_setup():
	if not os.path.exists(get_current_path()[0].replace('"','') + '/setup/CFMID_Tool_conf.txt'):
		print('CFMID will be configured')
		os.system('python ' + get_current_path()[1] + '/setup/CFMID_setup.py')
	else:
		print('CFMID has already been configured.')

	if not os.path.exists(get_current_path()[0].replace('"','') + '/setup/RDKit_Tool_conf.txt'):
		print('RDKit will be configured')
		os.system('python ' + get_current_path()[1] + '/setup/RDKit_setup.py')
	else:
		print('RDKit has already been configured.')

	if not os.path.exists(get_current_path()[0].replace('"','') + '/setup/NMRShift_Tool_conf.txt'):
		print('NMRShift will be configured')
		os.system('python ' + get_current_path()[1] + '/setup/NMRShift_setup.py')
	else:
		print('NMRShift has already been configured.')
		
def get_cfmid_docker_image():
    return open(get_current_path()[0] + '/CFM_ID_4/ID_container_cfmid.txt', 'r').read().split('\n')[0]
    