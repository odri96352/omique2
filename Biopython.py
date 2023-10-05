from Bio import SeqIO


def parseFile(name, type,dollar=True):
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

def DC3(text):
    return
def BWT(chromosome):
    return

if __name__=="__main__":
    genome, nucleotide_genome=parseFile("/home/azarkua/Documents/2023-2024/omiques2/developement/omique2/genome.fna", "fasta")
    #reads,nucleotide_reads=parseFile("/home/azarkua/Documents/2023-2024/omiques2/developement/omique2/reads.fq", "fastq")
    # la consigne nous recommande de réfléchir à une structure de donnée adéquate ...
    print(genome[0].seq)
