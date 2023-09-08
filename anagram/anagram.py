def find_anagrams(word: str, candidates: list[str]):
    '''
    Create a copy list with the candidates sorted and lowercased that will help
    comparing 1 to 1 with the word (also sorted and lowercase) and get the indexes
    when reading the list.

    Be aware that different results are expected wether a word is sorted or lowercased first.
    Sorting an uppercase word differs from the lowercase equivalent
    '''
    aux_candidates = [ ''.join(sorted(candidate_word.lower())) for candidate_word in candidates]
    aux_word = ''.join(sorted(word.lower()))

    result = []

    for i, candidate in enumerate(aux_candidates):
        if aux_word == candidate:
            result.append(candidates[i])

        if word.lower() == candidates[i].lower() and result:
            result.pop()
            
    return result