# -*- coding: utf-8 -*-


"""
@author: Xu Gaoxiang
@license: Apache V2
@email: djstava@gmail.com
@site: https://www.xugaoxiang.com
@software: PyCharm
@file: threads.py
@time: 2019/1/10 11:03
"""

import time

from PyQt5.QtCore import QThread, pyqtSignal

class WorkThread(QThread):
    
    finishSignal = pyqtSignal(str)
    
    def __init__(self,  ip, port, parent=None):
        super(WorkThread, self).__init__(parent)
        
        self.ip = ip
        self.port = port
        
    def run(self):
        '''
        重写方法
        '''
        
        print('=============sleep======ip: {}, port: {}'.format(self.ip, self.port))
        time.sleep(20)
        
        self.finishSignal.emit('This is a test.')
        return