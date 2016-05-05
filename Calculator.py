'''
Created on Mar 25, 2016

This module is responsible for performing all the necessary calculations for the program

@author: Anwar
'''
import Data
import math
import Constants

class Calculator:

    '''
    This method calculates the Value of 'K'
     
    @param technologyIndex: Index of the technology 
    @param vintageIndex: Index of the vintage
    @param portfolioIndex: Index of the portfolio
    
    @todo: Validation for last 2 params
    
    @return: Value of variable K  
    '''
    def calculateK(self, technologyIndex, vintageIndex, timeIndex, portfolioIndex):
    
        TCR_ivs = Data.TCR_o[technologyIndex]
        R_i = Data.R[technologyIndex]
        d_iv = Data.d[technologyIndex][vintageIndex]
        
        
        K_ivts = (TCR_ivs * d_iv * 1000)/ (1-math.pow((1+d_iv), (-1*R_i)))
        
        return K_ivts
                               
    
    def calculateTCR(self, technologyIndex, vintageIndex, portfolioIndex):
        
        TCR_i0 = Data.TCR_o[technologyIndex]
        Q_i0 = Data.Q_o[technologyIndex]
        alpha_i = self.calculateAlpha(technologyIndex)
        beta_i = self.calculateBeta(technologyIndex)
        row_i = self.calculateRow(technologyIndex)
        C_its = self.calculateC(self, technologyIndex, vintageIndex, portfolioIndex)
        I_its = self.calculateI(technologyIndex, vintageIndex, portfolioIndex)
               
        TCR_ivs = TCR_i0 / ((Q_i0**alpha_i) * (beta_i**row_i)) * pow(C_its, alpha_i) * pow(I_its, row_i)
        Data.TCR_out[technologyIndex][vintageIndex] = TCR_ivs
        return TCR_ivs
    
    def calculateBeta(self,technologyIndex):
        
        PR_FOM = Data.PR_FOM[technologyIndex]
        beta = math.log(PR_FOM, 2)
        
        return beta
    
    def calculateRow(self,technologyIndex):
        
        LR_i = Data.LR[technologyIndex]
        row = math.log(LR_i, 2)
        
        return row
    
    def calculateC(self, technologyIndex, timeIndex, portfolioIndex):
        
        Q_0 = Data.Q_o[technologyIndex]
        Add_ivts = 0
        
        for vintageIndex in range(1,timeIndex):
            Add_ivts += self.calculateAdd(technologyIndex, vintageIndex, timeIndex, portfolioIndex)
        
        C = Q_0 + (Add_ivts/1000)
        
        return C
    
    def calculateI(self, technologyIndex, timeIndex, portfolioIndex):
        
        B_i0 = Data.B[technologyIndex][0]
        
        J_ivts = 0
        for vintageIndex in range(1,timeIndex):
            J_ivts += self.calculateJ(technologyIndex, vintageIndex, timeIndex, portfolioIndex)
        
        I_its = B_i0 + (J_ivts/1000)
        
        return I_its
    
    def calculateAdd(self, technologyIndex, vintageIndex, timeIndex, portfolioIndex):
        
        Q_0 = Data.Q_o[technologyIndex]
        Add = 1
        
        for v in range(1,timeIndex):
            Add += self.calculateAdd()
        
        C = Q_0 + (Add/1000)
        
        return C
    
    def calculateJ(self, technologyIndex, vintageIndex, timeIndex, portfolioIndex):
        
        Q_0 = Data.Q_o[technologyIndex]
        Add = 1
        
        for v in range(1,timeIndex):
            Add += self.calculateAdd()
        
        C = Q_0 + (Add/1000)
        
        return C
    
    def calculateQ_its(self, technologyIndex, vintageIndex, timeIndex, portfolioIndex):
                
        E = Data.E[technologyIndex][timeIndex]
        CF = Data.CF[technologyIndex][timeIndex]
        
        Q_its = E/(CF * 8766)
        
        Data.Q_out[technologyIndex][timeIndex] = Q_its
        return Q_its
    
    def calculateLCOG(self, technologyIndex, vintageIndex, timeIndex, portfolioIndex):
        
        FOM = Data.FOM_o[technologyIndex]
        CF = Data.CF[technologyIndex][timeIndex]
        VOM = Data.VOM_o[technologyIndex]
        COF = Data.COF[technologyIndex]
        n = Data.n_o[technologyIndex]
        ACC = Data.ACC_0
        EF = Data.EF[technologyIndex]
        
        LCOG = (FOM * 1000)/(8766 * CF) + VOM + (COF/n) + ACC*EF
        
        return LCOG
    
    def calculateE_ivts(self, technologyIndex, vintageIndex, timeIndex, portfolioIndex):
        
        Q = self.calculateQ_its(technologyIndex, vintageIndex, timeIndex, portfolioIndex)
        CF = Data.CF[technologyIndex][timeIndex]
        
        E = Q * CF * 8766
        Data.E_out[technologyIndex][timeIndex] = E
        return E
    
    def calculateW(self, technologyIndex, vintageIndex, timeIndex, portfolioIndex):
        
        K_ivts = self.calculateK(technologyIndex, vintageIndex, timeIndex, portfolioIndex)
        Q_ivts = self.calculateQ_its(technologyIndex, vintageIndex, timeIndex, portfolioIndex)
        LCOG_ivts = self.calculateLCOG(technologyIndex, vintageIndex, timeIndex, portfolioIndex)
        E_ivts = self.calculateE_ivts(technologyIndex, vintageIndex, timeIndex, portfolioIndex)
        
        W_ivts = (K_ivts * Q_ivts) + (LCOG_ivts * E_ivts)
        
        return W_ivts
    
    def calculateWForPortfolio(self, portfolioIndex):
        self.intialize()
        totalWForPortfolio = 0
        
        for timeIndex in range(0, Data.T):
            W_t = 0
            for technologyIndex in range(0, len(Constants.technology)):
                W_it = self.calculateW(technologyIndex, timeIndex, timeIndex, portfolioIndex)
                Data.W_out[technologyIndex][timeIndex] = W_it
                W_t = W_t + W_it
            totalWForPortfolio += totalWForPortfolio + (W_t/((1+Data.r)**timeIndex))
        return totalWForPortfolio
    
    def intialize(self):
        Data.Q_out = [[0 for i in range(Data.T)] for i in range(len(Constants.technology))]
        Data.E_out = [[0 for i in range(Data.T)] for i in range(len(Constants.technology))]
        Data.W_out = [[0 for i in range(Data.T)] for i in range(len(Constants.technology))]
        Data.TCR_out = [[0 for i in range(Data.T)] for i in range(len(Constants.technology))]