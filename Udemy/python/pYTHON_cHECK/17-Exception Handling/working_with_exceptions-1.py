import subprocess
try:
    print("hello World")
except:
    print("Installing the missing module")
    cmd=['pip', 'install', 'fabric', '--user']
    sp=subprocess.Popen(cmd,shell=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
    rc=sp.wait()
    o,e=sp.communicate()
    if rc==0:
        print("fabric module installed", o)
    else:
        print("Command failed", e)    
