# 1. Introduction
This script can be installed to allow the standard python shell to print in coloured text to cmd or another shell which
is able to support coloured text in the terminal window. It acts as a wrapper for the colorama module.

# 2. What functions are available?
* printcol(text, fore_col=None, back_col=None, shade=None, end=None)
Prints a single line of text to the screen using the given fore_col and back_col colours. shade specifies to use a light or dark colour and end specifies which character to end the line on.
text - The string to print.
fore_col - A string containing a colour to use as the font colour.
back_col - A string containing a colour to use as the background colour.
shade - A string to decide to use a bright colour or dark colour.
end - A string to determine if the next print statement will be displayed on a new line.
* printcollist(list_to_print, fore_col=None, back_col=None, shade=None, end=None)
Prints out each of the elements of the list using the colours specified at the same index in the other lists.
list_to_print - The name of an iterable which can be printed out.
fore_col - A list of foregound colours to use to print out each line of text.
back_col - A list of background colours to print each line onto.
shade - A list specifing the brightness of each line of text.
end - Decides if the text should be printed as one long line or should be split up into individual lines.
* inputcolour - Creates an input prompt for users which features different styling options for the user prompt and the
text being entered by the user.
* testcolour - Print a sting using each foreground colour and each brightness level on a black background apart from black
text being printed on a white background.

Note: By default white text is shown on a black background using the normal shade.

# 3. What colours are available?
Only the following colours can for the foreground and background of text, they are:
* Red
* Light red
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
* Dim

# 5. Example
The code `printcol("Hello world", fore_col="red", back_col="black", shade="normal", end="\n")` produces the following output.

![Red text example](https://github.com/joshuawise610/PythonColour/raw/master/docs/image%20captures/example%20hello%20world.jpg)
