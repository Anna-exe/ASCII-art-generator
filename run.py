# Import of libraries
import time
import pyfiglet
import random
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Categorizing font styles
font_categories = {
    "Basic": ["standard", "slant", "banner", "doom"],
    "Script": ["script", "invita", "nvscript", "starwars"],
    "Fancy": ["alligator", "big", "block", "puffy"],
    "Comic": ["avatar", "cyberlarge", "ghost", "larry3d"],
    "My Favourites": ["poison", "smkeyboard", "fraktur", "bloody"]
}

# Precompute all available styles once at the start
all_styles = [font for fonts in font_categories.values() for font in fonts]

# Define rainbow colors in sequence
rainbow_colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]

# Function to apply rainbow colors to text
def apply_rainbow_gradient(text):
    colored_text = ""
    color_count = len(rainbow_colors)
    
    # Loop through each character and apply a rainbow color sequentially
    for i, char in enumerate(text):
        colored_text += rainbow_colors[i % color_count] + char
    
    return colored_text

# Function to print messages with a typing effect
def slow_print(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)

# List available categories and styles
def list_categories():
    slow_print("Available font categories:\n", Fore.CYAN)
    for category, fonts in font_categories.items():
        print(f"{Fore.GREEN}{category}:")
        print(", ".join(Fore.YELLOW + font for font in fonts))
        print() # Spacing between categories
        
# Random font style choice (uses precomputed 'all_styles')
def get_random_style():
    return random.choice(all_styles)

# Font transformation
def generate_ascii_art(text, style):
    fig = pyfiglet.Figlet(font=style)
    return fig.renderText(text)

# Get valid font style input (uses precomputed 'all_styles')
def get_valid_style():
    while True:
        style = input(Fore.BLUE + "Enter the style you want to use (or type 'random' for a random style): ")
        if style in all_styles + ['random']:
            return style
        slow_print(Fore.RED + "Invalid style. Available categories and styles are listed below:\n")
        list_categories()

# Function to prompt the user to try again or exit
def prompt_retry():
    return input(Fore.BLUE + "\nDo you want to try again? ('y' for yes or any other key to exit): ").lower() == 'y'

def slow_print(text, color=Fore.WHITE, delay=0.05):
    # Add color explicitly to each character to maintain color consistency
    for char in text:
        print(color + char, end='', flush=True)
        time.sleep(delay)

def main():
    slow_print("Welcome to the ASCII Art Generator!", Fore.CYAN)
    slow_print("You can use it to add style to footer of your emails or as banners in forums\n", Fore.MAGENTA)
    
    while True:
        # List font categories at the beginning
        list_categories()

        # Get a valid style input first
        style = get_valid_style()

        # Random font choice
        if style.lower() == 'random':
            style = get_random_style()
            slow_print(f"Randomly selected style: {style}", Fore.CYAN )

        # Then, user input for desired text
        text = input("\nEnter the text you want to convert to ASCII art: ", Fore.BLUE)

        # Generate ASCII art and display it with a rainbow gradient
        try:
            ascii_art = generate_ascii_art(text, style)
            slow_print("\nGenerating the best ASCII art for you...\n", Fore.YELLOW)
            
            # Apply rainbow gradient to the ASCII art
            rainbow_ascii_art = apply_rainbow_gradient(ascii_art)
            print(rainbow_ascii_art)
            slow_print("***Hint: To display your ASCII art properly, use fonts with equal spacing like 'Fixed width' in Gmail or 'Miriam Fixed' in Word\n", Fore.YELLOW)
        except Exception as e:
            slow_print(f"An error occurred: {e}. Please make sure you entered a valid style.", Fore.RED)

        # Ask if the user wants to try again
        if not prompt_retry():
            slow_print("\nThank you for using the ASCII Art Generator! Goodbye!", Fore.GREEN )
            break
main()