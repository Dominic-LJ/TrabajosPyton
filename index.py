"""
duoc ha contratadpo mi servicio para hacer un login en python
debe validar el usuario y la clave con lo aprendido hoy
"""

usuario = input(str("Ingrese su usuario "))

if usuario == ("duocacad"):
    print("usuario correcto")
    status = "correct"
else:
    print("usuario incorrecto")
    status = ("incorrect")

if status is "correct":
    contrasena = input(str("ingrese contraseña: "))
    if contrasena == ("jajaja123"):
        print("contraseña correcta, bienvenido.")
    else:
        print("contraseña incorrecta")
else:
    print("vuelva a intentarlo")