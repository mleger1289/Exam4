#!/usr/bin/env python3

# All Functions for exam 4

def p_kmers(input, k):  
  ### Checks for possible kmers within a string input
    
    # Args:
        # "input": DNA string to be reviewed, number of kmers (k): substring length 
                
    # Returns:
        # possible_kmers: Number of Observed kmers in the given string for a given substring length
    
    # Creating input validation criteria that will error and stop the script if invalid entries are entered.
    
    #possible_kmers = 0
    e = 0
    for i in range(len(input)):
        if input[i] !='A'and input[i] !='G' and input[i] !='C' and input[i] !='T':
            e = 1
            break
    if k%1 != 0 or k<=0 or k>len(input):
        print('K value is Invalid. An integer between one and the length of the input is required.')

    elif e ==1 or len(input)==0:
        print('Input is Invalid. Must contain only characters of A, C, G or T')

    else:              
        kmer_1 = len(input)- k + 1
        kmer_2 = 4**k
    
        possible_kmers =min(kmer_1,kmer_2)

        return possible_kmers
       
def o_kmers(input, k):
    ### Checks for observed kmers within a string input
    
    # Args:
        # "input": DNA string to be reviewed, number of kmers (k): substring length 
                
    # Returns:
        # observed_kmers: Number of Observed kmers in the given string for a given substring length
    
    # Creating input validation criteria that will error and stop the script if invalid entries are entered.
    error = 0
    for i in range(len(input)):
        if input[i] !='A'and input[i] !='G' and input[i] !='C' and input[i] !='T':
            error = 1
            break
        if k%1 != 0 or k<=0:
            print('K value is Invalid. An Integer greater than zero is needed')
        elif error ==1 or len(input)==0:
            print('Input is Invalid. Must contain only characters of A, C, G or T')
        else:
            
    # Create a blank dictionary for counting kmer's       
            observed_kmers = {}
    # Checks kmers against dictionary and counts each iteration
            for i in range(0, len(input) - k+1):
                kmer = input[i:i + k]
                if kmer in observed_kmers:
                    observed_kmers[kmer] +=1
                else:
                    observed_kmers[kmer] = 1
    return len(observed_kmers)

# Panda Table
def k_table(input,k):
    ### Adds observed and possible kmers to a table for each k value 1 to length of input 
    
    # Args:
        # "input": DNA string to be reviewed, number of kmers (k): substring length 
                
    # Returns:
        # data_f: Table of each k value with observed and possible kmers in table form
    
    
    # Creating input validation criteria that will error and stop the script if invalid entries are entered.
    error = 0
    for i in range(len(input)):
        if input[i] !='A'and input[i] !='G' and input[i] !='C' and input[i] !='T':
            error = 1
            break
        if k%1 != 0 or k<=0:
            print('K value is Invalid. An Integer greater than zero is needed')
        elif error ==1 or len(input)==0:
            print('Input is Invalid. Must contain only characters of A, C, G or T')
        else:
    
    # Initiate list for each coloumn 
            k_num = []
            p_kmers = []
            o_kmers = []
        # Checks between zero and k vaue to populate table
            for i in range(0 , k):
                k_num.append(i+1)
                kmer_1 = len(input)- i 
                kmer_2 = 4**(i+1)
            # Determines minimum possible kmer equation for each itteration    
                possible_kmers =min(kmer_1,kmer_2)
                p_kmers.append(possible_kmers)
            # Create a blank dictionary for counting kmer's    
                kFreq = {}
            # Adds okerms to the table    
                for j in range(0,len(input)-i):
                    kFreq[input[j:j+i+1]]=[]
                    olist=len(kFreq)
                o_kmers.append(len(kFreq))
            # Creates actual table for viewer to see    
            import pandas as Panda_table
            column = {'K':k_num,'Observed kmers':o_kmers,'Possible kmers':p_kmers}
            data_f = Panda_table.DataFrame(data=column)
            # Removes blank coloumn on right side of table
            blankIndex=[''] *len(data_f)
            data_f.index=blankIndex
            return(data_f)
        
# Linguistic complexity function
def k_lin(input,k):
     ### Finds the linguistic complxity of a DNA string 
    
    # Args:
        # "input": DNA string to be reviewed, number of kmers (k): substring length 
                
    # Returns:
        # k_lin: sum of observed / sum of possible 
    
    
    # Creating input validation criteria that will error and stop the script if invalid entries are entered.
    error = 0
    for i in range(len(input)):
        if input[i] !='A'and input[i] !='G' and input[i] !='C' and input[i] !='T':
            error = 1
            break
        if k%1 != 0 or k<=0:
            print('K value is Invalid. An Integer greater than zero is needed')
        elif error ==1 or len(input)==0:
            print('Input is Invalid. Must contain only characters of A, C, G or T')
        else:
            
            # Initiate list for each coloumn 
            k_num = []
            p_kmers = []
            o_kmers = []
            
            for m in range(0 , k):
                k_num.append(m+1)
                kmer_1 = len(input)- m 
                kmer_2 = 4**(m+1)
                possible_kmers =min(kmer_1,kmer_2)
                p_kmers.append(possible_kmers)          
                kFreq = {}
                for j in range(0,len(input)-m):
                    kFreq[input[j:j+m+1]]=[]
                olist=len(kFreq)
                o_kmers.append(len(kFreq))
        
        k_lin = sum(o_kmers)/sum(p_kmers)
        print(p_kmers,o_kmers)
    return (k_lin)


