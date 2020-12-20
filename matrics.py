# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 00:00:48 2020

@author: nahid
"""

import py_matrix as mt
obj1 = mt.custom_matrix()
matA = obj1.nested_matrix(3)

print("Nested matrix:")
obj1.views(matA)
