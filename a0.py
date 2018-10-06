''' CSCA08 Assignment 0, Fall 2017
 I hereby agree that the work contained herein is solely my work and that I
 have not received any external help from my peers, nor have I used any
 resources not directly supplied by the course in order to complete this
 assignment. I have not looked at anyone else's solution, and no one has
 looked at mine. I understand that by adding my name to this file, I am
 making a formal declaration, and any subsequent discovery of plagiarism
 or other academic misconduct could result in a charge of perjury in
 addition to other charges under the academic code of conduct of the
 University of Toronto Scarborough Campus
 Name: Sakina Shabbir Gadriwala
 UtorID: gadriwa1
 Student Number: 1004351051
 Date: October 7th, 2017
'''


def split_input(dna_sequence):
    ''' (str) -> list of str
    Returns a list with three elements from the input dna_sequence:
    - Upstream data
    - Gene
    - Downstream data
    REQ: dna_sequence can only have the letters 'A', 'G', 'C' and 'T'
    REQ: dna_sequence can only have capital letters.
    >>> split_input('CATATGGCTATG')
    ['CAT', 'ATGGCT', 'ATG']
    >>> split_input('ATGAGCTATG')
    ['', 'ATGAGCT', 'ATG']
    >>> split_input('GACATGCAT')
    ['GAC', 'ATGCAT', '']
    >>> split_input('ACACACAC')
    ['ACACACAC', '', '']
    '''
    # find 'ATG' within the sequence
    first_ATG_index = dna_sequence.find('ATG')
    # remove ATG from the sequence and find the next sequence
    string_without_first_ATG = dna_sequence[first_ATG_index + 3:]
    partial_index = string_without_first_ATG.find('ATG')
    # if first_ATG_index is -1 (i.e. there is no ATG present)
    if (first_ATG_index == -1):
        first_ATG_index = len(dna_sequence)
        # create upstream; gene and downstream equal to an empty string
        upstream = dna_sequence[:first_ATG_index]
        # combine it into a string
        dna_combination = upstream + ' ' + ' '
    # if partial_index is -1 (i.e. there is only one ATG present)
    elif (partial_index == -1):
        partial_index = 0
        # create upstream and gene; make downstream equal to an empty string
        upstream = dna_sequence[:first_ATG_index]
        gene = dna_sequence[first_ATG_index:]
        # combine it into a string
        dna_combination = upstream + ' ' + gene + ' '
    else:
        # calculate the second ATG index in dna_sequence
        second_ATG_index = first_ATG_index + 3 + partial_index
        # start splitting using the first_ATG_index and second_ATG_index
        upstream = dna_sequence[:first_ATG_index]
        gene = dna_sequence[first_ATG_index:second_ATG_index]
        downstream = dna_sequence[second_ATG_index:]
        # combine upstream, gene and downstream
        dna_combination = upstream + ' ' + gene + ' ' + downstream
    # convert dna_combination into a list
    split_dna = dna_combination.split(' ')
    # return the list
    return split_dna


def get_gene(dna_sequence):
    ''' (str) -> str
    returns the gene within dna_sequence else returns 'ERROR'
    REQ: dna_sequence can only have the letters 'A', 'G', 'C' and 'T'
    REQ: dna_sequence can only have capital letters.
    >>> get_gene('ATGAGCTATG')
    'ATGAGCT'
    >>> get_gene('ATGTAGATG')
    'ATGTAG'
    >>> get_gene('CATAG')
    'ERROR'
    '''
    # call split_input to split the sequence and return the list
    split_dna = split_input(dna_sequence)
    # return the second element of the list
    if (split_dna[1] != ""):
        gene = split_dna[1]
    else:
        # if the second element is '', then return 'ERROR'
        gene = 'ERROR'
    return gene


def validate_gene(gene):
    ''' (str) -> bool
    Returns True when the gene is valid iff:
    - contains a start condon (3 character): ATG
    - contains a condon after the start condon
    - does not have incomplete condons
    - does not have 4 consecutive nucleotides (i.e. repeating letters)
    Else returns false.
    REQ: gene can only contain A, T, C and G
    REQ: gene can only have capital letters.
    >>> validate_gene('ATGTAG')
    True
    >>> validate_gene('CATAG')
    False
    '''
    # initiate variables: has_complete_condon and no_consecutive_letters
    has_complete_condon = False
    no_consecutive_letters = True
    # check if gene contains ATG
    has_atg = gene.startswith('ATG')
    # check if gene contains 3 characters after ATG or gene contains
    # an incomplete condon
    if ((len(gene)) % 3 == 0):
        has_complete_condon = True
    # if it has 4 consecutive letters then return false.
    if (('A'*4 in gene) or ('T'*4 in gene) or ('C'*4 in gene) or
       ('G'*4 in gene)):
        no_consecutive_letters = False
    # return True if gene is valid, else false
    valid_gene = has_atg and has_complete_condon and no_consecutive_letters
    return valid_gene


def is_palindromic(gene):
    ''' (str) -> bool
    Returns True if the gene is read the same forwards and backwards. Else
    returns False.
    REQ: The gene can only contain A, T, C and G
    >>> is_palindromic('ATGGTA')
    True
    >>> is_palindromic('ATGTAG')
    False
    '''
    # flip the gene
    flip_gene = gene[::-1]
    # if the flip_gene and gene are the same return True, else return False
    palindromic_gene = (flip_gene == gene)
    return palindromic_gene


def evaluate_sequence(dna_sequence):
    ''' (str) -> str
    Returns the following output based on the input dna_sequence:
    - No Gene Found
    - Invalid Gene
    - Valid Gene Found
    - Valid Palindromic Gene Found
    REQ: dna_sequence should not have spaces in it
    REQ: dna_sequence should only have letters A, T, G, C
    >>> evaluate_sequence('CATATGGCTATG')
    'Valid Gene Found'
    >>> evaluate_sequence('ACACACAC')
    'No Gene Found'
    >>> evaluate_sequence('CTATGGTATG')
    'Invalid Gene'
    >>> evaluate_sequence('CATATGGTA')
    'Valid Palindromic Gene Found'
    '''
    # get gene from the input dna_sequence
    gene = get_gene(dna_sequence)
    # initialize result
    result = ''
    # If gene is present
    if (gene != 'ERROR'):
        # check if gene is valid
        if (validate_gene(gene) is True):
            result = 'Valid Gene Found'
            # check if gene is palindromic
            if (is_palindromic(gene) is True):
                result = 'Valid Palindromic Gene Found'
        else:
            # if gene is not valid
            result = 'Invalid Gene'
    else:
        # if gene is 'ERROR'
        result = 'No Gene Found'
    return result
