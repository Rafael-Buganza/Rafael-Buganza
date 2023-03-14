#!/usr/bin/env python
# coding: utf-8


# In[121]:


import pyautogui
from time import sleep

pyautogui.PAUSE = 1

pyautogui.hotkey ('ctrl', 't')
pyautogui.write ('https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema')
pyautogui.press ('Enter')

sleep(3)

pyautogui.click(x=587, y=367)
pyautogui.write('login@formulario')

pyautogui.click(x=671, y=456)
pyautogui.write('password')

pyautogui.click(x=700, y=524)

sleep(3)

pyautogui.click(x=394, y=377)
pyautogui.click(x=889, y=190)
pyautogui.click(x=970, y=556)
sleep(3)




# In[122]:


#sleep(5)

#print(pyautogui.position


# In[123]:


import pandas as pd

tabela = pd.read_csv(r"C:/Users/Rafa/Downloads/Compras.csv", sep=";")

ValorFinal = tabela["ValorFinal"].str.replace(',', '.')

total_gasto = ValorFinal.astype(float).sum()
quantidade = tabela["Quantidade"].sum()
preco_medio = total_gasto / quantidade

"""
display(tabela)
print(total_gasto)
print(quantidade)
print(preco_medio)"""


# In[124]:


import pyautogui
from time import sleep
import pyperclip

pyautogui.PAUSE = 1

pyautogui.hotkey ('ctrl', 't')
pyautogui.write ('https://mail.google.com/mail/u/1/#inbox')
pyautogui.press ('Enter')

sleep(2)

pyautogui.click(x=102, y=198)
pyautogui.write('buganza20@gmail.com')
pyautogui.press('Enter')

pyautogui.press('tab')
pyperclip.copy('Relatório de Vendas de hoje!')
pyautogui.hotkey('ctrl', 'v')

pyautogui.press('tab')
pyperclip.copy(f"""Prezados,
Segue o relatório de compras

Total Gasto: {total_gasto:,.2f} 
Quantidade de produtos: {quantidade:,.2f}
Preço Médio: R$ {preco_medio:,.2f} 

Att Rafael Buganza""")
pyautogui.hotkey('ctrl','v')

pyautogui.hotkey('Ctrl', 'Enter')


# In[ ]:




