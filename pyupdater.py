import subprocess, time
# import os module  
from os import system, name

k = 0
ulst = None
data = None

def clear():                        # define the clear function
    if name == 'nt': system('cls')  # for windows
    else: system('clear')           # for mac and linux

ulst = subprocess.Popen(args='python -m pip list -o'.split(), stdout=subprocess.PIPE)
while True:
    if ulst == None:
        print(type(ulst))
        time.sleep(1)
    else:
        break
# while True: 
#     for i in ["\\", "|", "/", "-"]:
#         if ulst == None:
#             # clear()
#             print(f'Поиск обновлений {i}', flush=True)
#             time.sleep(0.5)
#         else:
#             print(ulst, type(data))
#             break


# def updater():
#     global ulst
    
#     ulst = ulst.split()
#     try:
#         if ulst == []: raise ValueError('Пустое значение')
#         for i in ulst[8::4]: subprocess.run(f'python -m pip install -U {i}'.split())
#         print('Обновление пакетов завершено')
#     except ValueError: 
#         print('Нет обновлений')


"""
Поиск обновлений \
Поиск обновлений |
Поиск обновлений /
Поиск обновлений --
"""
