'''
Created on 2012-7-29

@author: jiang
'''
'''call windows api to lock computer'''
import ctypes
dll = ctypes.WinDLL("user32.dll")
dll.LockWorkStation();