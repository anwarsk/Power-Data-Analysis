'''
Created on April 29, 2016

@author: anwar
'''

import csv
import os

import Config
import Constants
import Data
import numpy


class OutputWriter(object):
    
    def writeOutput(self):
        os.chdir(Config.outputFileDirectory)
        self.writeW_out()
    
    def writeW_out(self):
        W_outTranspose = numpy.array(Data.W_out)
        with open('W_it.csv', 'wb') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(Constants.timeVsTechnologyHeader)
            for timeIndex in range(Data.T):
                outputRow = [timeIndex]
                outputRow = numpy.concatenate([outputRow, W_outTranspose[:,timeIndex]])
                writer.writerow(outputRow)
    
    def writeE_out(self):
        E_outTranspose = numpy.array(Data.E_out)
        with open('E_it.csv', 'wb') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(Constants.timeVsTechnologyHeader)
            for timeIndex in range(Data.T):
                outputRow = [timeIndex]
                outputRow = numpy.concatenate([outputRow, E_outTranspose[:,timeIndex]])
                writer.writerow(outputRow)
                
    def writeQ_out(self):
        Q_outTranspose = numpy.array(Data.Q_out)
        with open('Q_it.csv', 'wb') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(Constants.timeVsTechnologyHeader)
            for timeIndex in range(Data.T):
                outputRow = [timeIndex]
                outputRow = numpy.concatenate([outputRow, Q_outTranspose[:,timeIndex]])
                writer.writerow(outputRow)
                
    def writeTCR_out(self):
        #TCR_outTranspose = zip(* Data.W_out)
        TCR_outTranspose = numpy.array(Data.TCR_out)
        with open('TCR_it.csv', 'wb') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(Constants.timeVsTechnologyHeader)
            for timeIndex in range(Data.T):
                outputRow = [timeIndex]
                outputRow = numpy.concatenate([outputRow, TCR_outTranspose[:,timeIndex]])
                writer.writerow(outputRow)
                
    def writeData(self, outputFileDirectory):
        os.chdir(outputFileDirectory)
        self.writeW_out()
        self.writeE_out()
        self.writeQ_out()
        #self.writeTCR_out()
        
    def writeSummary(self):
         os.chdir(Config.outputFileDirectory)
         with open('Summary.csv', 'wb') as csvfile:
             writer = csv.writer(csvfile)
             writer.writerow(Constants.summaryHeader)
             portfolioIndex = 0
             for portfolio in Data.portfolios:
                 outputRow = [portfolioIndex, portfolio.name, portfolio.totalW]
                 portfolioIndex += 1
                 writer.writerow(outputRow)