'''
Created on May 5, 2016

@author: anwar
'''

class PortFolio(object):
    '''
    classdocs
    '''
    name = ""
    inputDirectory = ""
    totalW = 0
    def __init__(self, name, inputDirectory):
        self.name = name
        self.inputDirectory = inputDirectory
    
    def setTotalW(self, totalW):
        self.totalW = totalW