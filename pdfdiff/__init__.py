import pymupdf
import difflib

def pdf_diff(file1, file2):
    with pymupdf.open(file1) as doc1, pymupdf.open(file2) as doc2:
        lines1 = "".join([page.get_text() for page in doc1]).splitlines()
        lines2 = "".join([page.get_text() for page in doc2]).splitlines()

    result = difflib.ndiff(lines1, lines2)
    return list(result)