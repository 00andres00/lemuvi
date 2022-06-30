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

from modules import Menu
from modules import ControlScraper
from time import sleep
from os import system

#from .modules import Downloadletters
#from .modules import DownloadMusic
#from .modules import DownloadVideos

class SearchLetters():
    def __init__(self):
        self.menu = Menu()
        self.mainMenu()

    def menuletters(self):
        op = input('> ')
        if op == "1":
            system('clear')
            self.menu.menuInsertLetter()
            self.control.cShowArtists()
            input("-Enter-")

        elif op == '2':
            system('clear')
            self.menu.menuInsert()
            self.control.cShowmusic()
            self.control.cgetletters()
            system('clear')
        elif op == '3':
            print("Opcion 3")
        elif op == '00':
            self.mainMenu()
        else:
            print("Opcion invalida")
            sleep(1)
            system('clear')

    def mainMenu(self):
        system('clear')
        while True:
            self.menu.menu()
            self.control = ControlScraper()
            op = input("> ")
            if op == '1':
                system('clear')
                self.menu.menuYoutube()
                url = input('> ')
                DownloadMusic(url)
                system('clear')
            elif op == '2':
                system('clear')
                self.menu.menuYoutube()
                url = input('> ')
                DownloadVideos(url)
                system('clear')
            elif op == '3':
                system('clear')
                self.menu.menuLetters()
                self.menuletters()
            elif op == '0':
                print("### Adios ###")
                sleep(1)
                break
            else:
                print("Opcion invalida")
                sleep(1)
                system('clear')


SearchLetters()
