## Bibliotecas necessarias
import secrets  ## criptografia da senha
import sqlite3  ## banco de dados local offline, inutil no momento
import string   ## operação com strings, auxilia na criação do algoritmo

    
## Algoritmo teste

## Declaração da função que verifica a senha
def verificar_senha(senha):
    for i in senha: # percorre todos os caracteres da senha, prepara eles pra verificação

        if len(senha) >= 15: # se a senha for maior ou igual a 15, então:

            if any(i.isupper() for i in senha): #se a senha possuir alguma letra maiscula, então:

                if any(i.islower() for i in senha):  #se a senha possuir alguma letra minuscula, então:

                    return(senha) #se todas as condições acima forem verdadeiras, a função retorna a senha
    

## Declaração da função que gera a senha
def gerar_senha():
    while True: # Loop infinito
        char_senha = string.ascii_letters + string.punctuation + string.digits  ## cria uma sequencia de caracteres (letras,pontuação e digitos) 

        senha = ''.join(secrets.choice(char_senha) for i in range(15)) #escolhe de forma completamente aleatória 15 caractéres da sequencia que foi criada

        resultado = verificar_senha(senha) # chama a função verificar_senha() e guarda o valor de return dela na variável resultado

        if resultado == senha: # se o valor for a própria senha, então a função retorna senha

            return senha
            
senha_gerada = gerar_senha() #chama a função, pega seu return e guarda em uma variável

print(senha_gerada) #mostra a senha para o usuário

### se quiser, verifica a senha no site - > https://password.kaspersky.com/pt/