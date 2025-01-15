# Imporatações
import pyautogui as pa
import pandas as pd
import time

# Dando pausa de código em código
pa.PAUSE = 0.3

# Abrindo os links
pa.press('win')
time.sleep(0.5)
pa.write('chrome')
time.sleep(1)
pa.press('enter')
time.sleep(3)

pa.click(x=604, y=418)
time.sleep(3)

pa.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
time.sleep(1.5)
pa.press('enter')
time.sleep(4)

pa.click(x=438, y=373)
time.sleep(0.5)
pa.write('gerente@gmail.com')
pa.press('tab')
time.sleep(0.5)
pa.write('28092007@uVa')
pa.press('tab')
time.sleep(0.5)
pa.press('enter')
time.sleep(2)

# Cadastrando produtos
tabela = pd.read_csv('produtos.csv')

for linha in tabela.index:
    pa.click(x=454, y=256)
    time.sleep(1)
    '''
    fórmula: str(tabela.loc[linha, 'coluna'])
    Explicando: Pego a tabela e coloco o 'loc' que significa localizar algo,
    passo os parametros linha que vai ser o indice(1,2,3...)
    e passo o nome da coluna.
    '''

    # codigo
    pa.write(str(tabela.loc[linha, 'codigo'])) 
    pa.press('tab')
    time.sleep(0.5)

    # marca
    pa.write(str(tabela.loc[linha, 'marca']))
    pa.press('tab')
    time.sleep(0.5)

    # tipo
    pa.write(str(tabela.loc[linha, 'tipo']))
    pa.press('tab')
    time.sleep(0.5)

    # categoria
    pa.write(str(tabela.loc[linha, 'categoria']))
    pa.press('tab')
    time.sleep(0.5)

    # preco_unitario
    pa.write(str(tabela.loc[linha, 'preco_unitario']))
    pa.press('tab')
    time.sleep(0.5)

    # custo
    pa.write(str(tabela.loc[linha, 'custo']))
    pa.press('tab')
    time.sleep(0.5)

    # obs
    obs = str(tabela.loc[linha, 'obs'])
    if obs != 'nan':
        pa.write(obs)
    pa.press('tab')
    time.sleep(3)

    # enviar
    pa.press('enter')
    pa.press('enter')
    pa.press('enter')
    pa.scroll(10000000)