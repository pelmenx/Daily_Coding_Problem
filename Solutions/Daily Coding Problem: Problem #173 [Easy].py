# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Stripe.
#
# Write a function to flatten a nested dictionary. Namespace the keys with a
# period.
#
# For example, given the following dictionary:
#
# {
#     "key": 3,
#     "foo": {
#         "a": 5,
#         "bar": {
#             "baz": 8
#         }
#     }
# }
#
#
# it should become:
#
# {
#     "key": 3,
#     "foo.a": 5,
#     "foo.bar.baz": 8
# }
#
#
# You can assume keys do not contain dots in them, i.e. no clobbering will occur.
#
#
# --------------------------------------------------------------------------------
#
#
def reorganize_dictionary(dictionary):
    def reorg_dict(dictionary_, k=""):
        if isinstance(dictionary_, dict):
            for key in dictionary_.keys():
                yield from reorg_dict(dictionary_[key], k + key + ".")
        else:
            yield k[:-1], dictionary_
    result_dict = {}
    for key_, item in reorg_dict(dictionary):
        result_dict[key_] = item
    return result_dict


dict_ = {"key": 3,
         "foo": {"a": 5,
                 "bar": {
                     "baz": 8}}}
reorganize_dictionary(dict_) == {'key': 3, 'foo.a': 5, 'foo.bar.baz': 8}
