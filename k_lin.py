# Reads text file and shows users the data inside for processing puposess
with open('sampledna.txt') as f:
    lines = f.readlines()
# print lines to be tested
    print(lines)


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
        
    return (k_lin)


