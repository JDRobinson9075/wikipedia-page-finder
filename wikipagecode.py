import wikipediaapi
import webbrowser

def open_wikipedia_page(page_title):
    """
    Opens the Wikipedia page for the given title in the browser.

    Args:
        page_title (str): The title of the page. Can be a short form (e.g., "UK" for "United Kingdom").
    """
    wiki_wiki = wikipediaapi.Wikipedia(
        language='en',
        extract_format=wikipediaapi.ExtractFormat.WIKI,
        user_agent='Python-wikipediasearcher/3.11'
    )

    page = wiki_wiki.page(page_title)
    if page.exists():
        url = page.fullurl
        webbrowser.open(url)
        print(f"Redirecting to the Wikipedia page for '{page_title}'...")
    else:
        print(f"The page '{page_title}' does not exist on Wikipedia.")

def main():
    """
    Prompts the user continuously for a Wikipedia page title.
    Typing 'exit' will end the program.
    """
    while True:
        page_title = input("Enter a Wikipedia page title (or type 'exit' to quit): ")

        if page_title.lower() == "exit":
            print("Exiting the program.")
            break

        open_wikipedia_page(page_title)

if __name__ == "__main__":
    """
    Entry point for the program. 
    Calls the main function to start the user interaction loop.
    """
    main()


