email = input("Ingresa tu dirección de correo electrónico: ")
nombre, dominio = email.split('@')
dominio_nombre = dominio.split('.')[0]

domninios = ['gmail.com','yahoo.com','hotmail']

for dominio in domninios:
    if(dominio_nombre==dominio):
        print(f"Hola {nombre}, estoy viendo que tu email está registrado con {dominio}. ¡Eso es genial!")
        break;
    else:
        print(f"Hola {nombre}, estoy observando que estás utilizando un dominio personalizado de {dominio_nombre}. ¡Impresionante!")
        break;