#!/usr/bin/env python

import os
import logging
import ConfigParser
import argparse

import spynner
from bs4 import BeautifulSoup
from jinja2 import Environment, PackageLoader

# Setup logging
script_name = os.path.splitext(os.path.basename(__file__))[0]
logger = logging.getLogger(script_name)
logger.setLevel(logging.DEBUG)

# Logging to file
ch = logging.FileHandler(os.path.join('log', script_name + '.log'))
ch.setLevel(logging.DEBUG)
ch.setFormatter(logging.Formatter('%(asctime)s;%(levelname)s;%(message)s'))
logger.addHandler(ch)

# Logging to console
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
console.setFormatter(logging.Formatter('%(asctime)s;%(levelname)s;%(message)s'))
logger.addHandler(console)

# Parse command line options
parser = argparse.ArgumentParser(
    description='Grabs Now Playing from radio stations')
parser.add_argument('--version', action='version', version='%(prog)s 0.1.8')
args = parser.parse_args()

# Read config file
config = ConfigParser.SafeConfigParser()
config.read(os.path.join('etc', script_name + '.conf'))

# Get URL list
browser_urls = config.get('Type1', 'url').replace("\n", '').split(',')

# Open virtual browser
browser = spynner.Browser()

# Process URLs
now_playing = []
for browser_url in browser_urls:
    browser.load(browser_url, 30)
    browser.wait(5)
    radio_doc = BeautifulSoup(browser.html)
    logger.info('Fetched URL %s', browser_url)

    # Process DOM tree
    now_playing_table = radio_doc.find('div', 'trackInfo')
    artist = now_playing_table.find('span', 'artistName').string.strip()
    song = now_playing_table.find('a', 'trackTitle').string.strip()
    now_playing.append([ artist, song ])

# Close virtual browser
browser.close()

# Prepare template
env = Environment(loader=PackageLoader('__main__', 'templates'))
template = env.get_template('now-playing.tmpl')

# Write CSV file
output_file = os.path.join('output', config.get('General', 'output'))
output = open(output_file, 'w')
output.write(template.render(now_playing=now_playing).encode('utf-8'))
output.close()

logger.info('CSV now-playing list "%s" written', output_file)
