#! python3
# mapIt.py - Searches amazon for the product on the command line or
# the description on the clipboard. 

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
	# Get address from command line.
	address = ' '.join(sys.argv[1:])
else:
	# Get address from clipboard.
	address = pyperclip.paste()


webbrowser.open('https://www.amazon.com/s?k=' + address)
