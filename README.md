# Project Title

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Contributing](../CONTRIBUTING.md)

## About <a name = "about"></a>

Write your Oreilly's Highlights and Notes to a text file based on Book Title

## Getting Started <a name = "getting_started"></a>

1) Export all notes and highlights from your Oreilly Portal (it's exported as a CSV file).
2) Install Prequisites

### Prerequisites

- panda==0.24.2

## Usage <a name = "usage"></a>

```python
import oreilly

highlights = oreilly.read_csv(csv_filepath)

book_highlight = highlights.by_book_title('The Data Science HandBook')

book_highlight.to_txt('data_science_handbook.txt')
```
