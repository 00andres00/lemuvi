def menuMain():
    print("### ### ### Bienvenido ### ### ###")
    print()
    print("1) Descargar musica")
    print("2) Descargar video")
    print("3) Letras")
    print("0) Salir")
    print()
    print(" ### ### ###  ### ### ### ")

def menuYoutube(t='musica'):
    if t != 'musica':
        t = 'videos'
    print("### ### ### Descarga {} desde youtube ### ### ###".format(t))
    print()
    print("\tInserta la url")
    print()
    print("Por ejemplo:")
    print("https://youtube.com/watch?v=example o watch?v=example")
    print("Para las listas de reproduccion")
    print("https://youtube.com/playlist?list=example o playlist?list=example")
    print()
    print("00) Regresar al menu")
    print()
    print("### ### ###  ### ### ###")

def menuLetters():
    print("### ### ### Letras ### ### ###")
    print()
    print("1) Mostrar artistas o bandas")
    print("2) Mostrar canciones de bandas o artistas")
    print("3) Mostrar letra")
    print("4) Descargar letra")
    print("00) Regresar al menu anterior")
    print("0) Salir")
    print()
    print("### ### ###  ### ### ###")

def menuInsert(i="o"):
    if i == 'a':
        i = "el nombre de la banda o artista"
        e = "eminem"
    elif i == 'c':
        i = "el nombre de la Canción"
        e = "Titi Me Pregunto"
    else:
        i = "una letra del abecedario"
        e = "A"
    print("### ### ###  ### ### ###")
    print()
    print("Inserta {}".format(i))
    print("Por ejemplo: {}".format(e))
    print()
    print("00) Regresar al menu principal")
    print()
    print("### ### ###  ### ### ###")

def menuInsertDIRS():
    print("### ### ###  ### ### ###")
    print()
    print("¿Deseas guardar la carpeta de descarga?")
    print()
    print("### ### ###  ### ### ###")

def insertError(i=True):
    if i:
        error = "OPCION INVALIDA"
    else:
        error = "URL INVALIDA"
    print("\t### ### ###  ### ### ###")
    print()
    print("\t-- -- {} -- --".format(error))
    print()
    print("\t### ### ###  ### ### ###")

def valediction():
    print("\t### ### ###  ### ### ###")
    print()
    print("")
    print()
    print("\t### ### ###  ### ### ###")

