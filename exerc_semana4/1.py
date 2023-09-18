import re

def validar_email_usuario(texto):
    #verificar se o email contém @ e .com.br
    arroba = email.find('@') != -1
    _com_br = email.lower().find('.com.br') != -1

    #o email sera validado se os elementos estiverem presentes!
    return arroba and _com_br
def validar_senha(senha):
    #verificar se a senha tem pelo menos 8 caracteres
    if len(senha) < 8:
        return False
    #verificar se a senha contem pelo menos umas letra maiscula e uma minuscula.
    if not (any(c.isupper() for c in senha) and any (c.islower() for c in senha)):
        return False
    #verificar se a senha contem pelo menos um caractere especial
    if not re.search(r'[!@#$%]', senha):
        return False
    
    #Se todas as verificacoes passaram, a senha é valida
    return True


usuario = input('Digite seu nome completo: \n')
email = input('Digite seu email, favor conter @ e .com.br: \n')
resultado = validar_email_usuario(email)

senha = input('Digite sua senha, favor conter no minimo 8 caracteres, conter uma letra minúscula e maiúscula e um caractere especial!: \n')
resultado_senha = validar_senha(senha)

print(f'E-mail do usuario {usuario} é valido? {resultado}')
print(f'Senha do usuário {usuario} é valida? {resultado_senha}')
