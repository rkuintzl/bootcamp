import pytest
import tdd_test_driven_dev as tdd
import bootcamp_utils as bc_utils

def test_find_codon():

    mrna_dict = bc_utils.read_fasta('synaptobrevin_mrna.fa')
    protein_dict = bc_utils.read_fasta('synaptobrevin_protein.fa')

    for seq_id in mrna_dict.keys():

        mrna_seq = mrna_dict[seq_id]
        if not seq_id in protein_dict.keys():
            raise RuntimeError('Your protein defline must match your mRNA defline')
        protein_seq = protein_dict[seq_id]

        assert tdd.find_codon_lesson6('TGG', mrna_seq, protein_seq) == 1
        assert tdd.find_codon_lesson6('ATG', mrna_seq, protein_seq) == 0
        assert tdd.find_codon_lesson6('AGA', mrna_seq, protein_seq) == 4
        assert tdd.find_codon_lesson6('TGT', mrna_seq, protein_seq) == -1
        assert tdd.find_codon_lesson6('TGA', mrna_seq, protein_seq) == -1
        pytest.raises(RuntimeError, "tdd.find_codon_lesson6('AA', mrna_seq, protein_seq)")
        pytest.raises(RuntimeError, "tdd.find_codon_lesson6('ZZZ', mrna_seq, protein_seq)")

    return None
