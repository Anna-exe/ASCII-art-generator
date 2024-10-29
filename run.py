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
    "My Favourites": ["poison", "smkeyboard", "fraktur", "bloody"],
}

# Precompute all available styles once at the start
all_styles = [font for fonts in font_categories.values() for font in fonts]


def get_text_input():
    """Get valid text from user"""
    while True:
        text = input("\nEnter the text you want to convert to ASCII art:\n")
        # Check if input is not empty after stripping whitespace
        if text.strip():
            return text
        slow_print("Error: Please enter some text to generate ASCII art.\n", Fore.RED)


# Define rainbow colors in sequence
rainbow_colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]


def apply_rainbow_gradient(text):
    """Apply rainbow colors to text"""
    colored_text = ""
    color_count = len(rainbow_colors)

    # Loop through each character and apply a rainbow color sequentially
    for i, char in enumerate(text):
        colored_text += rainbow_colors[i % color_count] + char

    return colored_text


def slow_print(text, color=Fore.WHITE, delay=0.05):
    """Print messages with typing effect"""
    # Add color explicitly to each character to maintain color consistency
    for char in text:
        print(color + char, end="", flush=True)
        time.sleep(delay)


def list_categories():
    """List available categories and styles"""
    print(Fore.CYAN + "Available font categories:\n")
    for category, fonts in font_categories.items():
        print(f"{Fore.GREEN}{category}:")
        print(", ".join(Fore.YELLOW + font for font in fonts))
        print()  # Spacing between categories


def get_random_style():
    """Random font style choice (uses precomputed 'all_styles')"""
    return random.choice(all_styles)


def generate_ascii_art(text, style):
    """Font transformation"""
    fig = pyfiglet.Figlet(font=style)
    return fig.renderText(text)


def get_valid_style():
    """Get valid font style input (uses precomputed 'all_styles')"""
    while True:
        style = input(
            Fore.BLUE + "Enter the style you want to use (or type 'random' for a random style): ")
        if style in all_styles + ["random"]:
            return style
        slow_print("Invalid style. Available categories and styles are listed below:\n", Fore.RED)
        list_categories()


def prompt_retry():
    """Prompt the user to try again or exit"""
    return (
        input(
            Fore.BLUE + "\nDo you want to try again? ('y' for yes or any other key to exit): "
        ).lower() == "y"
    )
    

def main():
    """Main function"""
    slow_print("Welcome to the ASCII Art Generator!\n", Fore.CYAN)
    slow_print("You can use it to add style to your digital designs\n", Fore.MAGENTA)

    while True:
        # List font categories at the beginning
        list_categories()

        # Get a valid style input first
        style = get_valid_style()

        # Random font choice
        if style.lower() == "random":
            style = get_random_style()
            slow_print(f"Randomly selected style: {style}", Fore.CYAN)

        # Then, user input for desired text
        text = get_text_input()

        # Generate ASCII art and display it with a rainbow gradient
        try:
            ascii_art = generate_ascii_art(text, style)
            slow_print("\nGenerating the best ASCII art for you...\n", Fore.YELLOW)

            # Apply rainbow gradient to the ASCII art
            rainbow_ascii_art = apply_rainbow_gradient(ascii_art)
            print(rainbow_ascii_art)
            slow_print("Hope you liked it!\n", Fore.GREEN)
            slow_print("""***Hint: To display your ASCII art properly,
use fonts with equal spacing like 'Fixed width'
in Gmail or 'Miriam Fixed' in Word""",
            Fore.YELLOW)
        except Exception as e:
            slow_print(f"""An error occurred: {e}.
            Please make sure you entered a valid style.""", Fore.RED)

        # Ask if the user wants to try again
        if not prompt_retry():
            slow_print("\nThank you for using the ASCII Art Generator! Goodbye!", Fore.GREEN)
            break


main()
