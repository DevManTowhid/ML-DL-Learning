# Regular Expressions in Python

Regular expressions (regex) are powerful tools for pattern matching and text manipulation in Python. This guide covers basic and advanced operations with examples.

## Basic Regex Operations

### re.match()
Checks if the regular expression pattern matches at the beginning of the string.  
Returns a match object if a match is found; None if no match is found.

**Example:**
```python
import re
text = "Hello world"
match = re.match(r"Hello", text)
print(match.group())  # Output: Hello
```

### re.search()
Searches the entire string for the first occurrence of the pattern.  
Returns a match object if a match is found; None if no match is found.

**Example:**
```python
text = "The rain in Spain"
match = re.search(r"rain", text)
print(match.group())  # Output: rain
```

### re.findall()
Returns a list of all non-overlapping matches of the pattern in the string.

**Example:**
```python
text = "cat bat hat"
matches = re.findall(r"at", text)
print(matches)  # Output: ['at', 'at', 'at']
```

### re.sub()
Replaces the matched pattern with a specified replacement string.  
Returns the modified string.

**Example:**
```python
text = "I like cats"
new_text = re.sub(r"cats", "dogs", text)
print(new_text)  # Output: I like dogs
```

### re.split()
Splits the string at each match of the pattern and returns a list of substrings.

**Example:**
```python
text = "one,two,three"
parts = re.split(r",", text)
print(parts)  # Output: ['one', 'two', 'three']
```

### re.finditer()
Returns an iterator that yields match objects for all non-overlapping matches of the pattern.

**Example:**
```python
text = "test1 test2 test3"
for match in re.finditer(r"test\d", text):
    print(match.group())  # Output: test1, test2, test3
```

### re.compile()
Compiles a regular expression pattern into a regex object that can be used for matching operations.

**Example:**
```python
pattern = re.compile(r"\d+")
text = "There are 123 apples"
match = pattern.search(text)
print(match.group())  # Output: 123
```

### re.escape()
Escapes all non-alphanumeric characters in a string so that they can be used in a regex pattern without special meaning.

**Example:**
```python
special_string = "a.b+c"
escaped = re.escape(special_string)
print(escaped)  # Output: a\.b\+c
```

### re.subn()
Similar to re.sub(), but it also returns the number of substitutions made.

**Example:**
```python
text = "foo bar foo"
new_text, count = re.subn(r"foo", "baz", text)
print(new_text)  # Output: baz bar baz
print(count)     # Output: 2
```

## Advanced Matching Operations

### Character Classes and Anchors

- `\d`: Matches any digit (0-9).  
  **Example:** `re.findall(r'\d+', 'abc123def456')` → `['123', '456']`

- `\D`: Matches any non-digit character.  
  **Example:** `re.findall(r'\D+', 'abc123def')` → `['abc', 'def']`

- `\w`: Matches any word character (alphanumeric + underscore).  
  **Example:** `re.findall(r'\w+', 'hello_world 123')` → `['hello_world', '123']`

- `\W`: Matches any non-word character.  
  **Example:** `re.findall(r'\W+', 'hello world!')` → `[' ', '!']`

- `\s`: Matches any whitespace character (space, tab, newline).  
  **Example:** `re.split(r'\s+', 'a b c')` → `['a', 'b', 'c']`

- `\S`: Matches any non-whitespace character.  
  **Example:** `re.findall(r'\S+', 'a b c')` → `['a', 'b', 'c']`

- `\b`: Matches a word boundary.  
  **Example:** `re.findall(r'\bword\b', 'a word here')` → `['word']`

- `\B`: Matches a non-word boundary.  
  **Example:** `re.findall(r'\Bword\B', 'swordwords')` → `['word']`

- `^`: Anchors the match at the beginning of the string.  
  **Example:** `re.match(r'^Hello', 'Hello world')` → Match

- `$`: Anchors the match at the end of the string.  
  **Example:** `re.search(r'world$', 'Hello world')` → Match

- `[]`: Defines a character class.  
  **Example:** `re.findall(r'[aeiou]', 'hello')` → `['e', 'o']`

- `[^ ]`: Defines a negated character class.  
  **Example:** `re.findall(r'[^aeiou]', 'hello')` → `['h', 'l', 'l']`

### Quantifiers and Grouping

- `()`: Groups patterns and captures matched content.  
  **Example:** `re.search(r'(abc)+', 'abcabc')` → `('abcabc', 'abc')`

- `|`: Acts as a logical OR.  
  **Example:** `re.findall(r'cat|dog', 'cat dog')` → `['cat', 'dog']`

- `{m,n}`: Matches at least m, at most n times.  
  **Example:** `re.findall(r'a{2,3}', 'aaa')` → `['aaa']`

- `*`: Matches zero or more times.  
  **Example:** `re.findall(r'ab*', 'a ab abb')` → `['a', 'ab', 'abb']`

- `+`: Matches one or more times.  
  **Example:** `re.findall(r'ab+', 'a ab abb')` → `['ab', 'abb']`

- `?`: Matches zero or one time.  
  **Example:** `re.findall(r'ab?', 'a ab abb')` → `['a', 'ab', 'ab']`

Special Matching Sequences:

\A:

Matches only at the start of the string (equivalent to ^ but for the whole string).

\Z:

Matches only at the end of the string (equivalent to $ but for the whole string).

\b:

Matches a word boundary (e.g., space between a word and non-word character).

\B:

Matches a non-word boundary.

Grouping and Capturing:

():

Groups the regex pattern inside parentheses to apply quantifiers or capture the matched text for later use.

\1, \2, ...:

Refers to the capturing groups within the pattern (for backreferencing).

Assertions:

Positive Lookahead (?=...):

Matches a group only if it is followed by a specific pattern, without consuming characters.

Negative Lookahead (?!...):

Matches a group only if it is not followed by a specific pattern, without consuming characters.

Positive Lookbehind (?<=...):

Matches a group only if it is preceded by a specific pattern.

Negative Lookbehind (?<!...):

Matches a group only if it is not preceded by a specific pattern.