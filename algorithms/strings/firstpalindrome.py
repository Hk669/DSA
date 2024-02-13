def firstPalindrome(words):
    """
    Args:
        words List[string] : Input
        output string : Output
    """
    for word in words:
        if reverse(word) == word:
            return word
    return ""


def reverse(word):
    rev = ''
    idx = len(word)-1
    while idx >= 0:
        rev += word[idx]
        idx -=1
    return rev