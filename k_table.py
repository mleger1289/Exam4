# Reads text file and shows users the data inside for processing puposess
with open('sampledna.txt') as f:
    lines = f.readlines()
# print lines to be tested
    print(lines)

# Panda Table
def k_table(input,k):
  # Args:
        # "input": DNA string to be reviewed, number of kmers (k): substring length 
                
    # Returns:
        # data_f: Table of possible and observed kmers for each k value
    
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

            for i in range(0 , k):
                k_num.append(i+1)
                kmer_1 = len(input)- i 
                kmer_2 = 4**(i+1)
                possible_kmers =min(kmer_1,kmer_2)
                p_kmers.append(possible_kmers)

                kFreq = {}
                for j in range(0,len(input)-i):
                    kFreq[input[j:j+i+1]]=[]
                    olist=len(kFreq)
                o_kmers.append(len(kFreq))

            import pandas as Panda_table
            column = {'K':k_num,'Observed kmers':o_kmers,'Possible kmers':p_kmers}
            data_f = Panda_table.DataFrame(data=column)
            # Removes blank coloumn on right side of table
            blankIndex=[''] *len(data_f)
            data_f.index=blankIndex
            return(data_f)
