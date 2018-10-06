"""CSCA08 Assignment 1, Fall 2017
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
 Date: October 31st, 2017
"""
# You will also see '\' at the end of some lines. A TA taught me about this
# during one of my exercise errors. He told me that'\' basically ignores the
# '\n', and executes the next line as if it were continuous. =D

# these represent nucleotides that can be in a gene
NUCLEOTIDE_A = 'A'
NUCLEOTIDE_T = 'T'
NUCLEOTIDE_C = 'C'
NUCLEOTIDE_G = 'G'
# represents all the variables that a star can pair with
STAR = 'ATCG'


def help_can_pair(gene_loop, gene_compare):
    ''' (str, str) -> bool
    Returns True if and only if gene_one and gene_two can pair following these
    specifications:
    - A and T can pair with each other
    - C and G can pair with each other
    REQ: gene_one and gene_two can only have 'A', 'T', 'C' and 'G'
    >>> help_can_pair('TCTC', 'AGAG')
    True
    >>> help_can_pair('AGTC', 'CTTA')
    False
    '''
    # initialize can_pair as false and index as 0
    can_pair = True
    index = 0
    # while you're not at the end of gene_loop and not can_pair
    while (can_pair) and index < len(gene_loop):
        # if it is A then gene_compare should have T at the same index, if true
        if (gene_loop[index] == NUCLEOTIDE_A) and (gene_compare[index] ==
                                                   NUCLEOTIDE_T):
            # increase index by 1
            index += 1
        # since python is dumb, I need to check the same thing both ways
        elif (gene_loop[index] == NUCLEOTIDE_T) and (gene_compare[index] ==
                                                     NUCLEOTIDE_A):
                # increase index by 1
                index += 1
        # elif it is C then gene_compare should have G at the same index, if
        # true
        elif (gene_loop[index] == NUCLEOTIDE_C) and (gene_compare[index] ==
                                                     NUCLEOTIDE_G):
            # increase index by 1
            index += 1
        # since python is dumb, I need to check the same thing both ways
        elif (gene_loop[index] == NUCLEOTIDE_G) and (gene_compare[index] ==
                                                     NUCLEOTIDE_C):
            # increase index by 1
            index += 1
        # otherwise
        else:
            # negate can pair
            can_pair = not can_pair
    # return can_pair
    return can_pair


def pair_genes(gene_one, gene_two):
    ''' (str, str) -> bool
    Returns True if and only if gene_one and gene_two can pair such that A and
    T pair and G and T pair with themselves
    REQ: gene_one and gene_two should only have letters A, T, C and G
    >>> pair_genes('TCAG', 'CTGA')
    True
    >>> pair_genes('TCTC', 'AGAG')
    True
    >>> pair_genes('AGTC', 'CTTA')
    False
    '''
    # finding the longer gene
    # if gene_one > gene_two
    if len(gene_one) > len(gene_two):
        # store gene_one as a variable and gene_two as another variable
        gene_loop = gene_one
        gene_compare = gene_two
    # if gene_two < gene_one or they are equal
    else:
        # store the gene's in different variables
        gene_loop = gene_two
        gene_compare = gene_one
    # call the helper function to see if the genes pair
    can_pair = help_can_pair(gene_loop, gene_compare)
    # if the genes do not pair
    if can_pair is False:
        # reverse the longer gene
        gene_loop = gene_loop[::-1]
    # check if the genes pair when one of them is reversed
    can_pair = help_can_pair(gene_loop, gene_compare)
    # return can pair
    return can_pair


def zip_length(gene):
    ''' (str) -> int
    Returns the maximum number of nucleotides that can zip (the process of
    pairing the first nucleotide with the last nucleotide within the same gene)
    in the gene.
    REQ: the gene should only have letters 'A', 'T', 'G' and 'C'
    >>> zip_length ('AGTCTCGCT')
    2
    >>> zip_length ('AGTCG')
    0
    '''
    # initialize counter and index as 0
    counter = 0
    index = 0
    # set can_zip to False
    can_zip = False
    # take the first and last element
    first_element = gene[index]
    last_element = gene[index-1]
    # check if pair_genes is true
    can_zip = pair_genes(first_element, last_element)
    # while can_zip is true
    while (can_zip is True) and (len(gene) >= 0):
        # increase the counter by 1
        counter += 1
        # increase index by 1
        index += 1
        # slice the first and the last element of the gene
        first_element = gene[index]
        last_element = gene[-index-1]
        # check if the new first and last elements can pair
        can_zip = pair_genes(first_element, last_element)
    # return counter
    return counter


def help_find_anchor(gene, anchor):
    ''' (list, str) -> int
    Returns the index at which the anchor is found in the gene.
    This function will not mutate gene.
    REQ: the gene and anchor can only have nucleotides 'A', 'T', 'C', and 'G'
    >>> help_find_anchor(['A', 'T', 'G', 'C', 'A', 'T', 'A'], 'AT')
    0
    >>> help_find_anchor(['G', 'A', 'T', 'C', 'A', 'T', 'A'], 'TA')
    5
    '''
    # initialize any variables needed
    index = 0
    found_anchor = False
    splice = -1
    # while the first character of the start anchor is not found and we haven't
    # reached the end of the list
    while (not found_anchor and index < len(gene)):
        # check if the current index in the source gene is the first character
        # of the anchor. If true, (0, why? because I want to check if the
        # element of the current index I am on is the same as the element of
        # the anchor at 0
        if (gene[index] == anchor[0]):
            # check if the character after the same as the character in source
            # gene, if True (Token is a synonym for index, 'cause I used index
            # before -> Google just happens to save your life with variable
            # names that mean the same thing); you start at index + 1 because
            # you want to check if the next character is the same as start
            # anchor's
            for token in range(1, len(anchor)):
                if (gene[index+token] == anchor[token]):
                    # store the token on where it is found
                    splice = index
                    # change the found anchors to True to stop the loop
                    found_anchor = True
        # increase the index by 1
        index += 1
    # return the index from where we need to start splice
    return splice


def help_splice_gene(gene, start_anchor, end_anchor):
    ''' (list, str, str) -> tuple of two int
    Returns two integers (start_splice and end_splice) that will determine
    where the gene has to start splicing and end splicing. It compares and
    returns the lowest index possible in the gene. Returns -1, when not found
    This function will not mutate source_gene and destination_gene.
    REQ: source_gene, destination_gene, start_anchor and end_anchor must only
    have 'A', 'T', 'G' and 'C'
    >>> help_splice_gene(['A', 'T', 'G', 'C', 'A', 'T', 'A'], 'AT', 'TA')
    (0, 5)
    >>> help_splice_gene(['T', 'A', 'G', 'C', 'A', 'G', 'A', 'T'], 'AT', 'AG')
    (0, 5)
    '''
    # find the index of the occurence of start_anchor in source gene without
    # the anchor being reversed
    unreversed_start_splice = help_find_anchor(gene, start_anchor)
    # find the index of the occurence of start_anchor in source gene with the
    # anchor being reversed and store it in a variable
    reversed_start_splice = help_find_anchor(gene, start_anchor[::-1])
    # compare the two indices. if the index of the un-reversed anchor is
    # smaller
    if (unreversed_start_splice < reversed_start_splice):
        # then find the end_anchor in original source gene and store it as a
        # variable
        start_splice = unreversed_start_splice
        end_splice = help_find_anchor(gene, end_anchor)
    # if the reversed anchor has a smaller index
    elif (unreversed_start_splice > reversed_start_splice):
        # then find reverse the end anchor to find the end of the sequence
        start_splice = reversed_start_splice
        end_splice = help_find_anchor(gene, end_anchor[::-1])
    final_indices = (start_splice, end_splice)
    # return both indices in the form of a tuple
    return final_indices


def splice_gene(source_gene, destination_gene, start_anchor, end_anchor):
    ''' (list, list, str, str) -> NoneType
    Returns a NoneType and mutates the destination_gene and source_gene by
    splicing the source_gene between the start_anchor and end_anchor and
    inserting it in between the destination_gene's start_anchor and end_anchor.
    This function will mutate the source_gene and destination_gene.
    REQ: The source_gene, destination_gene start_anchor and end_anchor can only
    have nucleotides 'A', 'T', 'C', and 'G'
    >>> source_gene = ['A', 'T', 'G', 'C', 'A', 'T', 'A']
    >>> destination_gene = ['T', 'A', 'A', 'T', 'G', 'C', 'A', 'G', 'T', 'A']
    >>> splice_gene(source_gene, destination_gene, 'AT', 'TA')
    >>> source_gene == ['A']
    True
    >>> destination_gene == ['A', 'T', 'G', 'C', 'A', 'T', 'A', 'T', 'G', 'C',\
    'A', 'G', 'T', 'A']
    True
    '''
    # initialize any variables that I need
    splice_list = []
    # find the lowest occurence of the start and end anchors in the source gene
    (start_splice, end_splice) = help_splice_gene(source_gene, start_anchor,
                                                  end_anchor)
    # find the lowest occurence of the start and end anchors in the destination
    # gene
    (start_replace, end_replace) = help_splice_gene(destination_gene,
                                                    start_anchor, end_anchor)
    # check if none of the indices of start_splice or end_splice is -1, if true
    if not(start_splice == -1) and not(end_splice == -1) and \
       not(end_replace == -1) and not(start_replace == -1):
        # pop each element out of the source gene and store it in a variable
        # used index loop because start_splice and end_splice are both ints and
        # I was not dealing with the entire list, only part of it. Therefore
        # did not use elemental. The for loop will splice it backwards, hence
        # we will need to reverse it later, when replacing it in the
        # destination gene
        for index in range(end_splice, start_splice-1, -1):
            splice_list += [source_gene.pop(index)]
        # replace the elements from the source gene to the destination gene
        destination_gene[start_replace:end_replace] = splice_list[::-1]


def help_get_digits(mask, index):
    ''' (str, int) -> int
    Returns an int which are the digits after a non-digit character
    (nucleotides, stars, multis '[]') in the mask the functions get starting
    at and continuing after the index.
    REQ: gene and mask can only have 'A', 'T', 'C' and 'G'
    >>> help_get_digits('[A]C3', 4)
    3
    >>> help_get_digits('C3AG423T2', 4)
    423
    '''
    # initialize any variables we need. We don't intialize index because it is
    # already given to us. Therefore only initialize the digit variable
    digits = ''
    # while we haven't reached the end of the mask and we haven't found all the
    # digits
    while (index < len(mask) and mask[index].isdigit()):
        # add it to the digit var
        digits += mask[index]
        # add 1 to the index
        index += 1
    # returns the digit var
    if (digits == ''):
        digits = 1
    return int(digits)


def help_decode_mask(mask):
    ''' (str) -> list
    Returns the decoded version of a mask as a list. A mask is series of
    characters that include digits, '[', ']', letters, and '*'). They follow
    these rules:
    - if within brackets, they are called multis and can pair with anything
    inside the brackets
    - there must be a letter ('A', 'T', 'C' or 'G') before a number. The number
    shows how many times a nucleotide can occur
    - '*' can act like any nucleotide ('A', 'T', 'C' or 'G') and hence can pair
    in any order.
    REQ: The mask can have only have nucleotides 'A', 'T', 'C' or 'G'
    >>> help_decode_mask('CT')
    ['C', 'T']
    >>> help_decode_mask('[AG]3*')
    ['AG', 'AG', 'AG', 'ATCG']
    '''
    # initialize any variables needed
    decoded_mask = []
    index = 0
    # loop through the entire mask. Used while loop because if I want to skip
    # a multi's elements, then index for loop doesn't let me.
    while (index < len(mask)):
        # if the character is an alpha
        if (mask[index].isalpha()):
            # get digits by the helper function
            digits = help_get_digits(mask, index+1)
            # store it in the list
            decoded_mask += [mask[index]]*digits
        # if the element is a star
        elif (mask[index] is '*'):
            # get digits by the helper function
            digits = help_get_digits(mask, index+1)
            # store it in the list
            decoded_mask += [STAR]*digits
        # if the element is a bracket
        elif (mask[index] is '['):
            # find the next bracket
            close_bracket = mask.find(']')
            # slice everything within the bracket and add it to the list
            nucleotides = mask[index+1:close_bracket]
            # get digits by the helper function
            digits = help_get_digits(mask, close_bracket+1)
            # store it in the list
            decoded_mask += [nucleotides]*digits
            # increase the index by the length of the multi. If I don't do
            # this, then it will run throug the elements of the multi too and
            # give me access output (output that is not required by the user)
            index = index + close_bracket
        index += 1
    # return the list
    return decoded_mask


def help_match_mask(gene, mask):
    ''' (str, str) -> int
    Returns the lowest occurence of the first nucleotide where the mask matches
    with the gene. Returns -1, if the mask does not match anywhere with the
    gene.
    REQ: gene and mask can only have 'A', 'T', 'C' and 'G'
    >>> help_match_mask('TAGTCA', 'CT')
    1
    >>> help_match_mask('ACAA', '[A]C3')
    -1
    '''
    # initialize any variables needed
    index = 0
    paired = False
    # decode the mask using helper function
    decoded_mask = (help_decode_mask(mask))
    # for each nucleotide in the mask
    while (not paired) and (index < len(decoded_mask)):
        # check if the nucleotide can pair with the gene. If true
        if (help_can_pair(decoded_mask[index], gene[index])):
            # make the result equal to the current index
            paired = True
            matched_nucleotide = index
        # else check for the next character in the gene
        else:
            index += 1
    # if paired never changes
    if (paired is False):
        # make matched nucleotide to -1
        matched_nucleotide = -1
    # return matched nucleotide
    return matched_nucleotide


def match_mask(gene, mask):
    ''' (str, str) -> int
    Returns the lowest index of the first nucleotide where the mask matches.
    Returns -1, if the mask does not match anywhere.
    REQ: gene and mask can only have 'A', 'T', 'C' and 'G'
    >>> match_mask('TAGTCA', 'CT')
    1
    >>> match_mask('ACAA', '[A]C3')
    -1
    '''
    # get the matched nucleotide.
    matched_nucleotide = help_match_mask(gene, mask)
    # If it is -1,
    if matched_nucleotide == -1:
        # reverse the gene and check again
        matched_nucleotide = help_match_mask(gene[::-1], mask)
        # if it is not -1,
        if (matched_nucleotide != -1):
            # then get the value of the index relative to the original gene
            matched_nucleotide = len(gene) - matched_nucleotide
    # return the first index where the nucleotide matched in the gene
    return matched_nucleotide


def process_gene_file(input_file, gene, mask):
    ''' (io.TextIOWrapper, str, str) -> tuple
    Returns a tuple in the form (p, m, z), where
    -> p is the string representation of first gene in the input_file that can
       pair with gene
    -> m is the string representation of first gene in the input_file that will
       match with the mask
    -> z is the string represntation of the longest zip gene found in any gene
       up to and including the indices of p and m
    '''
    # read the file into a list
    all_genes = input_file.readlines()
    # for every element in the list
    for index in range(len(all_genes)):
        # strip the spaces at the end
        current_gene = all_genes[index].strip()
        # calculate zip length of the gene
        length_zipped = zip_length(current_gene)
        # find where the mask matches in the gene
        mask_matched_at = match_mask(current_gene, mask)
        # initialize paired at and masked at as -1
        paired_at = -1
        masked_at = -1
        # check if the input gene pairs with the gene in the file, if true
        if (pair_genes(current_gene, gene)):
            # make the current gene equal to the result
            does_pair = current_gene
            paired_at = index
        # else check if the input mask matches with the gene in the file, if
        # true
        elif (mask_matched_at > 0):
            # make the current gene equal to the result
            does_mask = current_gene
            masked_at = index
        # else check if the zip length is greater than p and m. If true
            # make the current gene equal to the result
        elif (length_zipped > masked_at) and (length_zipped > paired_at):
            longest_zip = current_gene
    result = (does_pair, does_mask, longest_zip)
    # return the result
    return result
