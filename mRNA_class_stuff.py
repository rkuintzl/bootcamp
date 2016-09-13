import io
import sys
import re
from Bio import SeqIO

def gc_blocks(seq, block_size):
	gc_blocks = []
	seq = seq.upper()
	blocks = partition_blocks(seq,block_size)
	for block in blocks:
		gc = compute_gc_content(block)
		gc_blocks.append((block,gc))
	return gc_blocks

def compute_gc_content(block):
	g = block.count('G')
	c = block.count('C')
	return (g+c)/len(block)

def partition_blocks(seq, block_size):
	blocks = []
	i = 0
	while i+block_size <= len(seq):
		blocks.append(seq[i:i+block_size])
		i+=block_size
	return blocks

def gc_map(seq, block_size, gc_thresh):
	gc_blocks = gc_blocks(seq, block_size)
	output_seq = ""
	for block in gc_blocks:
		(gc,seq) = block
		if gc < gc_thresh:
			output_seq += seq.lower()
		else:
			output_seq += seq
	return output_seq

# Execute code:
mapped_seq = gc_map(seq, block_size, gc_thresh)

class MRNA:
	"""A class defining a protein-coding RNA transcript contains the sequence id, the transcript sequence, and simplistically defines the CDS as the largest open reading frame. It also contains methods to translate the putative CDS to an amino acid sequence."""

	map = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
       "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
       "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
       "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
       "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
       "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
       "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
       "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
       "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
       "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
       "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
       "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
       "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
       "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
       "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
       "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",}

	def __init__(self,iid,iseq):
		"""Constructor for mRNA class"""
		self.id = iid
		self.seq = cleanup(iseq)

	def start_codon_pos(self):
		startIndexes = list()
		assert 'AUG' in self.seq,"Your DNA sequence doesn't have a start codon."
		length = len(self.seq)
		for i in xrange(1,length):
			triplet = self.seq[i:i+3]
			if triplet == 'AUG':
				startIndexes.append(i)
		return startIndexes

	def get_ORFs(self):
		print ("***Retrieving open reading frames***")
		startIndexes = self.start_codon_pos()
		orfs = list()
		for startPos in startIndexes:
			j = startPos
			while j+3 <= len(self.seq):
				codon = self.seq[j:j+3]
				if is_stop_codon(codon):
					# Retrieve the sequence from the start position to the end of the stop codon:
					orf = self.seq[startPos:j+3]
					orfs.append(orf)
				j+=3
		return orfs # A list of sequences (strings)

	def getCDS(self):
		"""Reports a putative CDS, the longest ORF"""
		maxLen = 0.0
		cds = ""
		orfList = self.get_ORFs()
		for seq in orfList:
			if len(seq) > maxLen:
				maxLen = len(seq)
				cds = seq
		assert cds != "", "I found no open reading frames for "+self.id
		return cds # A single string

	def translate(self):
		print ("***Attempting to translate mRNA***")
		protein = ""
		cds = self.getCDS()
		print "I found a putative CDS:", cds
		j = 0
		while j+3 <= len(cds):
			codon = cds[j:j+3]
			aminoAcid = MRNA.map[codon]
			if aminoAcid != 'STOP':
				protein = protein + aminoAcid
			j+=3

		return protein # A string of amino acids



def cleanup(sequence):
	clean_sequence = sequence.upper().replace('T','U')
	return clean_sequence

def is_stop_codon(codon):
	assert len(codon) == 3, "A codon should be three bases long. You passed this function a sequence of length" + len(codon) + "."
	if codon == "UAG" or codon == "UAA" or codon == "UGA":
		return True
	return False

def getSequences_from_fasta(input_file):
	"""Given the filename for a fasta file, returns a dictionary mapping defline IDs to sequence objects."""

	IDs_to_seqs = dict() # Declare a new dictionary

	handle = open(input_file, "rU") # Why "rU"?
	for record in SeqIO.parse(handle, "fasta"):
		IDs_to_seqs[record.id] = str(record.seq) # Need str?
	handle.close()

	return IDs_to_seqs


#############################################
## Begin "executable" portion of code here ##
#############################################

IDs_to_seqs = getSequences_from_fasta("mRNAs.fasta")

for id in IDs_to_seqs.keys():
	seq = IDs_to_seqs[id]
	new_mRNA = MRNA(id,seq)
	protein = new_mRNA.translate()
	print ">"+id+"_protein","\n",protein
