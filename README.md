# dilbert-scraper
Download all dilbert comics from the start

Dilbert first comic strip came out in 1984, April 16th

The script itself already contains the initial date of the first release of the comic strip. However, you can modifiy both the start date and the end date of the strips to download.

# Installation

You need to have pip installed first. After which, install the following dependencies which are located inside the requirements.txt:

```
pip install -r requirements.txt
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