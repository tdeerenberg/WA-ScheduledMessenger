# Author: tdeerenberg (C) 15 September 2022
import pywhatkit as pwk
import json
import csv
import datetime
import os
from time import sleep

# Global variables
now = datetime.datetime.now()
with open("config.json", "r") as json_config:
    config = json.load(json_config)

# Logging
def message_sent(db):
    with open(config["SUCCESSFUL_MESSAGE_LOG"], "a") as log:
        log.write(f"""
Date: {now.strftime("%d %b %Y")}
Time: {now.strftime("%X")}
Name: {db['Name']}
Phone: {db['Phone']}
Message: {db['Message']}
-------------------------
""")

def message_not_sent(db):
    with open(config["ERROR_LOG_FILENAME"], "a") as log:
        log.write(f"""
Date: {now.strftime("%d %b %Y")}
Time: {now.strftime("%X")}
Name: {db['Name']}
Phone: {db['Phone']}
Message: {db['Message']}
-------------------------
""")

# Main program
def main():
    with open(config["DATE_FILENAME"],'r') as data:
        reader = csv.DictReader(data)
        for row in reader:
            if now.strftime('%d-%m') == row["Date"]:
                print(f"Sending message to {row['Name']} with phone number: {row['Phone']}")
                try:
                    pwk.sendwhatmsg_instantly(row['Phone'], row['Message'])
                    message_sent(row)
                except:
                    message_not_sent(row)
    try: os.remove("PyWhatKit_DB.txt")
    except: print()

if __name__ == "__main__":
    main()
