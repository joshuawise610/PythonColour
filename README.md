===== 1. Introduction =====
This script can be installed to allow the standard python shell to print in coloured text to cmd or another shell which is able to
support coloured text in the terminal window. It acts as a wrapper for the colorama module.

===== 2. How does it work? =====
The printcol function is imported automatically when the python interpreter is run by the means of adding an import statement to
the user script which is run when python is started. This may not work when the user is writing scripts to run not in the
interactive window.

===== 3. What functions are added? =====
Only one function is added to python when run called 'printcol' it takes a argument to print to the screen like print then the
foreground colour, the background colour and the shade to use.

===== 4. What colours are avilable? =====
printcol can only use the following colours for printing as coloured text, they are:
Red, light red, magenta, light magenta, yellow, light yellow, green, light green, blue, light blue, cyan, light cyan, black and white.
You can set the shade of colour to one of: bright, normal or dim.
