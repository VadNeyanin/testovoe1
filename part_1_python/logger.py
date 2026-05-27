from datetime import datetime

def good_logger(request_code, status_code, response_text):
    log_text = f"Date: {datetime.now()} -- OK    -- Request code: {request_code} -- Response code: {status_code} -- Text: {response_text}"
    return log_text

def bad_logger(request_code, status_code, exception):
    log_text = f"Date: {datetime.now()} -- ERROR -- Request code: {request_code} -- Response code: {status_code} -- {exception}"
    return log_text