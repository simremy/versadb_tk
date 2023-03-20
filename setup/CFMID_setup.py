import time, os, subprocess
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

# Do you need to install cfmid ?
if not os.path.exists(path_idg + '/CFM_ID_4/ID_container_cfmid.txt'):
    print('You need to install CFM-ID4.0. So, take a coffee with you, the computer will work for you.')
    print(os.getcwd())
    # Install cfmid docker image
    Popen('start cmd.exe /k ' + path_idg + '/setup/Install_CFMID.bat ', shell=True)
    print('Installing CFM-ID4.0 on docker.')
    time.sleep(90)
    print('CFMID-4.0 was install with success ! Wait until it runs.')
    time.sleep(10)

    cfmid_container_name = ''
    if os.path.exists(path_idg + '/CFM_ID_4/container_names.txt'):
        print('OK, here were are !')
        filein = open(path_idg + '/CFM_ID_4/container_names.txt' , 'r').read().split('\n')
        for line in filein:
            if str('wishartlab/cfmid:4.2.6.0') in line:
                cfmid_container_name = (line.split('   ')[-1].replace(' ', ''))
                print(cfmid_container_name)

    else:
        print('OK, keep calm and wait one more time.')
        time.sleep(60)
        filein = open(path_id + '/CFM_ID_4/container_names.txt' , 'r').read().split('\n')
        for line in filein:
            if str('wishartlab/cfmid:4.2.6.0') in line:
                cfmid_container_name = (line.split('   ')[-1].replace(' ', ''))
                print(cfmid_container_name)
    # Get cfmid docker image id      
    if cfmid_container_name != '' :
        os.system('docker inspect --format="{{.Id}}" ' + cfmid_container_name + ' > ' + path_idg + '/CFM_ID_4/ID_container_cfmid.txt')
        ID_container_id = open(path_id + '/CFM_ID_4/ID_container_cfmid.txt', 'r').read().split('\n')[0]
        print(ID_container_id)
    else:
       print('crush everything and restart CFM-ID4.0 installation...')
        
    # Install GNU parallel in cfmid docker image    
    os.system('docker start ' +  ID_container_id)
    os.system('docker exec -t ' + ID_container_id + ' apk add make') # You must install this !
    os.system('docker exec -t ' + ID_container_id + ' apk add perl') # You must install this !
    os.system('docker  exec -t ' + ID_container_id + ' wget https://ftp.gnu.org/gnu/parallel/parallel-20201222.tar.bz2') #version is 20201222 !
    time.sleep(5)
    os.system('docker  exec -t ' + ID_container_id + ' tar -xjvf parallel-20201222.tar.bz2')
    time.sleep(10)
    os.system('docker exec -t ' + ID_container_id + ' rm -rf parallel-20201222.tar.bz2 ')
    time.sleep(5)

    os.system('docker exec -t ' + ID_container_id + '  parallel-20201222/configure ')
    time.sleep(5)
    os.system('docker exec -t ' + ID_container_id + ' make ./parallel-20201222/  ')
    time.sleep(5)
    os.system('docker exec -t ' + ID_container_id + ' make install ./parallel-20201222/  ')
    
    print('Everything must be in place ! Bravo !')
    
    filesetup = open(path_id + '/setup/CFMID_Tool_conf.txt' , 'w')
    filesetup.write('Tool installation')
    
    

    
else:
    print('CFM-ID4.0 has already been installed.')