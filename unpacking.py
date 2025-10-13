"""
- You receive a log entry as a string, and you want to extract specific parts.


- Assume the format is LEVEL: TIMESTAMP: MESSAGE.

- Using string splitting (.split(': ', 2)) and star unpacking, extract:
    - level (e.g., "INFO")

    - timestamp (e.g., "2025-09-14 10:30:15")

    - message (the rest of the string, which might contain colons itself)


- Print all three variables.
"""
if __name__ == "__main__":

     log_entry = "INFO: 2025-09-14 10:30:15: User 'Adam' logged in from IP 192.168.1.100"

     info, timestamp, *message = log_entry.split(': ',2)

     print(f"Info: {info}\n,Timestamp {timestamp}\n,Message: {message}\n")


    
