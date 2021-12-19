import subprocess, time
from threading import Thread

ulst = None

def dotter():
    global ulst
    k = 0
    print('Поиск обновлений',end='')
    while k < 10 and ulst == None:
        print('.', end='', flush=True)
        time.sleep(1)
        k += 1

def updater():
    global ulst
    ulst = subprocess.run('python -m pip list -o'.split(), capture_output=True, text=True).stdout
    print(ulst)
    ulst = ulst.split()
    try:
        if ulst == []: raise ValueError('Пустое значение')
        for i in ulst[8::4]: subprocess.run(f'python -m pip install -U {i}'.split())
        print('Обновление пакетов завершено')
    except ValueError: 
        print('Нет обновлений')

th1 = Thread(target=dotter, args=())
th2 = Thread(target=updater, args=())
th1.start()
th2.start()
