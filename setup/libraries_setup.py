import time, os, subprocess, sys

path_id = os.getcwd()
if " "in path_id :
    ll=path_id.split('\\')
    pa = ""
    for i in range(len(ll)):
        if " " in ll[i] :
            pa += '"'+ll[i]+'"/'
        else :
            pa+=ll[i]+"/"
    path_idg = pa[:-1]
else:
    path_idg = path_id
 
subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r' ,  str(path_idg + "/setup/requirements.txt")])
        
filesetup = open(path_id + '/setup/libraries_app_conf.txt' , 'w')
filesetup.write('libraries installation')    
filesetup.close()  