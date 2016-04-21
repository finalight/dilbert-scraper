# dilbert-scraper
Download all dilbert comics from the start

Dilbert first comic strip came out in 1984, April 16th

The script itself already contains the initial date of the first release of the comic strip. However, you can modifiy both the start date and the end date of the strips to download.

# Installation

You need to have pip installed first. After which, install the following dependencies which are located inside the requirements.txt:

```
pip install -r requirements.txt
```

You would also need to install supervisor in the operating system
After installation, proceed to add a config file with the follow values:

```
[program:dilbert]
; Point the command to the specific rq command you want to run.
; If you use virtualenv, be sure to point it to
; /path/to/virtualenv/bin/rq
; Also, you probably want to include a settings module to configure this
; worker.  For more info on that, see http://python-rq.org/docs/workers/
user=finalight
command=/usr/local/bin/rq worker #this should be the path of the python rq
process_name=%(program_name)s_%(process_num)02d

; If you want to run more than one worker instance, increase this
numprocs=1

; This is the directory from which RQ is ran. Be sure to point this to the
; directory where your source code is importable from
directory=/path/to

; RQ requires the TERM signal to perform a warm shutdown. If RQ does not die
; within 10 seconds, supervisor will forcefully kill it
stopsignal=TERM

; These are up to you
autostart=true
autorestart=true
```

# Execution

You can start the script by running the following command:

```
python dilbert.py
```


# Troubleshooting

Sometimes the script will just break in the midst. So what you can do is just modify the start date and rerun the script, this will download the strip from the missing date onwards


# Improvement to made

* Use of multiple redis queue to speed up the download process.
* Ensure the download never breaks in the midst. If it fails, it should restart by itself and continue from the break