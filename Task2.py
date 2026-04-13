import csv
import requests


file_path = 'Task 2 - Intern.csv'


def print_status_codes(file_path):
    """
    Read URLs from CSV and print their  HTTP status codes.
    Format: (STATUS_CODE) URL 
    """
    
    with open(file_path, mode = 'r', encoding = 'utf-8') as file:
        url_reader = csv.DictReader(file) 
        url_key = url_reader.fieldnames[0]  
        
        for row in url_reader:
            url = row[url_key].strip()

            try:
                response = requests.head(url, timeout=10)
                print(f"({response.status_code}) {url}")  
            
            except requests.exceptions.RequestException as err: 
                print(f"(Error) {url}")

if __name__ == "__main__":
    print_status_codes(file_path)
    
        
           