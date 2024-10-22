# Import of libraries
import pyfiglet
import random
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Categorizing font styles
font_categories = {
    "Basic": ["standard", "slant", "banner", "doom"],
    "Script": ["script", "dancing", "nvscript", "starwars"],
    "Fancy": ["3d", "big", "block", "puffy"],
    "Comic": ["cheese", "cyberlarge", "ghost", "larry3d"],
    "My Favourites": ["poison", "smkeyboard", "fraktur", "mono12"]
}

# Precompute all available styles once at the start
all_styles = [font for fonts in font_categories.values() for font in fonts]

# List available categories and styles
def list_categories():
    print(Fore.CYAN + "Available font categories:")
    for category, fonts in font_categories.items():
        print(f"{Fore.GREEN}{category}:")
        print(", ".join(Fore.YELLOW + font for font in fonts))
        
# Random font style choice (uses precomputed 'all_styles')
def get_random_style():
    return random.choice(all_styles)

# Font transformation
def generate_ascii_art(text, style):
    fig = pyfiglet.Figlet(font=style)
    return fig.renderText(text)

# Get valid font style input
def get_valid_style():
    all_styles = [font for fonts in font_categories.values() for font in fonts] + ['random']
    while True:
        style = input(Fore.BLUE + "Enter the style you want to use (or type 'random' for a random style): ")
        if style in all_styles:
            return style
        print(Fore.RED + "Invalid style. Please try again.")

def main():
    while True:
        print(Fore.MAGENTA + """Welcome to the ASCII Art Generator!
        You can use it to add style to footer of your emails or as banners in forums
        """)
        print()

        list_categories()

        # User input for desired text
        text = input(Fore.BLUE + "\nEnter the text you want to convert to ASCII art: ")

        # Get a valid style input
        style = get_valid_style()

        # Random font choice
        if style.lower() == 'random':
            style = get_random_style()
            print(Fore.CYAN + f"Randomly selected style: {style}")
        
        # Generate font from listed font styles
        try:
            ascii_art = generate_ascii_art(text, style)
            print(Fore.LIGHTWHITE_EX + "\nGenerating the best ASCII art for you...\n")
            print(ascii_art)
        except Exception as e:
            print(Fore.RED + f"An error occurred: {e}. Please make sure you entered a valid style.")

        # Ask if the user wants to try again
        retry = input(Fore.BLUE + "Hope you liked it!\nDo you want to try again? ('y' or any other key to exit): ").lower()
        if retry != 'y':
            print(Fore.GREEN + "Thank you for using the ASCII Art Generator! Goodbye!")
            break
main()