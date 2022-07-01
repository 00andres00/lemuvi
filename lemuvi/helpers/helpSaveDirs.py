from lemuvi.modules.menus.menus import menuInsertDIRS
from lemuvi.configs import DIR_MUSIC, DIR_VIDEOS

def hsaveDirs(t='M'):
    if t != 'M':
        if DIR_VIDEOS:
            return DIR_VIDEOS
        else:
            menuInsertDIRS(t)


