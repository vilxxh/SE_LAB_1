# Lab 5 — Reflection

> Compare these responses with the four exact reflection questions in the lab handout and adjust the headings to match them.

## 1. What is static code analysis?

Static code analysis inspects source code without executing it. It can find likely bugs, insecure patterns, maintainability problems, and style violations early in development. It complements, but does not replace, testing the program.

## 2. What is the difference between Pylint, Bandit, and Flake8?

Pylint checks code quality, common programming mistakes, naming, unused variables, and maintainability. Bandit looks for common security-sensitive patterns in Python code. Flake8 checks style and formatting, including many PEP 8 violations. They overlap in places, but each has a different main focus.

## 3. What issues were found and how were they addressed?

The original program included dynamic `eval()`, a hardcoded secret-like string, shell-command construction, MD5 hashing, a mutable default list, broad exception handling, unused code, and manual file management. The updated implementation removes expression evaluation, reads the optional secret from an environment variable, avoids shell execution, uses SHA-256 for the identifier digest, uses `None` for the optional list, validates room existence, removes unused code, and uses a file context manager. The actual tool reports should be consulted to identify which of these were specifically flagged by each tool.

## 4. What did you learn from the lab?

I learned that static analysis can detect different classes of issues before the program is deployed. Security findings should be reviewed according to their actual context and severity; code-quality warnings should be fixed without changing intended behavior; and formatting tools help keep code consistent. I also learned that a clean report does not prove correctness, so I must run the program and test important paths after changing it.
