import argparse

from sniec_scrapper.scrapper import createIcsFile
import os.path

def main():
    parser = argparse.ArgumentParser(prog="sniec_scrapper", description="Scrap SNIEC website and generate ICS calendar file for exhibition events.")

    parser.add_argument('month',
    help="month which you want to scrap events in, eg. 2019-03")
    parser.add_argument('-c', '--cn',
    help="flag indicates whether you want to have a Chinese version output",
    action='store_true')
    parser.add_argument('-o', '--output-dir', help="output directory", type=str, default='.')

    args = parser.parse_args()

    lang = 'en'
    if args.cn:
        lang = 'cn'
    filename = 'sniec-calendar-{}-{}.ics'.format(args.month, lang)
    filename = os.path.join(args.output_dir, filename)
    print("Saving to {}".format(filename))
    createIcsFile(filename, args.month, args.cn)
