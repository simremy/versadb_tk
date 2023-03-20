import os
import subprocess
from subprocess import Popen


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
print(path_id)


Popen('start cmd.exe /C ' + path_idg + '/setup/Install_RDKit.bat', shell=True)


filesetup = open(path_id + '/setup/RDKit_Tool_conf.txt' , 'w')
filesetup.write('Tool installation')

