"""
*Program 8 : DNA
*Programmer: Chandler Kilpatrick
*Due: 11/18/19
*CS 3A, Fall 2019
*Description: This program will deconstruct and analyze dna sequences.
"""


print("This program reports information about DNA "+ "\n"+
      "nucleotide sequences that may encode proteins.")
file_name = input("Please enter a File name: ")
open_file = open(file_name, "r")
new_file = input("Please enter a File name to store output: ")
open_new_file = open(new_file, "w")
open_new_file.close()

seq_data = []

# Constants
CONST_min_codons = 5
CONST_min_cg_perc = 30
CONST_num_nuc = 4
CONST_nuc_per = 3

# This for loop opens the desired file to be read.
for line in open_file:
    seq_data.append(line)

# This function counts the number of times a letter appears.    
def get_counts(chain):
    counts = [0] * CONST_num_nuc
    for letter in chain:
        if letter.upper() == "A":
            counts[0] = counts[0] + 1

        elif letter.upper() == "C":
            counts[1] = counts[1] + 1

        elif letter.upper() == "G":
            counts[2] = counts[2] + 1

        elif letter.upper() == "T":
            counts[3] = counts[3] + 1
    return counts

# This function counts the number of times a '-' is read.
def get_junk_count(chain):
    junk_count = 0
    for letter in chain:
        if letter == '-':
            junk_count += 1
    return junk_count

# This function calculates the mass of the sequence.       
def get_total_mass(counts, junk_count):
    return (counts[0] * 135.128 + counts[1] * 111.103 +
    counts[2] * 151.128 + counts[3] * 125.107 + junk_count * 100)

# This function calulates the percentage of each letter.
def get_percentages(count, mass_total):
    value = [0, 0, 0, 0]
    value[0] = count[0] * 135.128 / mass_total * 100
    value[1] = count[1] * 111.103 / mass_total * 100
    value[2] = count[2] * 151.128 / mass_total * 100
    value[3] = count[3] * 125.107 / mass_total * 100
    return value 

# This function breaks the given sequence into codons.
def get_codons(sequence):
    codons = []
    letter_count = 0
    codons_holder = ''
    for letter in sequence:
        if letter in "aAcCgGtT":
            letter_count += 1
            codons_holder += letter
        if letter_count == CONST_nuc_per:
            codons.append(codons_holder.upper())
            codons_holder = ''
            letter_count = 0
    return codons

# This function reports the results. 
def report_results(name, sequence, counts, total_mass, percentages,
                   codons, output):
    open_new_file = open(new_file, "a")

    open_new_file.write("Region Name: " + name.strip() + "\n")
    open_new_file.write("Nucleotides: " + str(sequence).strip().upper() + "\n")
    open_new_file.write("Nuc. Counts: " + str(counts).strip() + "\n")
    open_new_file.write("Total Mass%: " + str(percentages) +
                        ' of ' + str(round(total_mass, 1)) + "\n")
    open_new_file.write("Codons List: " + str(codons) + "\n")
    output_ans = ''
    if output == True:
        output_ans = "YES"
    else:
        output_ans = "NO"
    open_new_file.write("Is Protein?: " + output_ans + "\n\n")
    open_new_file.close()
    

# This function determines whether or not a sequence is a protein.
def is_protein(codons, percentages):
    if codons[0] == 'ATG':
        if codons[-1] in ['TAA', 'TAG', 'TGA']:
            if len(codons) >= CONST_min_codons:
                if percentages[1] + percentages[2] >= CONST_min_cg_perc:
                    return True

    
    return False   

# This function rounds all the percentages to 0.1 .
def round1(value):
    percentages = [0, 0, 0, 0]
    percentages[0] = round(value[0], 1)
    percentages[1] = round(value[1], 1)
    percentages[2] = round(value[2], 1)
    percentages[3] = round(value[3], 1)
    return percentages

# I'm not sure what this function should do.
def nuc_index(nucleotide):
    return

for i in range(len(seq_data)):
    if i % 2 != 0:

        name = seq_data[i - 1]

        sequence = seq_data[i]
        
        counts = get_counts(seq_data[i])
        #print(counts)

        seq_list = get_codons(seq_data[i])
        #print(seq_list)
        codons = seq_list

        total_mass = get_total_mass(counts, get_junk_count(seq_data[1]))
        #print(total_mass)

        value = get_percentages(counts, total_mass)
        percentages = round1(value)
        #print(percentages)

        protein_holder = is_protein(seq_list, percentages)
        #print(protein_holder)
        output = protein_holder

        report_results(name, sequence, counts, total_mass, percentages,
                       codons, output)


"""                         MY RUNS

##################################################################

Region Name: cure for cancer protein
Nucleotides: ATGCCACTATGGTAG
Nuc. Counts: [4, 3, 4, 4]
Total Mass%: [27.3, 16.8, 30.6, 25.3] of 1978.8
Codons List: ['ATG', 'CCA', 'CTA', 'TGG', 'TAG']
Is Protein?: YES

Region Name: captain picard hair growth protein
Nucleotides: ATGCCAACATGGATGCCCGATATGGATTGA
Nuc. Counts: [9, 6, 8, 7]
Total Mass%: [30.7, 16.8, 30.5, 22.1] of 3967.5
Codons List: ['ATG', 'CCA', 'ACA', 'TGG', 'ATG', 'CCC', 'GAT', 'ATG', 'GAT', 'TGA']
Is Protein?: YES

Region Name: bogus protein
Nucleotides: CCATT-AATGATCA-CAGTT
Nuc. Counts: [6, 4, 2, 6]
Total Mass%: [35.1, 19.3, 13.1, 32.5] of 2308.1
Codons List: ['CCA', 'TTA', 'ATG', 'ATC', 'ACA', 'GTT']
Is Protein?: NO

Region Name: michael jordan mad hops protein
Nucleotides: ATGAG-ATC-CGTGATGTGGG-AT-CCTA-CT-CATTAA
Nuc. Counts: [9, 6, 8, 10]
Total Mass%: [28.0, 15.3, 27.8, 28.8] of 4342.9
Codons List: ['ATG', 'AGA', 'TCC', 'GTG', 'ATG', 'TGG', 'GAT', 'CCT', 'ACT', 'CAT', 'TAA']
Is Protein?: YES

Region Name: paris hilton phony protein
Nucleotides: ATGC-CAACATGGATGCCCTAAG-ATATGGATTAGTGA
Nuc. Counts: [12, 6, 9, 9]
Total Mass%: [34.0, 14.0, 28.5, 23.6] of 4774.3
Codons List: ['ATG', 'CCA', 'ACA', 'TGG', 'ATG', 'CCC', 'TAA', 'GAT', 'ATG', 'GAT', 'TAG', 'TGA']
Is Protein?: YES

Region Name: jimi hendrix guitar talent protein
Nucleotides: ATGATAATTAGTTTTAATATCAGA-CTGTAA
Nuc. Counts: [12, 2, 4, 12]
Total Mass%: [41.1, 5.6, 15.3, 38.0] of 3949.5
Codons List: ['ATG', 'ATA', 'ATT', 'AGT', 'TTT', 'AAT', 'ATC', 'AGA', 'CTG', 'TAA']
Is Protein?: NO

Region Name: admiral grace murray hopper protein
Nucleotides: ATGC-AATT--GC-----TCGA--------TTAG
Nuc. Counts: [5, 3, 4, 6]
Total Mass%: [28.6, 14.1, 25.6, 31.8] of 2364.1
Codons List: ['ATG', 'CAA', 'TTG', 'CTC', 'GAT', 'TAG']
Is Protein?: YES

Region Name: tyler durden's brain protein
Nucleotides: ATGATACCTATGAGTAATGTGGACCATATCCAAACTATAGGCATTGTCGGACCAACGATCGATTGGTTATACTGA
Nuc. Counts: [24, 14, 16, 21]
Total Mass%: [32.9, 15.8, 24.6, 26.7] of 9843.8
Codons List: ['ATG', 'ATA', 'CCT', 'ATG', 'AGT', 'AAT', 'GTG', 'GAC', 'CAT', 'ATC', 'CAA', 'ACT', 'ATA', 'GGC', 'ATT', 'GTC', 'GGA', 'CCA', 'ACG', 'ATC', 'GAT', 'TGG', 'TTA', 'TAC', 'TGA']
Is Protein?: YES

Region Name: mini me growth hormone
Nucleotides: ATGGGACGCTGA
Nuc. Counts: [3, 2, 5, 2]
Total Mass%: [24.8, 13.6, 46.3, 15.3] of 1633.4
Codons List: ['ATG', 'GGA', 'CGC', 'TGA']
Is Protein?: NO

Region Name: Nyan Cat protein
Nucleotides: CAT-CAT-CAT-CAT-CAT-CAT-CAT-CAT-CAT-CAT
Nuc. Counts: [10, 10, 0, 10]
Total Mass%: [36.4, 29.9, 0.0, 33.7] of 3713.4
Codons List: ['CAT', 'CAT', 'CAT', 'CAT', 'CAT', 'CAT', 'CAT', 'CAT', 'CAT', 'CAT']
Is Protein?: NO

##################################################################


##################################################################
"""
