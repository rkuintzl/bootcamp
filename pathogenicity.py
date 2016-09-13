import io
import sys


def gc_blocks(seq, block_size):
	"""Returns an array of tuples with substring blocks and their GC content"""
	gc_blocks_list = []
	seq = seq.upper()
	blocks = partition_blocks(seq,block_size)
	for block in blocks:
		gc = compute_gc_content(block)
		gc_blocks_list.append((block,gc))
	gc_blocks_tuple = tuple(gc_blocks_list)
	return gc_blocks_tuple


def compute_gc_content(block):
	"""Computes GC content of a string of any length"""
	g = block.count('G')
	c = block.count('C')
	return (g+c)/len(block)


def partition_blocks(seq, block_size):
	"""Breaks a sequence into blocks of specified length"""
	blocks = []
	i = 0
	while i+block_size <= len(seq):
		blocks.append(seq[i:i+block_size])
		i += block_size
	return blocks


def gc_map(seq, block_size, gc_thresh):
	"""Annotates input sequences by GC content with capitalization"""
	gc_blocks_tuple = gc_blocks(seq, block_size)
	output_seq = ""
	for block in gc_blocks_tuple:
		(seq,gc) = block
		if gc < gc_thresh:
			output_seq += seq.lower()
		else:
			output_seq += seq
	return output_seq


def read_fasta(fasta_file):
	"""Given the filename for a fasta file, returns a dictionary mapping defline IDs to sequence objects."""

	seq_dict = dict() # Declare a new dictionary

	with open(fasta_file,'r') as f:
		lines = f.readlines()
		defline = ""
		for li in lines:
			li = li.rstrip() # remove newlines
			if '>' in li:
				defline = li # if i use 'id' it is blue; why?
				seq_dict[defline] = ""
			else:
				seq_dict[defline] += li

	return seq_dict


#############################################
## Begin "executable" portion of code here ##
#############################################

print("Usage: <fasta file> <block size (integer)> <gc content threshold>")

fasta = sys.argv[1]
block_size = int(sys.argv[2])
gc_thresh = float(sys.argv[3])

# line size for printing:
line_size = 60

seq_dict = read_fasta(fasta)

# Write new fasta file with GC island annotations
with open("sequences_out.fasta","w") as f_out:
	for defline in seq_dict.keys():
		seq = seq_dict[defline]
		mapped_seq = gc_map(seq, block_size, gc_thresh)
		f_out.write(defline+"\n")

		i = 0
		while(i<len(mapped_seq)):
			if i+line_size < len(mapped_seq):
				seq_block = mapped_seq[i:i+line_size]
				f_out.write(seq_block+"\n")
			else:
				seq_block = mapped_seq[i:]
			i+=line_size
