"""A wrapper for the colorama module."""
"""
Copyright 2019 Joshua Wise

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from colorama import init, Fore, Back, Style
import os


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
    # Convert the inputs into lowercase names to be checked
    fore_col = fore_col.lower()
    back_col = back_col.lower()
    shade = shade.lower()

    # Check if running from pycharm
    is_running_pycharm = "PYCHARM_HOSTED" in os.environ
    if is_running_pycharm:
        convert = False
        strip = False
    else:
        convert = None
        strip = None

    init(autoreset=True, convert=convert, strip=strip)  # Make sure the next print statement runs correctly
    # Define values for each style and colour
    shades = {"dim": Style.DIM, "bright": Style.BRIGHT, "normal": Style.NORMAL}  # When underline is available add Style.UNDERLINED
    fore_cols = {"red": Fore.RED, "light red": Fore.LIGHTRED_EX, "magenta": Fore.MAGENTA, "light magenta": Fore.LIGHTMAGENTA_EX, "yellow": Fore.YELLOW, "light yellow": Fore.LIGHTYELLOW_EX, "green": Fore.GREEN, "light green": Fore.LIGHTGREEN_EX, "blue": Fore.BLUE, "light blue": Fore.LIGHTBLUE_EX, "cyan": Fore.CYAN, "light cyan": Fore.LIGHTCYAN_EX, "black": Fore.BLACK}
    back_cols = {"red": Back.RED, "light red": Back.LIGHTRED_EX, "magenta": Back.MAGENTA, "light magenta": Back.LIGHTMAGENTA_EX, "yellow": Back.YELLOW, "light yellow": Back.LIGHTYELLOW_EX, "green": Back.GREEN, "light green": Back.LIGHTGREEN_EX, "blue": Back.BLUE, "light blue": Back.LIGHTBLUE_EX, "cyan": Back.CYAN, "light cyan": Back.LIGHTCYAN_EX, "white": Back.WHITE}
    
    # Check the shade of colour to use
    if shade in shades:
        shade = shades[shade]
    else:
        shade = Style.NORMAL
    
    # Check the foreground colour to use
    if fore_col in fore_cols:
        fore_col = fore_cols[fore_col]
    else:
        fore_col = Fore.WHITE
    
    # Check the background colour to use
    if back_col in back_cols:
        back_col = back_cols[back_col]
    else:
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


def inputcolour(text, prompt_fore_col=None, prompt_back_col=None, prompt_shade=None, input_fore_col=None, input_back_col=None, input_shade=None):
    """Returns input from a coloured input prompt.
    Arguments:
    text - The text to prompt the user for the desired input.
    prompt_fore_col - The colour of the text to print the prompt text in. Default: white, can be either of: red, light
    red, magenta, light Magenta, yellow, light yellow, green, light green, blue, light blue, cyan, light cyan, black or
    white
    prompt_back_col - The colour to print the prompt text onto. Default: black, can be either of: red, light red,
    magenta, light magenta, yellow, light yellow, green, light green, blue, light blue, cyan, light cyan, black or white
    prompt_shade - The shade of the colour to use for the input prompt. Default: normal, can be either of: dim, normal,
    bright
    input_fore_col - The colour of the text to print the user input in. Default: white, can be either of: red, light
    red, magenta, light Magenta, yellow, light yellow, green, light green, blue, light blue, cyan, light cyan, black or
    white
    input_back_col - The colour to print the user input onto. Default: black, can be either of: red, light red,
    magenta, light magenta, yellow, light yellow, green, light green, blue, light blue, cyan, light cyan, black or white
    input_shade - The shade of the colour to use for the text entered by the user. Default: normal, can be either of:
    dim, normal, bright"""
    # Handle None keywords
    if prompt_fore_col is None:
        prompt_fore_col = "white"
    if prompt_back_col is None:
        prompt_back_col = "black"
    if prompt_shade is None:
        prompt_shade = "normal"
    if input_fore_col is None:
        input_fore_col = "white"
    if input_back_col is None:
        input_back_col = "black"
    if input_shade is None:
        input_shade = "normal"

    # Convert the inputs into lowercase names to be checked
    prompt_fore_col = prompt_fore_col.lower()
    prompt_back_col = prompt_back_col.lower()
    prompt_shade = prompt_shade.lower()
    input_fore_col = input_fore_col.lower()
    input_back_col = input_back_col.lower()
    input_shade = input_shade.lower()

    # Check if running from pycharm
    is_running_pycharm = "PYCHARM_HOSTED" in os.environ
    if is_running_pycharm:
        convert = False
        strip = False
    else:
        convert = None
        strip = None

    init(autoreset=False, convert=convert, strip=strip)  # Disable autoreset to colour the prompt correctly
    
    # Define values for each style and colour
    shades = {"dim": Style.DIM, "bright": Style.BRIGHT, "normal": Style.NORMAL}  # When underline is available add Style.UNDERLINED
    fore_cols = {"red": Fore.RED, "light red": Fore.LIGHTRED_EX, "magenta": Fore.MAGENTA, "light magenta": Fore.LIGHTMAGENTA_EX, "yellow": Fore.YELLOW, "light yellow": Fore.LIGHTYELLOW_EX, "green": Fore.GREEN, "light green": Fore.LIGHTGREEN_EX, "blue": Fore.BLUE, "light blue": Fore.LIGHTBLUE_EX, "cyan": Fore.CYAN, "light cyan": Fore.LIGHTCYAN_EX, "black": Fore.BLACK}
    back_cols = {"red": Back.RED, "light red": Back.LIGHTRED_EX, "magenta": Back.MAGENTA, "light magenta": Back.LIGHTMAGENTA_EX, "yellow": Back.YELLOW, "light yellow": Back.LIGHTYELLOW_EX, "green": Back.GREEN, "light green": Back.LIGHTGREEN_EX, "blue": Back.BLUE, "light blue": Back.LIGHTBLUE_EX, "cyan": Back.CYAN, "light cyan": Back.LIGHTCYAN_EX, "white": Back.WHITE}
    
    # Check which shade of colour to use for the input prompt and the user input.
    if prompt_shade in shades:
        prompt_shade = shades[prompt_shade]
    else:
        prompt_shade = Style.NORMAL
    
    if input_shade in shades:
        input_shade = shades[input_shade]
    else:
        input_shade = Style.NORMAL
    

    # Begin checking the colour required
    if prompt_fore_col == "red":
        prompt_fore_col = Fore.RED
    elif prompt_fore_col == "light red":  # Same as Style.BRIGHT
        prompt_fore_col = Fore.LIGHTRED_EX

    elif prompt_fore_col == "magenta":
        prompt_fore_col = Fore.MAGENTA
    elif prompt_fore_col == "light magenta":
        prompt_fore_col = Fore.LIGHTMAGENTA_EX

    elif prompt_fore_col == "yellow":
        prompt_fore_col = Fore.YELLOW
    elif prompt_fore_col == "light yellow":
        prompt_fore_col = Fore.LIGHTYELLOW_EX

    elif prompt_fore_col == "green":
        prompt_fore_col = Fore.GREEN
    elif prompt_fore_col == "light green":
        prompt_fore_col = Fore.LIGHTGREEN_EX

    elif prompt_fore_col == "blue":
        prompt_fore_col = Fore.BLUE
    elif prompt_fore_col == "light blue":
        prompt_fore_col = Fore.LIGHTBLUE_EX

    elif prompt_fore_col == "cyan":
        prompt_fore_col = Fore.CYAN
    elif prompt_fore_col == "light cyan":
        prompt_fore_col = Fore.LIGHTCYAN_EX

    elif prompt_fore_col == "black":
        prompt_fore_col = Fore.BLACK
    else:  # If white or other to prevent errors
        prompt_fore_col = Fore.WHITE

    # Then check the background colour required
    if prompt_back_col == "red":
        prompt_back_col = Back.RED
    elif prompt_back_col == "light red":
        prompt_back_col = Back.LIGHTRED_EX

    elif prompt_back_col == "magenta":
        prompt_back_col = Back.MAGENTA
    elif prompt_back_col == "light magenta":
        prompt_back_col = Back.LIGHTMAGENTA_EX

    elif prompt_back_col == "yellow":
        prompt_back_col = Back.YELLOW
    elif prompt_back_col == "light yellow":
        prompt_back_col = Back.LIGHTYELLOW_EX

    elif prompt_back_col == "green":
        prompt_back_col = Back.GREEN
    elif prompt_back_col == "light green":
        prompt_back_col = Back.LIGHTGREEN_EX

    elif prompt_back_col == "blue":
        prompt_back_col = Back.BLUE
    elif prompt_back_col == "light blue":
        prompt_back_col = Back.LIGHTBLUE_EX

    elif prompt_back_col == "cyan":
        prompt_back_col = Back.CYAN
    elif prompt_back_col == "light cyan":
        prompt_back_col = Back.LIGHTCYAN_EX

    elif prompt_back_col == "white":  # White only comes in one shade
        prompt_back_col = Back.WHITE
    else:  # If black or other to prevent errors
        prompt_back_col = Back.BLACK

    # Check the input text fore colour
    if input_fore_col == "red":
        input_fore_col = Fore.RED
    elif input_fore_col == "light red":  # Same as Style.BRIGHT
        input_fore_col = Fore.LIGHTRED_EX

    elif input_fore_col == "magenta":
        input_fore_col = Fore.MAGENTA
    elif input_fore_col == "light magenta":
        input_fore_col = Fore.LIGHTMAGENTA_EX

    elif input_fore_col == "yellow":
        input_fore_col = Fore.YELLOW
    elif input_fore_col == "light yellow":
        input_fore_col = Fore.LIGHTYELLOW_EX

    elif input_fore_col == "green":
        input_fore_col = Fore.GREEN
    elif input_fore_col == "light green":
        input_fore_col = Fore.LIGHTGREEN_EX

    elif input_fore_col == "blue":
        input_fore_col = Fore.BLUE
    elif prompt_fore_col == "light blue":
        input_fore_col = Fore.LIGHTBLUE_EX

    elif input_fore_col == "cyan":
        input_fore_col = Fore.CYAN
    elif input_fore_col == "light cyan":
        input_fore_col = Fore.LIGHTCYAN_EX

    elif input_fore_col == "black":
        input_fore_col = Fore.BLACK
    else:  # If white or other to prevent errors
        input_fore_col = Fore.WHITE

    # Then check the input background colour required
    if input_back_col == "red":
        input_back_col = Back.RED
    elif input_back_col == "light red":
        input_back_col = Back.LIGHTRED_EX

    elif input_back_col == "magenta":
        input_back_col = Back.MAGENTA
    elif input_back_col == "light magenta":
        input_back_col = Back.LIGHTMAGENTA_EX

    elif input_back_col == "yellow":
        input_back_col = Back.YELLOW
    elif input_back_col == "light yellow":
        input_back_col = Back.LIGHTYELLOW_EX

    elif input_back_col == "green":
        input_back_col = Back.GREEN
    elif input_back_col == "light green":
        input_back_col = Back.LIGHTGREEN_EX

    elif input_back_col == "blue":
        input_back_col = Back.BLUE
    elif input_back_col == "light blue":
        input_back_col = Back.LIGHTBLUE_EX

    elif input_back_col == "cyan":
        input_back_col = Back.CYAN
    elif input_back_col == "light cyan":
        input_back_col = Back.LIGHTCYAN_EX

    elif input_back_col == "white":  # White only comes in one shade
        input_back_col = Back.WHITE
    else:  # If black or other to prevent errors
        input_back_col = Back.BLACK

    print(prompt_shade + prompt_fore_col + prompt_back_col, end='')
    show_text = str(text) + " " + Style.RESET_ALL  # Force the text to string and add a space for styling
    show_text + input_shade + input_fore_col + input_back_col
    return_text = input(show_text)  # Show the text
    print(Style.RESET_ALL)  # Reset for normal
    return return_text


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
