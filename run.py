# Import ASCII font art library
import pyfiglet
# Import randomizer
import random

# Categorizing font styles
font_categories = {
    "Basic": ["standard", "slant", "banner", "doom"],
    "Script": ["script", "dancing", "nvscript", "starwars"],
    "Fancy": ["3d", "big", "block", "puffy"],
    "Comic": ["cheese", "cyberlarge", "ghost", "larry3d"],
    "My Favourites": ["poison", "smkeyboard", "fraktur", "katakana", "mono12"]
}

# List available categories and styles
def list_categories():
    print("Available font categories:")
    for category, fonts in font_categories.items():
        print(f"\n{category}:")
        print(", ".join(fonts))
        
# Random font style choice
def get_random_style():
    all_styles = [font for fonts in font_categories.values() for font in fonts]
    return random.choice(all_styles)

# Font transformation
def generate_ascii_art(text, style):
    fig = pyfiglet.Figlet(font=style)
    return fig.renderText(text)

# Get valid font style input
def get_valid_style():
    all_styles = [font for fonts in font_categories.values() for font in fonts] + ['random']
    while True:
        style = input("Enter the style you want to use (or type 'random' for a random style): ")
        if style in all_styles:
            return style
        print("Invalid style. Please try again.")

def main():
    while True:
        print("Welcome to the ASCII Art Generator!")
        print("You can use it to add style to footer of your emails or as banners in forums")
        print()

        list_categories()

        # User input for desired text
        text = input("\nEnter the text you want to convert to ASCII art: ")

        # Get a valid style input
        style = get_valid_style()

        # Random font choice
        if style.lower() == 'random':
            style = get_random_style()
            print(f"Randomly selected style: {style}")
        
        # Generate font from listed font styles
        try:
            ascii_art = generate_ascii_art(text, style)
            print("\nGenerating the best ASCII art for you...\n")
            print(ascii_art)
        except Exception as e:
            print(f"An error occurred: {e}. Please make sure you entered a valid style.")

        # Ask if the user wants to try again
        retry = input("Hope you liked it!\nDo you want to try again? ('y' or any other key to exit): ").lower()
        if retry != 'y':
            print("Thank you for using the ASCII Art Generator! Goodbye!")
            break
main()