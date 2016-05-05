'''
Created on Mar 15, 2016

This is validator module that will validate the inputs given to the program 

@author: Anwar

'''

import Config
import os

class Validator:
    
    def validateConfig(self):
        '''
        This function is responsible for validating the configuration provided in Config.py
        @return: true if configurations are valid else false
        @note: This function will print necessary error message for invalid configuration
        '''
        errorMessage = ""
        isValidConfig = True
        
        # Validate the input directory 
#         if os.path.isdir(Config.inputFileDirectory):
#             if os.access(Config.inputFileDirectory, os.R_OK):
#                 '''Check the contents of the directory if all files exists '''
#                 
#             else:
#                 errorMessage = "Input directory does not have read access."
#         else:
#             errorMessage = "Input directory Does not exists"
        
        # Validate the output directory
        if not os.path.exists(Config.outputFileDirectory):
            os.makedirs(Config.outputFileDirectory)
            
        if os.path.isdir(Config.outputFileDirectory):
            if os.access(Config.outputFileDirectory, os.W_OK):
                ''' Valid output directory'''
            else:
                errorMessage += "Output directory does not have write access"
        else:
            errorMessage += "Output directory Does not exists"
        
        print(errorMessage)
        if errorMessage != "":
            isValidConfig = False
        return isValidConfig