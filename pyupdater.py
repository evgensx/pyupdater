import subprocess, time
from os import system, name
import sys
k = 1
ulst = None

# def clear():                        # define the clear function
#     if name == 'nt': system('cls')  # for windows
#     else: system('clear')           # for mac and linux

ulst = subprocess.Popen(args='python -m pip list -o'.split(), text=True, stdout=subprocess.PIPE)
# one, two = out
# print(out)
while ulst.returncode == None:
    ulst.poll()
    time.sleep(1)
    # try:
    #     print(ulst)
    #     # ulst = ulst.stdout
    # except AttributeError:
        # out = ulst.communicate(10)
        # print(out)
        # print(type(out))
        # time.sleep(1)

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
