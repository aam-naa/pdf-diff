# pdf-diff: Prototype for GSOC 2026

Prototype for the Wayback PDF Changes project for GSOC 2026. 

This repository contains a simple prototype that detects changes made between two given PDFs.

## Installation
This script can be installed as a Python package using the following commands:

```bash
git clone https://github.com/aam-naa/pdf-diff.git
cd pdf-diff
pip install .
```

## Usage
Once installed, the module pdfdiff can be imported and used:

```python
from pdfdiff import pdf_diff

result = pdf_diff("file1.pdf", "file2.pdf")
print(result)
```

## How It Works
PyMuPDF extracts the text from both files, which is then compared using the built-in difflib package.
A "+" prefix indicates a line has been added.
A "-" prefix indicates a line has been removed.

## Dependencies

- Python 3.10+
- PyMuPDF



