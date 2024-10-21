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

def get_random_style():
    all_styles = [font for fonts in font_categories.values() for font in fonts]
    return random.choice(all_styles)

def main():

    print("Welcome to text the ASCII Art Generator!")
    print("You can use it to add style to footer of your emails or as banners in forums")
    print()

    list_categories()

main()