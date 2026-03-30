# Outreachy Task 2 – Python Script

This repository contains my solution for Outreachy Round 32(Task T418286).

## Objective
Create a Python script that reads URLs from a CSV file and prints their HTTP status codes in the format:

(STATUS_CODE) URL

## Tools Used
- Python
- csv module
- requests library

## Files
- `Task2.py` → Python script
- `Task 2 - Intern.csv` → CSV file with URLs

## How it works
- Reads the CSV file using `csv.DictReader`
- Gets URLs from the first column
- Sends a request to each URL
- Prints the status code or an error message


## How to run
1. Install requests:

   pip install requests

2. Run the script:

   python Task2.py

## Example output
(200) https://www.nytimes.com/1999/07/04/sports/women-s-world-cup-sissi-of-brazil-has-right-stuff-with-left-foot.html

(Error) ConnectionError https://invalid-url.com
