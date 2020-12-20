# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 21:50:06 2020

@author: nahid
"""

import sys

## Normal Matrix Class
class Matrix:
  def __init__(self,dmat=None,matr=None):
    super().__init__()
    if dmat or matr is None:
      dmat = []
      matr = []
    self.dmat= dmat
    self.matr= matr
  
  def diagonal_matrix(self,block_size):
    self.block = block_size
    self.dmat.clear()
    
    print('Input the diagonal coeffiecients: ')
    for i in range(self.block):
      x= int(input('Value of d['+str(i+1)+']['+str(i+1)+']='))
      row = []
      for j in range(self.block):
        if i == j:
          row.append(x)
        else: row.append( 0)
      self.dmat.insert(i, row)
      
    return self.dmat

  def square_matrix(self,block_size):
    self.matr.clear()
    self.block = block_size
    
    print('Input the matrix coefficients:')
    for i in range(self.block):
      sq_row = []
      for j in range(self.block):
        x = float(input('Value of d['+str(i+1)+']['+str(j+1)+']='))
        sq_row.append(x)
      self.matr.append(sq_row)
      
    return self.matr
  
##Nested Matrix class
class Nested_Matrix:
  def __init__(self,matrix_nest=None):
    super().__init__()
    if matrix_nest is None:
      matrix_nest = []
    self.matrix_nest = matrix_nest

  def nested_matrix(self,mat_size):
    self.matrix_nest.clear()
    self.mat_size = mat_size
    
    block = int(float(input('Enter the block size of the diagonal matrix D:')))
    for i in range(self.mat_size):
      row = []
      for j in range(self.mat_size):
        print('For a Diagonal matrix D['+str(i+1)+']['+str(j+1)+']:')
        d = Matrix() # block size
        D = d.diagonal_matrix(block)
        row.append(D)
      self.matrix_nest.append(row)
    return self.matrix_nest
  

##Operation Class
class Operation:
  def __init__(self):
    super().__init__()
    return None

  def multiplication(self,matA,matB):
    result = []
    for i in range(len(matA)):
      rowsofzeros = [0] * len(matB[0])
      result.append(rowsofzeros)

    for i in range(len(matA)):  
      for j in range(len(matB[0])): 
        for k in range(len(matB)): 
            result[i][j] += matA[i][k] * matB[k][j]
    # Result of multiplication
     
    return result

  def inverse(self,matA):
    z = [] 
    inverse = []

    n = len(matA)
    #initialize zero matrix
    for i in range(n):
      zero = [0] *n
      inverse.append(zero)

    for i in range(n):
      zero = [0] * 2*n
      z.append(zero)
    ## update full zero matrix with main one
    for i in range(n):
      for j in range(n):
        z[i][j] = matA[i][j]
    #update full matrix's 2nd half with identity matrix
    for i in range(n):
        for j in range(n):
            if i == j:
                z[i][j+n] = 1
    #Guass jordan method
    for i in range(n):
        if z[i][i] == 0.0:
            sys.exit('Inverse cannot be found. Zero division errot occured!')

        for j in range(n):
            if i != j:
                ratio = z[j][i]/z[i][i]

                for k in range(2*n):
                    z[j][k] = z[j][k] - ratio * z[i][k]
      
    for i in range(n):
        divisor = z[i][i]
        for j in range(2*n):
            z[i][j] = round(z[i][j]/divisor, 2)

    #Enter inverse result to the inverse matrix
    for i in range(n):
        for j in range(n):
            inverse[i][j] = z[i][j+n]
    return inverse
    


class custom_matrix(Matrix, Nested_Matrix, Operation):
  def __init__(self):
    super().__init__()
    return None
  #for view any matrix
  def views(self,ip):
    print('Output:')
    for i in range(len(ip)):
      for j in range(len(ip)):
        print(ip[i][j], end='\t')
      print()

##finish code