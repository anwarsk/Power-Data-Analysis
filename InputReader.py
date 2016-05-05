'''
Created on Mar 15, 2016

This is function that will read the input for the program and update the Data module of the program.
@author: Anwar
'''
import Constants
import Data
import os
import Config
import logging
import Portfolio

class InputReader:
    ''' Class for reading the input files '''
    def readD(self):
        ''' reading d matrix from the file d.csv '''
        os.chdir(Config.inputFileDirectory)
        with open(Constants.D_FILE_NAME) as dFile:
            next(dFile)
            next(dFile)
            Data.T = 0
            for line in dFile:
                lineData = line.strip().split(',')[2:]
                Data.d.append(map(float,lineData))
                Data.T += 1
            # Transpose of the matrix to put in d[technologyIndex][timeIndex] format
            Data.d = zip(*Data.d)
            
        logging.debug("Reading D Successful")
    
    def readE(self):
        ''' reading d matrix from the file d.csv '''
        os.chdir(Config.inputFileDirectory)
        with open(Constants.E_FILE_NAME) as EFile:
            next(EFile)
            next(EFile)
            next(EFile)
            for line in EFile:
                lineData = line.strip().split(',')[3:]
                Data.E.append(map(float,lineData))
            Data.E = zip(*Data.E)
            
        logging.debug("Reading E Successful")
        
    def readCF(self):
        ''' reading d matrix from the file d.csv '''
        os.chdir(Config.inputFileDirectory)
        with open(Constants.CF_FILE_NAME) as CFFile:
            next(CFFile)
            next(CFFile)
            next(CFFile)
            for line in CFFile:
                lineData = line.strip().split(',')[3:]
                Data.CF.append(map(float,lineData))
            Data.CF = zip(*Data.CF)
        
        logging.debug("Reading CF Successful")
                
    def readVectors(self):
        ''' reading vectors for different technologies from the file Vectors file '''
        os.chdir(Config.inputFileDirectory)
        with open(Constants.VECTORS_FILE_NAME) as vectorFile:
            next(vectorFile)
            for line in vectorFile:
                lineData = map(float, line.strip().split(',')[2:])
                Data.R.append(lineData[0])
                Data.TCR_o.append(lineData[1])
                Data.FOM_o.append(lineData[2])
                Data.VOM_o.append(lineData[3])
                Data.n_o.append(lineData[4])
                Data.Q_o.append(lineData[5])
                Data.EF.append(lineData[6])
                Data.COF.append(lineData[7])
                Data.PR_TCR.append(lineData[8])
                Data.PR_FOM.append(lineData[9])
                Data.PR_VOM.append(lineData[10])
                Data.PR_n.append(lineData[11])
                   
        logging.debug("Reading Vectors Successful")
        
    def readScalars(self):
        os.chdir(Config.inputFileDirectory)
        with open(Constants.SCALARS_FILE_NAME) as scalarFile:
            lines = scalarFile.readlines()
            Data.r = float(lines[0].strip().split(',')[1])
            Data.ACC_0 = float(lines[1].strip().split(',')[1])
            Data.m = float(lines[2].strip().split(',')[1])
            Data.mu = float(lines[3].strip().split(',')[1])
            Data.sigma = float(lines[4].strip().split(',')[1])
            Data.kappa = float(lines[5].strip().split(',')[1])
            Data.lamda = float(lines[6].strip().split(',')[1])
            Data.ceta = float(lines[6].strip().split(',')[1])
            
        logging.debug("Reading Scalars Successful")
            
    def readData(self):
        self.clearData()
        self.readE()
        self.readD()
        self.readCF()
        self.readVectors()
        self.readScalars()
        
        logging.debug("Reading Data Successful")
        
    def readPortfolioFile(self):
        os.chdir(Config.inputFileDirectory)
        with open(Config.multiPortfolioInputFile) as portfolioFile:
            next(portfolioFile)
            for line in portfolioFile:
                lineData = line.strip().split(',')[1:]
                portfolio = Portfolio.PortFolio(lineData[0], lineData[1])
                Data.portfolios.append(portfolio) 

    def clearData(self):
        Data.d = []
        Data.E = []
        Data.CF = []
        
        ''' Vectors'''
        Data.R = []
        Data.TCR_o = []
        Data.FOM_o = []    
        Data.VOM_o = []    
        Data.n_o = []
        Data.Q_o = []  
        Data.EF = []
        Data.COF = []
        Data.PR_TCR = []
        Data.PR_FOM = []
        Data.PR_VOM = []
        Data.PR_n = []
        Data.LR = []
        Data.J = []
        Data.B = []
        
        ''' ScalarA '''
        Data.ACC_0 = 0
        Data.r = 0
        Data.m = 0
        Data.mu = 0
        Data.sigma = 0
        Data.kappa = 0
        Data.lamda = 0
        Data.ceta = 0
        
        
        ''' Calculated Data '''
        Data.T = 0
        Data.W_out = []
        Data.Q_out = []
        Data.E_out = []
        Data.TCR_out = []

