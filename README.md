# WA-ScheduledMessenger
A Python3 program with a WebUI that checks if today is the date to send a WhatsApp message to the corresponding person. For example on someones birthday or anniversary.

Works on Linux, Windows and MacOS

## Features

- Automattically check daily if messages need to be sent
- Erasing the schedule via the WebUI
- Adding tasks to the schedule via the WebUI
- Launch a manual check and send messages (if the schedule matches the date)
- Log on to the WebUI with other devices on the network (or from any network with port forwarding (not recommended))
- All functions are compatible if logged on via another device

## Demo
[![Watch the video](https://github.com/tdeerenberg/WA-ScheduledMessenger/blob/main/demo-thumbnail.png)](https://raw.githubusercontent.com/tdeerenberg/WA-ScheduledMessenger/main/demo.mp4)
## Installation

Install WA-ScheduledMessenger

```bash
  git clone https://github.com/tdeerenberg/WA-ScheduledMessenger.git
  cd WA-ScheduledMessenger
  pip install -r requirements.txt
```
    
## Usage/Examples

You need to be logged on on https://web.whatsapp.com/ in your default browser. WA-ScheduledMessenger opens this webpage and automatically send the set message to the designated contact.

The program can be run by clicking it in a file manager or with the command (make sure that you are in the right directory):
```bash
  python app.py
```
or
```bash
  python3 app.py
```
## Configuration

#### Username and password
All configurable settings can be configured in`config.json`

## Run Daily

There are two methods on how to run this program automatically every day.

#### First method: Via the WebUI
The option `Send the scheduled messages daily` in the navigation bar once logged onto the WebUI repeats the `Send the scheduled messages once` every day. It has a built in sleep function that sleeps for around 24 hours before executing again. **The WebUI will keep loading because the Python proces is not done until the sleep is over. Please do not open an issue saying that the page keeps loading indefinitely.**

#### Second method: Crontab (Linux) or Windows Task Scheduler (Windows)
WA-ScheduledMessenger can be added to the Crontab table (Linux) and to Windows Task Scheduler (Windows). If you use any other program that schedules and runs programs every day, you can use that.

The Python program that needs to be added to the scheduler application is ScheduledMessenger.py.

## Authors

- [@tdeerenberg](https://www.github.com/tdeerenberg)


## License

[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)
Permissions of this strong copyleft license are conditioned on making available complete source code of licensed works and modifications, which include larger works using a licensed work, under the same license. Copyright and license notices must be preserved. Contributors provide an express grant of patent rights. 
