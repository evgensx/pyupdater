import subprocess, time
from os import system, name

def clear():
    if name == 'nt': system('cls')  # windows
    else: system('clear')           # mac linux


# proc = subprocess.Popen(args='python -m pip list -o'.split(), text=True, stdout=subprocess.PIPE)
proc = subprocess.Popen(args='pip list -o'.split(), text=True, stdout=subprocess.PIPE)
while proc.returncode == None:
    for i in ["\\", "|", "/", "-"]:
        proc.poll()
        clear()
        print(f'Поиск обновлений {i}')
        time.sleep(0.5)
    clear()
outs, _ = proc.communicate()
if outs != '':
    outs = outs.split()
    for i in outs[8::4]: 
        subprocess.run(f'pip install {i}'.split())
    print('Обновление пакетов завершено')
else:
    print('Нет обновлений')
