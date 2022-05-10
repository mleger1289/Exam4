# Reads text file and shows users the data inside for processing puposess
with open('sampledna.txt') as f:
    lines = f.readlines()
# print lines to be tested for user to manual add to functions
    print(lines)
    
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

            for i in range(0, len(input) - k+1):


                kmer = input[i:i + k]

                if kmer in observed_kmers:
                     observed_kmers[kmer] +=1
                else:
                     observed_kmers[kmer] = 1
                
    return len(observed_kmers)



