# sbJsonParser

## Overview

`sbJsonParser` is a Python-based JSON parser, created as an educational tool to explore parsing techniques and compiler construction. It adeptly handles a variety of JSON structures, including complex nested objects and arrays, and recognizes multiple data types like strings, numbers, booleans, and null.

## Features

-   **Lexical Analysis**: Breaks down JSON strings into tokens.
-   **Syntactic Analysis**: Validates JSON structure from tokenized input.
-   **Versatile Data Type Support**: Handles strings, numbers, booleans, null, arrays, and nested objects.
-   **Error Reporting**: Provides clear error messages for invalid JSON inputs.
-   **Extensibility**: Can be expanded for additional functionalities, such as pretty-printing or converting JSON to Python objects.

## Getting Started

### Prerequisites

This project requires Python, preferably Python 3.x. Ensure Python is installed on your system.

### Installation

To get started with `sbJsonParser`, clone the repository to your local machine using CMD:

```
cd your\desired\directory
```
```
git clone https://github.com/stevobain/sbJsonParser.git
cd sbJsonParser
``` 

Replace `your\desired\directory` with the path where you want to clone the repository.

### Usage

To run the parser, use the following command in CMD:

```
python sbJsonParser.py path\to\your\jsonfile.json
``` 

Make sure to replace `path\to\your\jsonfile.json` with the actual path to the JSON file you want to parse.

## Testing

The parser has undergone thorough testing with various JSON files, including complex nested structures and edge cases. Unit tests will be written in the future.

## Contributing

Contributions to enhance `sbJsonParser` are always welcome. Feel free to fork the repository, make your changes, and open a pull request.

## License

`sbJsonParser` is open source and available under the MIT License.

## Acknowledgments

A heartfelt thank you to all contributors and supporters of this project, who have offered invaluable insights and suggestions.
