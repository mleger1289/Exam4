#!/usr/bin/env python3

# Test Script for DSP 539 Final Exam
# Import all scripts from the exam 4 folder
from k_total import * 

# Test that checks for correct characters
def test_char():
    assert p_kmers('ATTVGGATT',9) == None

# Test that checks for valid k
def test_k():
    assert p_kmers('ATTTGGATT',len('ATTTGGATT')+1) == None

# Test that checks for valid results
def test_valido1():
    assert o_kmers('ATTTGGATT',1) == 3
def test_valid1():
    assert p_kmers('ATTTGGATT',1) == 4
    
def test_valido2():
    assert o_kmers('ATTTGGATT',2) == 5
def test_valid2():
    assert p_kmers('ATTTGGATT',2) == 8
    
def test_valido3():
    assert o_kmers('ATTTGGATT',3) == 6
def test_valid3():
    assert p_kmers('ATTTGGATT',3) == 7
    
def test_valido4():
    assert o_kmers('ATTTGGATT',4) == 6  
def test_valid4():
    assert p_kmers('ATTTGGATT',4) == 6
    
def test_valido5():
    assert o_kmers('ATTTGGATT',5) == 5
def test_valid5():
    assert p_kmers('ATTTGGATT',5) == 5
    
def test_valido6():
    assert o_kmers('ATTTGGATT',6) == 4
def test_valid6():
    assert p_kmers('ATTTGGATT',6) == 4
    
def test_valido7():
    assert o_kmers('ATTTGGATT',7) == 3
def test_valid7():
    assert p_kmers('ATTTGGATT',7) == 3
    
def test_valid8():
    assert p_kmers('ATTTGGATT',8) == 2  
def test_valido8():
    assert o_kmers('ATTTGGATT',8) == 2
    
def test_valid9():
    assert p_kmers('ATTTGGATT',9) == 1  
def test_valido9():
    assert o_kmers('ATTTGGATT',9) == 1     

#  Test that checks for valid linqustics 
def test_lin():
    assert k_lin('ATTTGGATT',9)== 0.875
def test_lin2():
    assert k_lin('ATCG',1) == 1