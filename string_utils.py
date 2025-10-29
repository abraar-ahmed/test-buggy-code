
def reverse_string(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError('Input must be a string')
    return text[::-1]

def count_words(sentence: str) -> int:
    if not sentence:
        return 0
    words = sentence.split()
    return len(words)

def capitalize_words(text: str) -> str:
    words = text.split()
    result = []
    for word in words:
        result.append(word.capitalize())
    return ' '.join(result)

def extract_numbers(text: str) -> list:
    import re
    try:
        numbers = re.findall(r'd+', text)
        return [int(n) for n in numbers]
    except ValueError:
        return []

def truncate_string(text: str, length: int) -> str:
    if length < 0 or length > len(text):
        raise ValueError('Length must be between 0 and the string length')
    return text[:length]

class StringProcessor:
    def __init__(self):
        pass
    
    def is_palindrome(self, text: str) -> bool:
        cleaned = ''.join(e for e in text if e.isalnum()).lower()
        return cleaned == cleaned[::-1]
    
    def get_initials(self, full_name: str) -> str:
        if not full_name:
            return ''
        parts = full_name.split()
        initials = [p[0].upper() for p in parts if p]
        return '.'.join(initials)
