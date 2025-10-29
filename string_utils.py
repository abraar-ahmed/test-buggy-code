def reverse_string(text):
    # Missing type checking
    return text[::-1]

def count_words(sentence):
    words = sentence.split()
    return len(words)
    # No handling for None or empty strings

def capitalize_words(text)  # Missing colon
    words = text.split()
    result = []
    for word in words:
        result.append(word.capitalize())
    return ' '.join(result)

def extract_numbers(text):
    import re
    numbers = re.findall(r'\d+', text)
    return [int(n) for n in numbers]
    # No error handling for invalid input

def truncate_string(text, length):
    return text[:length]
    # No check if length is negative or greater than string length

class StringProcessor:
    def __init__(self):
        pass
    
    def is_palindrome(self, text):
        cleaned = text.lower().replace(' ', '')
        return cleaned == cleaned[::-1]
        # Doesn't handle special characters or punctuation
    
    def get_initials(self, full_name):
        parts = full_name.split()
        initials = [p[0].upper() for p in parts]  # IndexError if empty string
        return '.'.join(initials)
