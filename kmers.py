def kmer2str(val, k):
    """ Transform a kmer integer into a its string representation
    :param int val: An integer representation of a kmer
    :param int k: The number of nucleotides involved into the kmer.
    :return str: The kmer string formatted
    """
    letters = ['A', 'C', 'T', 'G']
    str_val = []
    for i in range(k):
        str_val.append(letters[val & 0b11])
        val >>= 2

    str_val.reverse()
    return "".join(str_val)




def encode(letter):
    #letters={'A':0, 'C':1, 'T': 2, 'G':3}
    letters = ['A', 'C', 'T', 'G']
    
    return letters.index(letter)

   
text='AGGTC' 

k=2   

def mask(k):
    return( (1<< 2*(k-1))-1)


def stream_kmers(text, k):

    #encodage de la 1ere lettre:
    kmer=0
    for i in range (k-1):
        #print(kmer)
        kmer=kmer<<2
        kmer=kmer+ encode(text[i])
        print(kmer)
        
    #encodage du reste du text:
    list_kmer=[]
    for i in text[k-1:]:
        kmer=kmer & mask(k)
        kmer=kmer<<2
        kmer+=encode(i)
        print(kmer)
        #rkmer=kmer
        #rkmer=rkmer>>2
        
        list_kmer.append(kmer)
        
    return list_kmer




a=stream_kmers('TGTA', 3)
print (a)
for j in a:
    print(kmer2str(j, k))
