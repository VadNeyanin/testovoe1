import os
from dotenv import load_dotenv
from request import request
from logger import good_logger, bad_logger
from code_checker import code_checker

load_dotenv()

def main():
    URL = os.getenv("URL")
    codes = os.getenv('CODES').split(',')
    logfile = os.getenv('LOGFILE')
    
    for code in codes:
        try:
            status_code, response_text = request(URL, code)
            if code_checker(status_code):
                raise Exception(f"HTTP {status_code}")
                
        except Exception as e:
            print(bad_logger(code, status_code, e))
            
        else:
            log_entry = good_logger(code, status_code, response_text)
            print(log_entry)
            
            with open(logfile, 'a') as f:
                f.write(log_entry + '\n')

if __name__ == "__main__":
    main()