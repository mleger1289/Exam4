def p_kmers(input, k):  
  ### Checks for possible kmers within a string input
    
    # Args:
        # "input": DNA string to be reviewed, number of kmers (k): substring length 
                
    # Returns:
        # possible_kmers: Number of Observed kmers in the given string for a given substring length
    
    # Creating input validation criteria that will error and stop the script if invalid entries are entered.
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
       