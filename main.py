# !/usr/bi/python3
# -*- coding: utf8 -*-
# --- --- --- --- --- --- --- ---
#
# date:          2022-44-29
# autor:         and0.0bna
# version:       0.0
# Descriptions:  App de terminal para descargar Musica
#                y videos de youtube, y letras de canciones.
#
# --- --- --- --- --- --- --- ---

from lemuvi import menuMain, menuYoutube, menuLetters, menuInsert, menuInsertDIRS, insertError

from lemuvi import Controls
from time import sleep
from os import system
#from lemuvi import Downloadletters
from lemuvi import DownloadYoutube

class Main():
    def __init__(self):
        self.mainMenu()

    def error(self, i=True):
        system('clear')
        insertError(i)
        input('\n    -- presiona ENTER para continuar --')
        system('clear')

    def mainMenu(self):
        system('clear')
        self.control = Controls()
        while True:
            menuMain()
            op = input("> ")
            ### ### ### Download Music ### ### ###
            if op == '1':
                system('clear')
                menuYoutube()
                url = input('> ')
                if url != '00':
                    self.control.cdownloads(url)
                    if self.control.e:
                        self.error(i=False)
                else:
                    menuMain()
                    system('clear')
            ### ### ### Download Videos ### ### ###
            elif op == '2':
                system('clear')
                menuYoutube('v')
                url = input('> ')
                if url != '00':
                    self.control.cdownloads(url, Music=False)
                    if self.control.e:
                        self.error(i=False)
                else:
                    menuMain()
                    system('clear')
            ### ### ### Menu Letter ### ### ###
            elif op == '3':
                system('clear')
                menuLetters()
                op = input('> ')
                if op == '1':
                    system('clear')
                    menuInsert()
                    self.control.cShowArtists()
                    if self.control.e:
                        self.error()
                elif op == '2':
                    system('clear')
                    menuInsert('a')
                    self.control.cShowmusic()
                    self.control.cgetletters()
                    system('clear')
                elif op == '3':
                    menuInsert('c')
                elif op == '4':
                    print("Opcion 3")
                elif op == '0':
                     print("### Adios ###")
                     sleep(1)
                     break
                elif op == '00':
                    menuMain()
                    system('clear')
                else:
                    print("Opcion invalida")
                    sleep(1)
                    system('clear')
                    op = '3'
            elif op == '0':
                 print("### Adios ###")
                 sleep(1)
                 break
            else:
                system('clear')
                insertError()
                input('\n    -- presiona ENTER para continuar --')
                system('clear')


Main()
