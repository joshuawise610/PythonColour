# 1. Introduction
This script can be installed to allow the standard python shell to print in coloured text to cmd or another shell which
is able to support coloured text in the terminal window. It acts as a wrapper for the colorama module.

# 2. What functions are available?
* printcol - Takes a string, foreground colour, background colour and brightness. The string is then printed using the
colours specified to the shell.
* printcollist - Takes a list of items, foreground colours, background colours and brightness levels and prints the text
as specified in each list
* inputcolour - Creates an input prompt for users which features different styling options for the user prompt and the
text being entered by the user.
* testcolour - Print a sting using each foreground colour and each brightness level on a black background apart from black
text being printed on a white background.

# 3. What colours are available?
Only the following colours can for printing as coloured text, they are:
* Red
* light red
* Magenta
* Light magenta
* Yellow
* Light yellow
* Green
* Light green
* Blue
* Light blue
* Cyan
* Light cyan
* Black
* White

You can set the shade of colour to one of:
* Bright
* Normal
* dim
