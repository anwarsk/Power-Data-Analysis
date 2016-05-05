'''
Created on Mar 15, 2016

This is the First Python script to be execute while running Program Power.

@author: Anwar

'''
import logging
import os
import sys

from Calculator import Calculator
import Config
import Constants
import Data
from InputReader import  InputReader
from OutputWriter import OutputWriter
from Validator import Validator


logging.basicConfig(stream=sys.stdout, level=Config.LOG_LEVEL, format='%(asctime)s - %(levelname)s - %(message)s')

''' Test Area '''

#inputReader = InputReader()
#inputReader.readData()
#Data.Q = [[0 for i in range(2)] for i in range(3)]
#print (Constants.timeVsTechnologyHeader)
''' ==================================== '''

print "Program execution started..."

''' Validate the configuration for the program'''
validator = Validator()
if validator.validateConfig() == False:
    exit(1)

''' Read input directory and create data file '''
inputReader = InputReader()
inputReader.readPortfolioFile()

for portfolio in Data.portfolios:
    logging.debug("Started Processing Portfolio"+ portfolio.name)
    Config.inputFileDirectory = portfolio.inputDirectory 
    inputReader.readData()
    
    ''' Calculate W for the portfolio '''
    calculator = Calculator()
    totalWForPortfolio = calculator.calculateWForPortfolio(0)
    portfolio.setTotalW(totalWForPortfolio)
    
    outputWriter = OutputWriter()
    portfolioOutputDirectory = Config.outputFileDirectory + "/" + portfolio.name
    if not os.path.exists(portfolioOutputDirectory):
        os.mkdir(portfolioOutputDirectory)
    if os.path.isdir(portfolioOutputDirectory):
        outputWriter.writeData(portfolioOutputDirectory)
        
print "Creating required output files..."    
outputWriter.writeSummary()
print "Program execution completed successfully."