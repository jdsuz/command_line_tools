#! python3
# mapIt.py - Launches a map in the browswer using an address from the 
# command line or clipboard.

import webbrowser, sys, pyperclip
import logging

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s',filename='mapitLog.log',level=logging.DEBUG)

if len(sys.argv) > 1:
	# Get address from command line.
	address = ' '.join(sys.argv[1:])
else:
	# Get address from clipboard.
	address = pyperclip.paste()

logging.info(sys.argv)
logging.info(address)

webbrowser.open('https://www.google.com/maps/place/' + address)
