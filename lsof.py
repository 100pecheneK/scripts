import os
import subprocess

direct_output = str(subprocess.check_output('lsof -i tcp:5000', shell=True))
command = direct_output.find('node')
user = direct_output.find('misha')
pid = direct_output[command+8:user]
os.system(f'kill -9 {pid}')
