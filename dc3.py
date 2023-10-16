def position1_2_0_ascii_alphabet (seq):
        """
        Return a list of the ascii equivalent of each element of the list in argument
        adding the three sentinel zeroes at the end

        and returns positions congruent to 1 and 2 modulo 3 in seq
        and returns positions congruent to 0 modulo 3 in seq

        and returns list of triplets starting from indexes not multiple of 3
        and returns list couples in the form [nucleotide multiple of 0, rank of the next nucleotide]

        and returns

        Parameter
        ---------
        seq: list of str
            List of our nucleotides

        Returns
        -------
        asc: list of int
                    List of ascii equivalent of nucleotides + sentinel sequence
        p1+p2: list of int
                List of positions congruent to 1 and 2 modulo 3
        p0: list of int
            List of positions congruent to 0 module 3
        r1+r2: list of triplets (triplet: list of int)
                List of three numbers starting for indexes of p1+p2
        r0: list of couples (couple: list of in t)
            List of couples in the form [nucleotide multiple of 0, rank of the next nucleotide]
        alphabetr12: Dictionnary
                    Every key is a position of seq not multiple of 3
                    every value is its order compared to the other keys.
        alphabetr0:Dictionnary
                Every key is a position of seq multiple of 3
                every value is its order compared to the other keys.
        """
        p1,p2=[],[]
        p0=[]
        r1,r2=[],[]
        r0=[]
        asc=[]
        dic12={}
        dic0={}
        alphabetr12={}
        alphabetr0={}

        for k in range(len(seq)):
            #print("k boucle 1 "+str(k))
            asc.append(ord(seq[k]))
            # dic nous sert à entreposer tous les types d'éléments qu'on trouve dans asc
            # on utilise un dictionnaire pour rendre l'opération (element is in dic) rapide
            if (k%3==1 and k+2<len(seq)):
                p1.append(k)
                add_triplet(seq, k, r1)
                update_dictionnary_of_r12(seq,k,dic12)
            elif (k%3==2 and k+2<len(seq)):
                p2.append(k)
                add_triplet(seq, k, r2)
                update_dictionnary_of_r12(seq,k,dic12)
            elif (k%3==0 and k+1<len(seq)):
                p0.append(k)
                add_couple_r0(seq, k, k+2, r0)
                update_dictionnary_of_r0(seq, asc,k,k+2, dic0)
            elif (k%3==0 and k+1>=len(seq)-1):
                p0.append(k)
                add_couple_r0(seq, k, 1, r0)
                update_dictionnary_of_r0(seq, asc,k,1, dic0)

        # we add the sentinel sequence to asc
        asc+=[0,0,0]
        # we now finish our previous algorithm
        for k in range(len(asc)-5,len(asc)):
            #print("k boucle 2 "+str(k))
            if (k%3==1 and k+2<len(asc)):
                p1.append(k)
                add_triplet_ascii(asc, k, r1)
                update_dictionnary_of_r12_ascii(asc,k,dic12)
            elif (k%3==2 and k+2<len(asc)):
                p2.append(k)
                add_triplet_ascii(asc, k, r2)
                update_dictionnary_of_r12_ascii(asc,k,dic12)
        # create alphabet of triplets that are not multiples of 3
        alphabetr12=alphabet(dic12)
        # create alphabet for liste of positions multiples of 3 and the next item rank
        alphabetr0=alphabet(dic0)
        return p1+p2, p0, asc, r1+r2, r0, alphabetr12, alphabetr0

def add_triplet(sequence, position, listOfTriplets):
    """
    Appends the triplet
    [nucleotide that is not multiple of 3 in "position"-th position,
    the next nucleotide in "sequence",
    the second next nucleotide in "sequence"]
    to "listOfTriplets".

    Parameter
    ---------
    sequence: list of str
            Sequence of nucleotides
    position: int
            Position of the nucleotide multiple of 3
    listOfTriplets: list of triplets (triplet: list of int)
                List we are modifying.

    Returns
    -------
    None
    But the parameter "listOfTriplets" has changed.
    """

    listOfTriplets.append([ord(sequence[position]),ord(sequence[position+1]),ord(sequence[position+2])])
    return

def add_triplet_ascii(asciisequence, position, listOfTriplets):
    """
    Appends the triplet
    [nucleotide that is not multiple of 3 in "position"-th position,
    the next nucleotide in "sequence",
    the second next nucleotide in "sequence"]
    to "listOfTriplets".

    Parameter
    ---------
    asciisequence: list of str
                Sequence of nucleotides in ascii code
    position: int
            Position of the nucleotide multiple of 3
    listOfTriplets: list of triplets (triplet: list of int)
                List we are modifying.

    Returns
    -------
    None
    But the parameter "listOfTriplets" has changed.
    """
    listOfTriplets.append([asciisequence[position],asciisequence[position+1],asciisequence[position+2]])
    return

def add_couple_r0(sequence, position, rankOfNextItem, listOfCouples):
    """
    Appends the couple [nucleotide in "position"-th position, rank of the next nucleotide]
    to "listOfCouples".

    Parameter
    ---------
    sequence: list of str
            Sequence of nucleotides
    position: int
            Position of the nucleotide multiple of 3
    listOfCouples: list of couple (couple: list of int)
                List we are modifying.

    Returns
    -------
    None
    But the parameter "listOfCouples" has changed.
    """

    listOfCouples.append([ord(sequence[position]),rankOfNextItem])
    return

def update_dictionnary_of_r12(sequence, position, dictionnary):
    """
    adds in "dictionnary" the positions of:
    -nucleotide that is not multiple of 3 in "position"-th position
    -the next nucleotide in "sequence"
    -the second next nucleotide in "sequence"

    Parameter
    ---------
    sequence: list of str
            Sequence of nucleotides
    position: int
            Position of the nucleotide not multiple of 3
    dictionnary: dict
                Dictionnary we are modifying

    Returns
    -------
    None
    But the parameter "dictionnary" has changed.
    """
    if not (ord(sequence[position]) in dictionnary):
            dictionnary[ord(sequence[position])]=0
    if not (ord(sequence[position+1]) in dictionnary):
            dictionnary[ord(sequence[position+1])]=0
    if not (ord(sequence[position+2]) in dictionnary):
            dictionnary[ord(sequence[position+2])]=0
    return

def update_dictionnary_of_r12_ascii(asciisequence, position, dictionnary):
    """
    adds in "dictionnary" the positions of:
    -nucleotide that is not multiple of 3 in "position"-th position
    -the next nucleotide in "sequence"
    -the second next nucleotide in "sequence"

    Parameter
    ---------
    asciisequence: list of str
            Sequence of nucleotides in ascii code
    position: int
            Position of the nucleotide not multiple of 3
    dictionnary: dict
                Dictionnary we are modifying

    Returns
    -------
    None
    But the parameter "dictionnary" has changed.
    """
    if not (asciisequence[position] in dictionnary):
            dictionnary[asciisequence[position]]=0
    if not (asciisequence[position+1] in dictionnary):
            dictionnary[asciisequence[position+1]]=0
    if not (asciisequence[position+2] in dictionnary):
            dictionnary[asciisequence[position+2]]=0
    return

def update_dictionnary_of_r0(sequence, asciisequence, position,rankOfNextItem, dictionnary):
    """
    adds the positions of nucleotides that are multiples of 3 and the rank of the next nucleotides
    as keys in our dictionnary.

    Parameter
    ---------
    sequence: list of str
            Sequence of nucleotides
    asciisequence: list of int
                  Ascii equivalent of our sequence of nucleotides
    position: int
            Position of the nucleotide
    dictionnary: dict
                Dictionnary we are modifying

    Returns
    -------
    None
    But the parameter "dictionnary" has changed.
    """
    if not (asciisequence[position] in dictionnary):
            dictionnary[asciisequence[position]]=0

    if not (rankOfNextItem in dictionnary):
            dictionnary[rankOfNextItem]=0

    return

def alphabet(inputdic):
    """
    Returns a dictionnary. The keys are the elements of "inputdic" sorted and the values
    are the order of the key compared to the other keys.
    example: alphabet({7:0,6:0, 8:0})={6:1,7:2,8:3}

    Parameter
    ---------
    inputdic: dictionnary
            The keys should be the letters we want out alphabet to have. The values have no importance

    Returns
    -------
    output: dictionnary
            Every key has a value representing its order compared to the other keys.

    """
    output={}
    templist=list(inputdic.keys())
    templist.sort()
    for element in templist:
        output[element]=len(output)
    return output

# def countingSortByDigit2point0(array, index, alphabet, column):
#     """
#     Counting Sort
#     Returns a list containing the lists of "array" sorted
#     according to the element in the "column"-th column
#     and a list of indexes of the elements of "array", that are also sorted according
#     to element in "column"-th column
#
#     Parameter
#     ---------
#     array: list of lists of int
#             In our case, array is a list of triplets or of couples
#     index: list of int
#             List of indexes to be sorted
#     column: int
#             Column number of the lists in array, from which we base our sorting on.
#     alphabet: dict
#             Output of the function "alphabet"
#
#     Returns
#     -------
#     output: List of lists
#             Sorted according to element in "column"-th column
#     outputIndex: List of int
#                 Indexes of the elements of "array", that are also sorted according to element in "column"-th column
#     """
#
#     countIndex = -1
#     count = [0] * len(alphabet)
#     output = [None] * len(array)
#     outputIndex= [0] * len(array)
#     key=[] #liste qui contiendra toutes les keys du dictinnaire "countdic" et qu'on va sort
#
#   # Count frequencies
#     for i in range(0, len(array)):
#         print("i "+str(i))
#         print("array[i] "+ str(array[i]))
#         print("column "+str(column))
#         print("array[i] "+ str(array[i]))
#  # Essayer de ne plus utiliser la fonction "alphabet"
#  # au lieu d'être une liste "count" sera un dictionnaire qui prend comme key les valeurs de "array[i][column]"
#         countdict={}
#         if array[i][column] in countdict:
#             countdict[array[i][column]] += 1
#         else:
#             countdict[array[i][column]] = 1
#             key.append(array[i][column])
#     print("countdict")
#     print(countdict)
#     print("key")
#     print(key)
#
#   # Compute cumulates
#     for i in range(1, len(countdict)):
#         count[i] += count[i - 1]
#   # Sort "key"
#     key.sort()
#   # Move records
#     for i in range(len(array) - 1, -1, -1):
#         countIndex=alphabet[array[i][column]]
#         print("countIndex "+str(countIndex))
#         count[countIndex] -= 1
#         print("count[countIndex] "+str(count[countIndex]))
#         output[count[countIndex]] = array[i]
#         outputIndex[count[countIndex]]=index[i]
#
#     return output, outputIndex

def countingSortByDigit(array, index, alphabet, column):
    """
    Counting Sort
    Returns a list containing the lists of "array" sorted
    according to the element in the "column"-th column
    and a list of indexes of the elements of "array", that are also sorted according
    to element in "column"-th column

    Parameter
    ---------
    array: list of lists of int
            In our case, array is a list of triplets or of couples
    index: list of int
            List of indexes to be sorted
    column: int
            Column number of the lists in array, from which we base our sorting on.
    alphabet: dict
            Output of the function "alphabet"

    Returns
    -------
    output: List of lists
            Sorted according to element in "column"-th column
    outputIndex: List of int
                Indexes of the elements of "array", that are also sorted according to element in "column"-th column
    """

    countIndex = -1
    count = [0] * len(alphabet)
    output = [None] * len(array)
    outputIndex= [0] * len(array)
    ordre=[] #transforme orde en une liste de tous les entiers et après modifie les chiffres identiques ??

  # Count frequencies
    for i in range(0, len(array)):
        print("i "+str(i))
        print("array[i] "+ str(array[i]))
        print("column "+str(column))

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

def radixSort(array,index, alphabet):
    """
    Radix Sort
    Returns a list containing the lists of "array" sorted
    and a list of indexes of the elements of "array", that are also sorted

    Parameter
    ---------
    array: list of lists of int
            In our case, array is a list of triplets or of couples
    index: list of int
            List of indexes to be sorted
    alphabet: dict
            output of the function "alphabet"

    Returns
    -------
    array: List of lists
            Each element is sorted
    index: List of int
        Indexes of the elements of "array", that are also sorted
    """
    if len(array) == 0:
        return array

    # Perform counting sort on each column, starting at the last

    column = len(array[0])-1
    while column>=0:
        print(alphabet)
        array, index = countingSortByDigit(array,index, alphabet, column)
        column-=1

    return array, index

def ordre(R):
    index=1
    ordre=[1]
    for i in range(1, len(R)):
        if R[i-1]==R[i] :
            ordre.append(index)
            index=index

        else :
            index+=1
            ordre.append(index)

    return ordre



if __name__=="__main__":
    S="abcabcacab"
    print(ascii(0))
    print("1%3="+str(1%3))
    print([1,2]+[3,4])
    print(position1_2_0_ascii_alphabet(S))
    p12, p0, T, r12, r0, alphabetr12, alphabetr0=position1_2_0_ascii_alphabet(S)
    r12sorted, p12sorted=radixSort(r12,p12,alphabetr12)
    print(radixSort(r12,p12,alphabetr12))
