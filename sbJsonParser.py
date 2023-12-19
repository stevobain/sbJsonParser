import re

def lexer(json_string):
    tokens = []
    i = 0
    while i < len(json_string):
        if json_string[i] in ['{', '}', ':', ',', '[', ']']:
            tokens.append(json_string[i])
            i += 1
        elif json_string[i] == '"':
            # Extract string literal
            start = i
            i += 1
            while i < len(json_string) and json_string[i] != '"':
                i += 1
            if i < len(json_string):
                tokens.append(json_string[start:i + 1])
                i += 1
        elif json_string[i].isdigit() or json_string[i] in ['-', '+']:
            # Extract number (integer or float)
            start = i
            i += 1
            while i < len(json_string) and (json_string[i].isdigit() or json_string[i] in ['.', 'e', 'E', '+', '-']):
                i += 1
            tokens.append(json_string[start:i])
        elif re.match(r"\A(true|false|null)\Z", json_string[i:i+4]) or \
             re.match(r"\A(true|false|null)\Z", json_string[i:i+5]):
            # Extract boolean or null
            if json_string.startswith("true", i):
                tokens.append("true")
                i += 4
            elif json_string.startswith("false", i):
                tokens.append("false")
                i += 5
            elif json_string.startswith("null", i):
                tokens.append("null")
                i += 4
        else:
            if not json_string[i].isspace():
                # Invalid token
                return ['INVALID']
            i += 1
    return tokens

def parse_value(tokens, index):
    if tokens[index] == '{':
        return parse_object(tokens, index)
    elif tokens[index] == '[':
        return parse_array(tokens, index)
    elif is_valid_value(tokens[index]):  # The is_valid_value function you already have
        return index + 1, True
    else:
        return index, False

def parse_array(tokens, index):
    index += 1  # Skip '['
    if tokens[index] == ']':
        return index + 1, True  # Empty array

    while True:
        index, valid = parse_value(tokens, index)
        if not valid:
            return index, False

        if tokens[index] == ']':
            return index + 1, True
        elif tokens[index] != ',':
            return index, False

        index += 1  # Skip ','

def parse_object(tokens, index):
    index += 1  # Skip '{'
    if tokens[index] == '}':
        return index + 1, True  # Empty object

    while True:
        # Object key (string) followed by colon
        if tokens[index][0] != '"' or tokens[index + 1] != ':':
            return index, False
        index += 2

        # Object value
        index, valid = parse_value(tokens, index)
        if not valid:
            return index, False

        if tokens[index] == '}':
            return index + 1, True
        elif tokens[index] != ',':
            return index, False

        index += 1  # Skip ','

def is_valid_value(token):
    # Check if the token is a valid JSON value (string, number, true, false, null)
    if token[0] == '"' and token[-1] == '"':  # String value
        return True
    if token.isdigit() or (token.replace('.', '', 1).isdigit() and token.count('.') < 2):  # Number value
        return True
    if token in ["true", "false", "null"]:  # Boolean or null
        return True
    return False

def parser(tokens):
    if not tokens or tokens[0] != '{':
        return False

    index, valid = parse_object(tokens, 0)
    return valid and index == len(tokens)

import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python sbJsonParser.py <path_to_json_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    try:
        with open(file_path, 'r') as file:
            json_string = file.read()
            tokens = lexer(json_string)
            is_valid = parser(tokens)
            print("Valid JSON" if is_valid else "Invalid JSON")
    except IOError as e:
        print(f"Error reading file: {e}")

if __name__ == "__main__":
    main()