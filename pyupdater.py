import subprocess, time
from threading import Thread
from os import name, system

ulst = None

def clear(): 
    if name == 'nt':
        system('cls')
    else:
        system('clear')

def progress():
    global ulst
    while True:
        for i in ["\\", "|", "/", "-"]:
            if ulst == None:
                clear()
                print(f'Поиск обновлений {i}', flush=True)
                time.sleep(0.5)
            else: 
                exit()

def updater():
    global ulst
    ulst = subprocess.run('python -m pip list -o'.split(), capture_output=True, text=True).stdout
    clear()
    if ulst != '':
        ulst = ulst.split()
        for i in ulst[8::4]: 
            subprocess.run(f'python -m pip install -U {i}'.split())
        print('Обновление пакетов завершено')
    else:
        print('Нет обновлений')
    ulst = ulst.split()

th1 = Thread(target=progress, args=())
th2 = Thread(target=updater, args=())

th1.start()
th2.start()

th1.join()
th2.join()
