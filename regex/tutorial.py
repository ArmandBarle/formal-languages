import re


def basic_tutorial():
    """Basic Patterns"""
    # Literal Characters: Match literal characters in a string.
    pattern = re.compile(r'hello')
    result = pattern.match('hello world')
    print(result.group())  # Output: hello

    # Dot Character: Matches any character except newline.
    pattern = re.compile(r'he..o')
    result = pattern.match('hello')
    print(result.group())  # Output: hello

    # Character Classes: Match one of a set of characters.
    pattern = re.compile(r'[aeiou]')
    result = pattern.search('hello')
    print(result.group())  # Output: e

    """Quantifiers"""
    # * Quantifier: Matches 0 or more repetitions of the preceding expression.
    pattern = re.compile(r'go*d')
    result = pattern.match('good')
    print(result.group())  # Output: good

    # + Quantifier: Matches 1 or more repetitions of the preceding expression.
    pattern = re.compile(r'go+d')
    result = pattern.match('good')
    print(result.group())  # Output: good

    # ? Quantifier: Matches 0 or 1 repetitions of the preceding expression.
    pattern = re.compile(r'colou?r')
    result = pattern.match('color')
    print(result.group())  # Output: color

    # {m} and {m,n} Quantifiers: Matches exactly m repetitions of the preceding expression.
    pattern = re.compile(r'\d{2,4}')
    result = pattern.match('123')
    print(result.group())  # Output: 123

    """Anchors"""
    # ^ Anchor: Matches the start of a string.
    pattern = re.compile(r'^hello')
    result = pattern.match('hello world')
    print(result.group())  # Output: hello

    # $ Anchor: Matches the end of a string.
    pattern = re.compile(r'world$')
    result = pattern.search('hello world')
    print(result.group())  # Output: world

    """Character Encapsulation"""
    # \ Character Class: Matches a literal character.
    pattern = re.compile(r'\d+')  # Matches one or more digits
    result = pattern.match('123')
    print(result.group())  # Output: 123

    """Groups"""
    # () Group: Matches a subexpression.
    pattern = re.compile(r'(\d+)-(\w+)')
    result = pattern.match('123-abc')
    print(result.group(1))  # Output: 123
    print(result.group(2))  # Output: abc

    """Flags"""
    # re.I, re.IGNORECASE: Makes the pattern case-insensitive.
    pattern = re.compile(r'hello', re.IGNORECASE)
    result = pattern.match('HELLO')
    print(result.group())  # Output: HELLO


def main():
    basic_tutorial()


if __name__ == '__main__':
    main()
