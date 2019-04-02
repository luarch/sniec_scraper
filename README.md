# SNIEC Scraper

Scrape [SNIEC website](http://www.sniec.net/cn/visit_exhibition.php) and generate [ICS calendar file](https://tools.ietf.org/html/rfc5545) for exhibition events

## Usage

```
$ pip3 install -r requirements.txt
$ python3 -m sniec_scraper -h
```

```
usage: sniec_scraper [-h] [-c] [-o OUTPUT_DIR] month

Scrape SNIEC website and generate ICS calendar file for exhibition events.

positional arguments:
  month                 month which you want to scrape events in, eg. 2019-03

optional arguments:
  -h, --help            show this help message and exit
  -c, --cn              flag indicates whether you want to have a Chinese
                        version output
  -o OUTPUT_DIR, --output-dir OUTPUT_DIR
                        output directory
``` 
