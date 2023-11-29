import os
import subprocess

os.system("ls")
subprocess.run(["ls","-l","Bucles.py"])

command = "uname"
commandArgument = "-a"
print(f'Recolectando información del sistema con el comando: {command} {commandArgument}')
subprocess.run([command,commandArgument])

command ="ps"
commandArgument = "-x"
print(f'Recolectando información de los procesos activos con el comando: {command} {commandArgument}')
subprocess.run([command,commandArgument])