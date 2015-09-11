""" module 4 : sequence alignment """

def score(letr1, letr2, diag_score, off_diag_score, dash_score):
    """ determine the score on scoringmatrix[letr1][letr2] """
    if letr1 == '-' or letr2 == '-':
        return dash_score
    if letr1 == letr2:
        return diag_score
    return off_diag_score


def build_scoring_matrix(alphabet, diag_score, off_diag_score, dash_score):
    """ returns a dictionary of dictonaries of scoring matrix """
    score_matrix = {}
    alphabet = list(alphabet) + ['-']
    for letter in alphabet:
        inner_dict = {}
        for inner_letter in alphabet:
            inner_dict[inner_letter] = score(letter, inner_letter, diag_score, off_diag_score, dash_score)
        score_matrix[letter] = inner_dict
    return score_matrix


def det_score(org_score, global_flag):
    """ determine score based on whether local or global alignment needed """
    if org_score >= 0:
        return org_score
    if not global_flag:
        return 0
    return org_score

def get_score(scoring_matrix, seq_x, seq_y, row, col):
    """ 
    return the score at seq_x[row], seq_y[col] where row and col is the position
    of letters in seq_x and seq_y respectively
    """
    letter_x = seq_x[row]
    letter_y = seq_y[col]
    return scoring_matrix[letter_x][letter_y]

def compute_alignment_matrix(seq_x, seq_y, scoring_matrix, global_flag):
    """ computes local or global alignment matrix based on global flag """
    size_x = len(seq_x)
    if size_x == 0:
        return [[0]]
    size_y = len(seq_y)
    align_matrix = [[0]] 
    for len_x in range(1, size_x + 1):
        org_score = (scoring_matrix[seq_x[len_x - 1]]['-'] + 
                    align_matrix[len_x - 1][0])
        if len_x >= len(align_matrix):
            align_matrix.append([])
        align_matrix[len_x].insert(0, det_score(org_score, global_flag))
    
    for len_y in range(1, size_y + 1):
        org_score = (scoring_matrix['-'][seq_y[len_y - 1]] +
                    align_matrix[0][len_y - 1])
        align_matrix[0].insert(len_y, det_score(org_score, global_flag))
    
    for len_x in range(1, size_x + 1):
        for len_y in range(1, size_y + 1):
            score1 = (align_matrix[len_x - 1][len_y - 1] + 
                    get_score(scoring_matrix, seq_x, seq_y, len_x - 1, len_y - 1))
            score2 = (align_matrix[len_x - 1][len_y] + 
                    scoring_matrix[seq_x[len_x - 1]]['-'])
            score3 = (align_matrix[len_x][len_y - 1] + 
                    scoring_matrix['-'][seq_y[len_y - 1]])
            org_score = max(score1, score2, score3)
            align_matrix[len_x].insert(len_y, det_score(org_score, global_flag))
    
    return align_matrix

def compute_global_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix):
    """
    compute the optimal global alignment of seq_x and seq_y based on the scoring
    matrix and alignment matrix
    returns a tuple (optimal_score, alignement_x, alignment_y)
    """
    size_x = len(seq_x)
    size_y = len(seq_y)
    align_x = align_y = ""

    while size_x != 0 and size_y!= 0:
        alignment_score = get_score(scoring_matrix, seq_x, seq_y, size_x - 1, size_y - 1)
        alignment_score = alignment_matrix[size_x - 1][size_y - 1] + alignment_score
        if alignment_matrix[size_x][size_y] == alignment_score:
            align_x = seq_x[size_x - 1] + align_x
            align_y = seq_y[size_y - 1] + align_y
            size_x -= 1
            size_y -= 1


        elif alignment_matrix[size_x][size_y] == (alignment_matrix[size_x - 1][size_y] + 
                                                scoring_matrix[seq_x[size_x - 1]]['-']):
            align_x = seq_x[size_x - 1] + align_x
            align_y = '-' + align_y
            size_x -= 1

        else:
            align_y = seq_y[size_y - 1] + align_y
            align_x = '-' + align_x
            size_y -= 1
    
    while size_x != 0:
        align_x = seq_x[size_x - 1] + align_x
        align_y = '-' + align_y
        size_x -= 1
    
    while size_y != 0:
        align_y = seq_y[size_y - 1] + align_y
        align_x = '-' + align_x
        size_y -= 1

    return (alignment_matrix[len(seq_x)][len(seq_y)], align_x, align_y)


def max_indices(matrix):
    """ find the indices of the maximum value in a matrix """
    row = 0
    col = 0
    max_score = matrix[0][0]
    index_max = lambda lst: (lst.index(max(lst)), max(lst))
    for idx in range(len(matrix)):
        temp_col, temp_max = index_max(matrix[idx])
        if temp_max > max_score:
            row = idx
            col = temp_col
            max_score = temp_max
    return (row, col, max_score)


def compute_local_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix):
    """
    compute the optimal local alignment of seq_x and seq_y based on the scoring
    matrix and alignment matrix
    returns a tuple (optimal_score, alignement_x, alignment_y)
    """
    size_x, size_y, max_score = max_indices(alignment_matrix)
    align_x = align_y = ""
    end = lambda row, col: not alignment_matrix[row][col]
    while size_x != 0 and size_y!= 0:
        alignment_score = get_score(scoring_matrix, seq_x, seq_y, size_x - 1, size_y - 1)
        alignment_score = alignment_matrix[size_x - 1][size_y - 1] + alignment_score
        if alignment_matrix[size_x][size_y] == alignment_score:
            align_x = seq_x[size_x - 1] + align_x
            align_y = seq_y[size_y - 1] + align_y
            size_x -= 1
            size_y -= 1


        elif alignment_matrix[size_x][size_y] == (alignment_matrix[size_x - 1][size_y] + 
                                                scoring_matrix[seq_x[size_x - 1]]['-']):
            align_x = seq_x[size_x - 1] + align_x
            align_y = '-' + align_y
            size_x -= 1

        else:
            align_y = seq_y[size_y - 1] + align_y
            align_x = '-' + align_x
            size_y -= 1

        if end(size_x, size_y):
            return (max_score, align_x, align_y)

    while size_x != 0:
        align_x = seq_x[size_x - 1] + align_x
        align_y = '-' + align_y
        size_x -= 1
    
    while size_y != 0:
        align_y = seq_y[size_y - 1] + align_y
        align_x = '-' + align_x
        size_y -= 1

    return (max_score, align_x, align_y)
