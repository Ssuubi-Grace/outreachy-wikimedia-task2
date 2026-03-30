import csv
import requests


file_path = 'Task 2 - Intern.csv'


def print_status_codes(file_path):
    """
    Reads a list of URLs from a CSV file and shows their status codes.
    Format: (STATUS_CODE) URL 
    """
    
    #opening the CSV file with UTF-8 encoding to handle non-ASCIII text.
    with open(file_path, mode = 'r', encoding = 'utf-8') as file:
        
        #reading the CSV rows as dictionaries so columns can be accessed by their header names
        url_reader = csv.DictReader(file) 

        #getting the first column name as the key for accessing URLs   
        url_key = url_reader.fieldnames[0]  
        
        for row in url_reader:
            url = row[url_key].strip() #removing any accidental spaces from the URL

           
            #Fetching the URL with a timeout of and printing it's status code.
            try:
                response = requests.get(url, timeout=10)
        
                print(f"({response.status_code}) {url}")  
            
            #handling request exceptions and printing an error message with the URL. 
            except requests.exceptions.RequestException as err: 
                print(f"(Error) {err} {url}")
                
file_path = 'Task 2 - Intern.csv'

if __name__ == "__main__":
    print_status_codes(file_path)
    
        
           