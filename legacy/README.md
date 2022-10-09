![Logo](logo.png)

# WA-ScheduledMessenger (Legacy Version)

A Python3 program that checks if today is the date to send a WhatsApp message to the corresponding person. For example on someones birthday or anniversary.

Works on Linux, Windows and MacOS


## Installation

Install WA-ScheduledMessenger

```bash
  git clone https://github.com/tdeerenberg/WA-ScheduledMessenger.git
  cd WA-ScheduledMessenger
  pip install -r requirements.txt
```

## Usage
You need to be logged on on https://web.whatsapp.com/ in your default browser. ScheduledMessenger.py opens this webpage and automatically send the set message to the designated contact.

The program can be run by clicking it in a file manager or  with the command:
```
python ScheduledMessenger.py
```
or
```
python3 ScheduledMessenger.py
```

## Configuration

#### Add contacts to message
The contacts and messages can be added and changed in the ```date.csv``` file.

For example (phone numbers are not filled in for obvious reasons):
| Name | Phone        | Date  | Message                |
| ---- | ------------ | ----- | ---------------------- |
| John | +41xxxxxxxxx | 15-05 | Happy Birthday John!   |
| Bob  | +316xxxxxxxx | 22-09 | Happy Anniversary Bob! |

#### Change the name of the output files
There are three input/output files. The ```.csv``` file with dates and contacts and the log files.
If, for any reason, you'd like to change the input/output location of each file, 
then it can be edited in ```config.json```.
## Run Daily
There are two methods on how to run this program automatically every day.

#### First method: Built in sleep
WA-ScheduledMessenger has a built in fuction to sleep for 24 hours before executing the program again.
#### Second method: Crontab (Linux) or Windows Task Scheduler (Windows)
can be added to the Crontab table (Linux) and to Windows Task Scheduler (Windows).
If you add ScheduledMessenger.py to a service that automatically runs a program daily, remove these two lines from projectname.py:
```python
53  print("The program wil sleep for 24 hours and run again. \nDO NOT CLOSE THIS PROGRAM/WINDOW. \n\nTo cancel: Ctrl+C or Kill Python")
54  sleep(86400)
```

## Authors

- [@tdeerenberg](https://www.github.com/tdeerenberg)

## License

[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)
Permissions of this strong copyleft license are conditioned on making available complete source code of licensed works and modifications, which include larger works using a licensed work, under the same license. Copyright and license notices must be preserved. Contributors provide an express grant of patent rights. 

