BASE64_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
HEX_CHARS = "1234567890abcdefABCDEF"

import math
from regex import regexes
def shannon_entropy(data, iterator):
    """
    Borrowed from http://blog.dkbza.org/2007/05/scanning-data-for-entropy-anomalies.html
    """
    if not data:
        return 0
    entropy = 0
    for x in iterator:
        p_x = float(data.count(x))/len(data)
        if p_x > 0:
            entropy += - p_x*math.log(p_x, 2)
    return entropy

def regex_check(text):
    #text = ''.join(c for c in text if c in BASE64_CHARS)
    regex_matches = []
    for key in regexes:
        t =regexes[key].findall(text)
        if t:
            for k in t:
                regex_matches.append(k)
    return regex_matches

def find_entropy(text):
    #text = ''.join(" " for c in text if c not in BASE64_CHARS)
    stringsFound = []
    lines = text.split("\n")
    for line in lines:
        for word in line.split():
            base64_strings = get_strings_of_set(word, BASE64_CHARS)
            hex_strings = get_strings_of_set(word, HEX_CHARS)
            for string in base64_strings:
                b64Entropy = shannon_entropy(string, BASE64_CHARS)
                if b64Entropy > 5:
                    stringsFound.append(string)
            for string in hex_strings:
                hexEntropy = shannon_entropy(string, HEX_CHARS)
                if hexEntropy > 3:
                    stringsFound.append(string)
    return "".join("ENTROPY: " + str(line) +"\n" for line in stringsFound if len(line) < 50) +  "".join("REGEX: " + str(line) +"\n" for line in regex_check(text)if len(line) < 50)


def get_strings_of_set(word, char_set, threshold=20):
    count = 0
    letters = ""
    strings = []
    for char in word:
        if char in char_set:
            letters += char
            count += 1
        else:
            if count > threshold:
                strings.append(letters)
            letters = ""
            count = 0
    if count > threshold:
        strings.append(letters)
    return strings