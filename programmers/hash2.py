def solution(phone_book):
    not_have_prefix = True
    sorted_phone_book = sorted(phone_book, key=len)
    not_have_prefix = check_have_prefix(sorted_phone_book)
    return not_have_prefix

def check_have_prefix(phone_book):
    not_have_prefix = True
    prefix_hashtable = {}
    for number in phone_book:
        not_have_prefix = hash_substrings(number, prefix_hashtable)
        if not not_have_prefix:
            return not_have_prefix
    return not_have_prefix

def hash_substrings(number, prefix_hashtable):
    hash_val = 0
    for i in range(1, len(number)+1):
        hash_val = hash(number[:i])
        if hash_val in prefix_hashtable:
            return False
    prefix_hashtable[hash_val] = number
    return True
