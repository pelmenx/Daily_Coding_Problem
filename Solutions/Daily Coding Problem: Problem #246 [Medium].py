# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Dropbox.
#
# Given a list of words, determine whether the words can be chained to form a
# circle. A word X can be placed in front of another word Y in a circle if the
# last character of X is same as the first character of Y.
#
# For example, the words ['chair', 'height', 'racket', touch', 'tunic'] can form
# the following circle: chair --> racket --> touch --> height --> tunic --> chair.
#
#
# --------------------------------------------------------------------------------
#
#
def make_words_curcle(words_list: list[str]) -> bool:
    def make_words_curcle_helper(array: list[str], words_curcle: list[str]) -> list[str]:
        if not array:
            if words_curcle[0][0] == words_curcle[-1][-1]:
                yield
        for i, item in enumerate(array):
            if words_curcle[-1][-1] == item[0]:
                yield from make_words_curcle_helper(array[:i] + array[i + 1:], words_curcle + [item])

    for curcle in make_words_curcle_helper(words_list[1:], [words_list[0]]):
        return True
    return False


assert make_words_curcle(['chair', 'height', 'racket', 'touch', 'tunic']) is True
