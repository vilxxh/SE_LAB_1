$ErrorActionPreference = "Continue"

# Run the tools against the original source and save the baseline reports.
python -m pylint hotel_booking_system_original.py *> pylint_report_before.txt
python -m bandit -r hotel_booking_system_original.py *> bandit_report_before.txt
python -m flake8 hotel_booking_system_original.py *> flake8_report_before.txt

# Run the tools against the revised source and save final reports.
python -m pylint hotel_booking_system.py *> pylint_report.txt
python -m bandit -r hotel_booking_system.py *> bandit_report.txt
python -m flake8 hotel_booking_system.py *> flake8_report.txt

Write-Host "`nAnalysis complete. Review these files:"
Get-ChildItem -Name "*_report*.txt"

Write-Host "`nFinal Pylint score:"
python -m pylint hotel_booking_system.py
