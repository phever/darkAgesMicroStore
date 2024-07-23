# Dark Ages Micro Store
#### by: [Phever](https://phever.dev)

for selling items and such within the [Dark Ages](https://www.darkages.com) MMO

__Feel free to use this yourself__

### \# Hosting yourself

1. you will need a domain name (url/website address) - these cost a small amount of $ per year. I recommend [NameCheap](https://namecheap.com)
2. set up your domain on [CloudFlare](https://cloudflare.com) (very simple & free), to simplify DNS changes
3. find a hosting provider - any Virtual Private Server (VPS) running Ubuntu is fine
4. download and setup darkAgesMicroStore

### \# darkAgesMicroStore setup

> the following are instructions for __Ubuntu Linux__, if hosting on another operating system, you'll have to modify the instructions for that OS

> Instructions that are within `code blocks` are __Terminal__ commands (usually SSH'd into your VPS)

1. install the requirements `sudo apt install python3 git nginx`
2. navigate to your preferred directory (usually /var/www) `cd /var/www`
3. download these files `git clone git@github.com:phever/darkAgesMicroStore.git`
4. enter the new directory `cd darkAgesMicroStore`
5. create a virtual environment `python3 -m venv venv`
6. enter the virtual environment `source venv/bin/activate`
7. download required python packages `pip install -r requirements.txt`
8. create local_settings file `cp darkAgesMicroStore/_local_settings.py darkAgesMicroStore/local_settings.py`
9. edit the local_settings.py file with your preferred editor `nano darkAgesMicroStore/local_settings.py`
