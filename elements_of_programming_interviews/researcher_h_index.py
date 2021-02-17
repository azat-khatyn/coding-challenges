"""
index_h = h papers that have been cited at least h times

Example:

Published papers = 'A, B, C, D, E, F, G, H, I'
Number_citations = [1, 4, 1, 4, 2, 1, 3, 5, 6]
h index = 4
"""

def get_h_index(cits):
    sorted_cits = sorted(cits)
    h = 1
    while h <= len(sorted_cits):
        count = 0
        for cit in sorted_cits:
            if cit >= h:
                count += 1
        if count < h:
            return h-1
        h += 1
    return h-1


def get_h_index_sorted(cits):




papers = 'A, B, C, D, E, F, G, H, I'
cits = [1, 4, 1, 4, 2, 1, 3, 5, 6]

print(get_h_index(papers, cits))
