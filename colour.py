from colorama import init, Fore, Back, Style


def printcol(text, fore_col=None, back_col=None, shade=None, end=None):
    """A function which prints the text in the specified colour on the specified background.
    Arguments:
    text - The text to print to the screen in the required format.
    fore_col - The colour of the text to print the text in. Default: white, can be either of: red, light red, magenta,
    light Magenta, yellow, light yellow, green, light green, blue, light blue, cyan, light cyan, black or white
    back_col - The colour to print the text onto. Default: black, can be either of: red, light red, magenta, light
    magenta, yellow, light yellow, green, light green, blue, light blue, cyan, light cyan, black or white
    shade - The shade of the colour to use. Default: normal, can be either of: dim, normal, bright
    end - What character to end the print line with. By default this is the newline character. This can be set to an
    empty string to change the colour of the text being printed out.
    """

    # Handle the keyword arguments so that they still work correctly when the terminal is used, this allows any not
    # defined to be set to the default. E.G. It is possible to run printcol("Some text") and still get some output,
    # This will be white text using the normal shade on a white background, this is normal print for cmd, but may be
    # different for other terminals.
    if fore_col is None:
        fore_col = "white"
    if back_col is None:
        back_col = "black"
    if shade is None:
        shade = "normal"
    if end is None:
        end = "\n"

    init(autoreset=True)  # Make sure the next print statement runs correctly regardless of type
    # Convert the inputs into lowercase names to be checked
    fore_col = fore_col.lower()
    back_col = back_col.lower()
    shade = shade.lower()

    # Check the shade, can be one of three options
    if shade == "dim":
        shade = Style.DIM
    elif shade == "bright":
        shade = Style.BRIGHT
    # For when underline available
    # elif shade == "underline":
    #    shade = Style.UNDERLINED
    else:  # If normal or other input
        shade = Style.NORMAL

    # Begin checking the colour required
    if fore_col == "red":
        fore_col = Fore.RED
    elif fore_col == "light red" or fore_col == "bright red":  # Same as Style.BRIGHT
        fore_col = Fore.LIGHTRED_EX

    elif fore_col == "magenta":
        fore_col = Fore.MAGENTA
    elif fore_col == "light magenta" or fore_col == "bright magenta":
        fore_col = Fore.LIGHTMAGENTA_EX

    elif fore_col == "yellow":
        fore_col = Fore.YELLOW
    elif fore_col == "light yellow" or fore_col == "bright yellow":
        fore_col = Fore.LIGHTYELLOW_EX

    elif fore_col == "green":
        fore_col = Fore.GREEN
    elif fore_col == "light green" or fore_col == "bright green":
        fore_col = Fore.LIGHTGREEN_EX

    elif fore_col == "blue":
        fore_col = Fore.BLUE
    elif fore_col == "light blue" or fore_col == "bright blue":
        fore_col = Fore.LIGHTBLUE_EX

    elif fore_col == "cyan":
        fore_col = Fore.CYAN
    elif fore_col == "light cyan" or fore_col == "bright cyan":
        fore_col = Fore.LIGHTCYAN_EX

    elif fore_col == "black":
        fore_col = Fore.BLACK

    else:
        # If white or other to prevent errors
        fore_col = Fore.WHITE

    # Then check the background colour required
    if back_col == "red":
        back_col = Back.RED
    elif back_col == "light red" or back_col == "bright red":
        back_col = Back.LIGHTRED_EX

    elif back_col == "magenta":
        back_col = Back.MAGENTA
    elif back_col == "light magenta" or back_col == "bright magenta":
        back_col = Back.LIGHTMAGENTA_EX

    elif back_col == "yellow":
        back_col = Back.YELLOW
    elif back_col == "light yellow" or back_col == "bright yellow":
        back_col = Back.LIGHTYELLOW_EX

    elif back_col == "green":
        back_col = Back.GREEN
    elif back_col == "light green" or back_col == "bright green":
        back_col = Back.LIGHTGREEN_EX

    elif back_col == "blue":
        back_col = Back.BLUE
    elif back_col == "light blue" or back_col == "bright blue":
        back_col = Back.LIGHTBLUE_EX

    elif back_col == "cyan":
        back_col = Back.CYAN
    elif back_col == "light cyan" or back_col == "bright cyan":
        back_col = Back.LIGHTCYAN_EX

    elif back_col == "white":
        back_col = Back.WHITE

    else:
        # If black or other to prevent errors
        back_col = Back.BLACK

    # Then print the text to the screen
    print(shade + fore_col + back_col + text, end=end)


def printcollist(list_to_print, fore_col=None, back_col=None, shade=None, end=None):
    """A Function which takes a list and iterates through the list and prints it out in coloured text. The
    colours and shade to use can be provided as a list or as a sting.
    Arguments:
    list_to_print - A iterable list of strings or numbers to print out.
    fore_col - A list of strings or a single string to use as the text colour for the strings being printed.
    Default White, colours same as printcol
    back_col - A list of strings or a single string to use as the background text colour for the strings being
    printed. Default Black, colours same as printcol
    shade - A list of strings or a single string to use as the shade of the text colour for the string.
    Default Normal, options same as printcol
    end - A list of strings or a single string to use as the separator between the strings being printed.
    Default Newline, this list must be passed for the system to work correctly
    """

    # Check the keyword arguments are None and then set the defaults.
    if fore_col is None:
        fore_col = "white"
    if back_col is None:
        back_col = "black"
    if shade is None:
        shade = "normal"
    if end is None:
        end = "\n"

    # Check the lists are of the correct length before attempting the iteration
    if len(list_to_print) == len(fore_col) == len(back_col) == len(shade) == len(end):
        # Then print out each item as required in its colour
        for item, foreground, background, shade, ending in zip(list_to_print, fore_col, back_col, shade, end):
            # Print the item
            printcol(item, fore_col=foreground, back_col=background, shade=shade, end=ending)
    else:
        # The lists are not of all equal length so print an error message in red.
        printcol("Please use lists of equal length.")


def testcolour(use_string=None):
    """A function which is used to test the colour printing of the shell by printing a string in different colours onto
    different backgrounds.
    Arguments:
        use_string - The string to use for testing the console prints text correctly in all colours. Default:
        'Hello World'."""
    if use_string is None:
        use_string = "Hello World"
    printcol(use_string, "red", "black", "dim")
    printcol(use_string, "red", "black", "normal")
    printcol(use_string, "red", "black", "bright")
    printcol(use_string, "magenta", "black", "dim")
    printcol(use_string, "magenta", "black", "normal")
    printcol(use_string, "magenta", "black", "bright")
    printcol(use_string, "yellow", "black", "dim")
    printcol(use_string, "yellow", "black", "normal")
    printcol(use_string, "yellow", "black", "bright")
    printcol(use_string, "green", "black", "dim")
    printcol(use_string, "green", "black", "normal")
    printcol(use_string, "green", "black", "bright")
    printcol(use_string, "cyan", "black", "dim")
    printcol(use_string, "cyan", "black", "normal")
    printcol(use_string, "cyan", "black", "bright")
    printcol(use_string, "blue", "black", "dim")
    printcol(use_string, "blue", "black", "normal")
    printcol(use_string, "blue", "black", "bright")
    printcol(use_string, "white", "black", "dim")
    printcol(use_string, "white", "black", "normal")
    printcol(use_string, "white", "black", "bright")
    printcol(use_string, "black", "white", "dim")
    printcol(use_string, "black", "white", "normal")
    printcol(use_string, "black", "white", "bright")
