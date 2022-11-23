'''
 # @ Author: AME Jacky
 # @ Creation: 2022-11-23 13:50:18
'''

class Read:
    # CONSTRUCTEUR
    def __init__(self, sequence = ""):
        if sequence != "":
            self.seq = sequence.upper()
            self.lseq = len(self.seq)
        else:
            self.seq = sequence
            self.lseq = 0

    # ACCESSEURS
    def get_seq(self):
        return(self.seq)

    def get_lseq(self):
        return(self.lseq)

    # MUTATEURS
    def set_seq(self, new_seq):
        self.seq = new_seq

    def set_lseq(self, new_L):
        self.lseq = new_L

    # METHODES
    def validate_dna_seq(self) -> bool:
        """
        Checks DNA sequences for incorrect characters.
        Anything else than A,T,G and C is considered incorrect.
        Args:
            seq (str): a DNA read
        Raises:
            Exception: sequence is empty
            TypeError: sequence is not a string
            Exception: incorrect character detected
        Returns:
            bool: sequence validity
        """
        if self.get_lseq() == 0:
            return False
        seq = self.get_seq()
        if seq == "":
            raise Exception("Sequence is empty.")
        if not isinstance(seq, str):
            raise TypeError("Sequence is not readable (must be a string).")

        for nuc in seq:  # check for unwanted character
            if nuc not in 'ATGC':
                raise Exception("Incorrect character detected.")
        return True

    def count_nucleotides(self) -> dict:
        """
        Create a dictionary to count nucleotides in the read sequence

        Returns:
            counts_nuc_dict (dict): {'A': 0, 'C': 0, 'G': 0, 'T': 0}
        """
        seq = self.get_seq()
        counts_nuc_dict = {nuc:seq.count(nuc) for nuc in 'ACGT'}
        return counts_nuc_dict

    # SURCHARGE METHODE __str__
    def __str__(self):
        counts_nuc_dict = self.count_nucleotides()
        s = "***** Read *****\n"
        s += "Sequence : \n" + str(self.get_seq()) + "\nLongueur :  \n" + str(self.get_lseq()) + "\n"
        s += "Number of nucleotides : \n"
        for key, value in counts_nuc_dict.items():
            s += key + " : " + str(value) + "\n"
        s += "\n"
        return(s)

if __name__ == "__main__":
    # INSTANCES
    read1 = Read("ATGTCTGTAGTGTCCTAGTCTGA")
    read2 = Read("cgtAt")
    read3 = Read("FHT")
    # DISPLAY
    print(read1)
    print(read2)
    print(read1.validate_dna_seq())
    print(read1.count_nucleotides())
    print(read2.validate_dna_seq())
    print(read2.count_nucleotides())
    print(read3.validate_dna_seq())
    print(read3.count_nucleotides())