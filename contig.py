'''
 # @ Author: AME Jacky
 # @ Creation: 2022-11-23 15:50:26
 '''
class Contig:
    # CONSTRUCTEUR
    def __init__(self, seq_contig = ""):
        if seq_contig != "":
            self.contig = seq_contig
            self.lcontig = len(self.contig)
            self.compteur = 1
        else:
            self.contig = seq_contig
            self.lcontig = 0
            self.compteur = 1

    # ACCESSEURS
    def get_contig(self):
        return(self.contig)

    def get_lcontig(self):
        return(self.lcontig)

    def get_compteur(self):
        return(self.compteur)

    # MUTATEURS
    def set_contig(self, new_contig):
        self.contig = new_contig

    def set_lcontig(self, new_Lcontig):
        self.lcontig = new_Lcontig

    def set_compteur(self, new_compt):
        self.compteur = new_compt

    # METHODES
    def fasta_format(self):
        s = ">contig\n"
        i = 0
        for elt in self.get_contig():
            if i == 60:
                s+='\n'
                i = 0
            s += str(elt)
            i+=1
        return(s)

    def next_read(self, list_reads):
        maxi = 0
        i = 0
        index = 0
        for elt in list_reads:
            score = elt.best_overlap()
            if score > maxi :
                maxi = score
                index = i
            i += 1
        if maxi < 8 :
            return (-1)
        else :
            return (index)

    # SURCHARGE METHODE __str__
    def __str__(self):
        s = "***** Contig *****\n"
        s += "Contig : \n" + str(self.get_contig()) + "\nLongueur contig :  \n" + str(self.get_lcontig()) + "\n"
        s += "Compteur : \n" + str(self.get_compteur()) + "\n"
        return(s)

if __name__ == "__main__":
    # INSTANCES
    contig1 = Contig("ATGTCTATGATGATGTAGTAGTAGTAGTATGATGATGATGTAGTATGATGATGTATGATGATGTATGATGATGATGTAGTAGTATGGTATGATATGTCTATGATGATGTAGTAGTAGTAGTATGATGATGATGTAGTATGATGATGTATGATGATGTATGATGATGATGTAGTAGTATGGTAT")
    contig2 = Contig("cgtAt")
    contig3 = Contig("FHT")
    print(contig1)
    print(contig2)
    print(contig1.fasta_format())
