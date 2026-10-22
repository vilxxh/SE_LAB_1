# Lab 5 — Static Code Analysis: Issue Log

> Update the line numbers and findings below after running Pylint, Bandit, and Flake8 against the original file in your own environment. Severity must match the actual tool output where available.

| Issue | Tool / category | Original location | Risk or impact | Fix applied |
|---|---|---:|---|---|
| Dynamic `eval()` on a string | Bandit / security | `compute_seasonal_rate` | Evaluates Python expressions and can execute unintended code if input is untrusted. | Replaced expression strings with a numeric multiplier and direct arithmetic. |
| Hardcoded secret-like value | Security review | `main` | Secrets committed in source can be exposed and are difficult to rotate. | Read the optional value from `HOTEL_SECRET_KEY` environment variable. |
| Shell command built from filename | Bandit / security | `export_room_ledger` | Shell interpretation of untrusted filename text can create command-injection risk. | Replaced `os.system` with a normal `print` statement. |
| MD5 used for hashing | Bandit / cryptography review | `generate_guest_hash` | MD5 is unsuitable for security-sensitive cryptographic use. | Replaced it with SHA-256; this remains an identifier digest, not password storage. |
| Mutable default list | Pylint / correctness | `bookRoom` | Calls can unintentionally share one list object. | Changed default to `None` and initialize a list inside the function. |
| Bare `except` and silent `pass` | Pylint / reliability | `cancel_booking` | Hides unexpected failures and gives no clear result. | Check whether the room exists and return a success/failure boolean. |
| Unused variable / imports | Pylint / maintainability | `check_room_status`, imports | Dead code makes the program harder to maintain. | Removed unused variable and imports. |
| Manual file open/close | Code quality | `export_room_ledger` | An exception may prevent the file from being closed. | Used a context manager (`with open(...)`). |
| Insecure or predictable booking reference | Security review | `generate_booking_ref` | Standard pseudorandom values are not ideal when a reference must be hard to guess. | Used `secrets.randbelow`; for a production booking system, uniqueness must also be enforced. |
| Inconsistent naming and formatting | Flake8 / Pylint | Multiple locations | Non-PEP 8 naming, spacing, and formatting reduce readability. | Reformatted code and changed `bookRoom` to `book_room`, updating its caller. |

## Verification notes

- Run all three tools locally and retain their actual output in the `*_report_before.txt` and `*_report.txt` files.
- Confirm the final Pylint score is above 9.5/10.
- Confirm Bandit findings have been reviewed and resolved as required by the lab.
- Confirm Flake8 produces no output.
- Run the program and verify booking, cancellation, pricing, hashing, reference generation, and ledger export.
- Static analysis is not proof that a program is bug-free.
