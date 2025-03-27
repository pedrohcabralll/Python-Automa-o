# Passo 1 - Entrar no sistema da empresa
    ## https:/dlp.hashtagtreinamentos.com/python/intensivao/login
import pyautogui
import time

#pyautogui.PAUSE = x  ---> tempo de delay dos comandos
pyautogui.PAUSE = 1

       
pyautogui.press("win")
pyautogui.write("google chrome")
pyautogui.press("enter")
pyautogui.hotkey("win","up")

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)

pyautogui.press("enter")

#espera 3 segundos
time.sleep(3)

# Passo 2 - Fazer login
pyautogui.press("tab")
pyautogui.write("pedrohcabral007@gmail.com")
pyautogui.press("tab")
pyautogui.write("nurfin")
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(2)

# Passo 3 - Importar a base de dados
import pandas
tabela = pandas.read_csv("produtos.csv")
print(tabela)
# Passo 4 - Cadastrar um produto 
for linha in tabela.index:
    # clicar no campo de código
    pyautogui.click(x=699, y=258)
    # codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")
    # marca
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    # tipo
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")     
    # categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    # preço
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    # custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    # obs
    obs = tabela.loc[linha, "obs"]
    #se ele não tiver vazio(Nan) ele preenche o obs
    if not pandas.isna(obs):
        pyautogui.write(obs)
     
    pyautogui.press("tab")  
    pyautogui.press("enter")
    pyautogui.scroll(3000)
 
# Passo 5 - Repetir isso até acabar a base de dadosgoogle chrome

