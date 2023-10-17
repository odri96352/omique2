from Bio import SeqIO
import cProfile


def asciiDC3 (seq) :
    asc=[]
    for i in seq :
        asc.append(ord(i))

    return asc+[0,0,0]
def position1_2 (asc):
    ind1=[]
    ind2=[]
    for k in range(len(asc)-2):  #attention on a peut etre fait de la merde ici, pas sure du -2
        if k%3==1 :
            ind1.append(k)
        if k%3==2:
            ind2.append(k)
    return ind1+ind2
def radix (p, t):
    r=[]
    for i in range(len(p)):
        index=p[i]
        r.append([t[index],t[index+1], t[index+2]])
    return r
def alphabetT(T):
    ### à changer pcq c laid
    dic={}
    a=[]
    for i in range(len(T)):
        a.append(T[i])
    a.sort() ## MDR CE SORT EST A CHANGER SERGIO VA NOUS TUER

    for element in a:
        if not (element in dic):
            dic[element]=len(dic)
    print("coucou")
    return dic
def sort(array,index, alphabet, columnNumber):
    print("array")
    print(array)
    print("alphabet")
    print(alphabet)
    if len(array) == 0:
        return array

  # Perform counting sort on each column, starting at the last

    column = columnNumber
    while column>=0: # nous on met "tant que l'indice est supérieur à 3"
        array, index = countingSortByDigit(array,index, alphabet, column)
        column-=1 #change de colonne dans ton tableau

    return array, index
def countingSortByDigit(array, index, alphabet, column):
    """
    ici possibleNumbers= nombre de chiffres possibles. Nous n'avons que 4 nombres (0,97,98,99)
    """

    countIndex = -1
    count = [0] * len(alphabet)
    output = [None] * len(array)
    outputIndex= [0] * len(array)

  # Count frequencies
    for i in range(0, len(array)):
        #print("i "+str(i))
        #print("array[i] "+ str(array[i]))
        #print("column "+str(column))

        countIndex = alphabet[array[i][column]]
        count[countIndex] += 1

  # Compute cumulates
    for i in range(1, len(alphabet)):
        count[i] += count[i - 1]

  # Move records
    for i in range(len(array) - 1, -1, -1):
        countIndex = alphabet[array[i][column]]
        count[countIndex] -= 1
        output[count[countIndex]] = array[i]
        outputIndex[count[countIndex]]=index[i]

    return output, outputIndex
def ordre(R):
    # nous renovie la liste order du genre (1,2,2,3,4,4,5)  et un booléen indiquant s'il y a répétition
    index=1
    repetition=False
    ordre=[1]
    for i in range(1, len(R)):
        if R[i-1]==R[i] :
            ordre.append(index)
            repetition=True
        else :
            index+=1
            ordre.append(index)

    return ordre, repetition
def Tprime(ordre, p12, index):
    t=[]
    for p in p12:
        for i in range(len(index)):
            if index[i]==p :
                t.append(ordre[i])
    return t

def resumeHigherOrder(index012prime, P12):
    output=[]
    for element in index012prime:
        output.append(P12[element])

    return output
def position0_R0(T, index12):
    #attention T se finit avec trois 0
    position=[]
    R=[]
    for i in range(len(T)-3): #on ne prend pas en compte les trois 0 sentinelle
        if i%3==0:
            position.append(i)
            for k in range(len(index12)):
                if index12[k]==i+1:
                    R.append([T[i],k+1])
    return position, R
def alphabetR0(R0):
    ### à changer pcq c laid
    dic={}
    a=[]
    for column in range(2):
        for i in range(len(R0)):
            a.append(R0[i][column])
    a.sort() ## MDR CE SORT EST A CHANGER SERGIO VA NOUS TUER

    for element in a:
        if not (element in dic):
            dic[element]=len(dic)
    return dic
def merge(Tfinal, index_0, index12) :
    liste=[]
    A=0
    B=0
    while A<len(index_0) and B<len(index12):
        #print("rentre dans le while")
        a=index_0[A]
        b=index12[B]
        if Tfinal[a]!=Tfinal[b] :
            minimum=min(Tfinal[a], Tfinal[b])

            if minimum == Tfinal[a]:
                #print("a= "+str(a)+", b= "+str(b)+", on append le "+str(a))
                A+=1
                liste.append(a)
            else:
                #print("a= "+str(a)+", b= "+str(b)+", on append le "+str(b))
                B+=1
                liste.append(b)

        else :
            if b%3==1 :
                #print(str(b)+" est congru à 1 modulo 3")
                longueur=len(liste)
                i=0
                while longueur==len(liste):
                    #print("index12")
                    #print(index12)
                    #print("a= "+str(a)+", b= "+str(b))
                    if a+1==index12[i]:
                        #print(str(a+1)+" apparait en premier dans index12")
                        liste.append(a)
                        A+=1
                    elif b+1==index12[i]:
                        #print(str(b+1)+" apparait en premier dans index12")
                        liste.append(b)

                        B+=1
                    else:
                        i+=1


            elif b%3==2 :
                #print(str(b)+"est congru à 2 modulo 3")
                if Tfinal[a+1]!=Tfinal[b+1] :
                    minimum=min(Tfinal[a], Tfinal[b])
                    if minimum == Tfinal[a]:
                        A+=1
                        liste.append(a)
                    else:
                        B+=1
                        liste.append(b)

                else:
                    for element in index12:
                        if a+2==element:
                            liste.append(a)
                            A+=1
                        elif b+2==element:
                            liste.append(b)
                            B+=1

        #print("A "+str(A))
        #print("B "+str(B))
        if A==len(index_0):
            for i in range(B, len(index12)):
                liste.append(index12[i])
        if B==len(index12):
            for i in range(A, len(index_0)):
                liste.append(index_0[i])

    return liste
def removesentinel(index):
    return index[1:]

def almost_dc3(T):
    # T est une liste de int
    columnNumber=2
    p12=position1_2(T)
    r12=radix(p12,T)
    alphabet_T=alphabetT(T)
    r12sorted, index12=sort(r12, p12, alphabet_T, columnNumber)
    order12,repetition=ordre(r12sorted)
    if repetition:
        Tprim=Tprime(order12, p12, index12)+[0,0,0]
        index012=almost_dc3(Tprim)
        index12=resumeHigherOrder(index012, p12)
    p0,r0=position0_R0(T, index12)
    alphabet_r0=alphabetR0(r0)
    r0sorted, index0=sort(r0,p0,alphabet_r0 ,columnNumber-1)
    order0=ordre(r0sorted)
    index012=removesentinel(merge(T, index0, index12))
    return index012




def parseFile(name, type,dollar=False):
    #parses a given file of a given data structure
    #returns a list of every sequence as a SEQIO object
    #and counts how much nucleotide the lists contains in total
    sequence=[]
    count=0
    for seq_record in SeqIO.parse(name, type):
        if dollar:
            seq_record.seq+="$" #adding a dollar for BW
            sequence.append(seq_record)
        else:
            sequence.append(seq_record)
        count+=len(seq_record.seq)
    return sequence, count


if __name__=="__main__":
    #genome, nucleotide_genome=parseFile("/home/azarkua/Documents/2023-2024/omiques2/developement/omique2/genome.fna", "fasta")
    #reads,nucleotide_reads=parseFile("/home/azarkua/Documents/2023-2024/omiques2/developement/omique2/reads.fq", "fastq")
    # la consigne nous recommande de réfléchir à une structure de donnée adéquate ...

    #temp=reads[1].seq.upper()
    temp="TATATCTTTAAAATGATGTTGCAAATTTATTGAACATGTTAATAAATCATCCTGTTCATTTTGTATGTCTACTAAATTATGTAACGTATCCTCTTCTTCA"
    temp[50:60]
    T=asciiDC3(temp)
    cProfile.run("almost_dc3(temp)")
    print(almost_dc3(T)[:100])
