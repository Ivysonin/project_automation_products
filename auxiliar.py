# Pegando informações que vou precisar em alguns locais do código

import pyautogui
import pandas
import time

# Pegando posição do mouse
# time.sleep(5)
# print(pyautogui.position())

# Pegando tabela
tabela = pandas.read_csv('produtos.csv')
print(tabela)