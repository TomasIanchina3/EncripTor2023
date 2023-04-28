import subprocess

comando = 'sudo apt-get install python3'
comando2 = 'sudo apt-get install python3-tk'

proceso= subprocess.Popen(comando,shell = True,stdin=subprocess.PIPE)
proceso2 = subprocess.Popen(comando2,shell=True,stdin=subprocess.PIPE)

contraseña ='1234'
proceso.stdin.write(contraseña.encode('utf-8'))
proceso.stdin.flush()
proceso2.stdin.write(contraseña.encode('utf-8'))
proceso2.stdin.flush()

proceso.wait()
proceso2.wait()