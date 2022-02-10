import ctypes
import os
import platform


"""This function will return the free space one the drive of the folder (In MB)"""

def disk_space(dossier):
    if platform.system() == 'Windows':
        free_bytes = ctypes.c_ulonglong(0)
        ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(dossier), None, None, ctypes.pointer(free_bytes))
        return free_bytes.value / 1024 / 1024
    else:
        a_os = os.statvfs(dossier)
        return a_os.f_bavail * a_os.f_frsize / 1024 / 1024



"""This function return list of file and subdirectories in a folder"""



def folder_struct(dossier):
    print('====================================="Folder structure"===================================================')
    for root, dirs, files in os.walk(dossier):
        level = root.replace(dossier, '').count(os.sep)
        indent = ' ' * 2 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 2 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))


