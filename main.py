import sys
import time
import wikipediaapi
from rich.console import Console
from rich.prompt import Prompt


wiki_wiki = wikipediaapi.Wikipedia('MyProjectName (merlin@example.com)', 'en')

def print_main_screen():
    console = Console()
    
    console.clear()
    console.rule("[bold red] Wikiscraper")
    
    console.print("""
                  Welcome to Wikiscraper. A TUI application that lets 
                  you interact with the wikipedia-api for a distraction free 
                  Wikipedia experience. Made for terminal lovers!
                  
                  To get started...
                  """)
    
    page_title = console.input("""
                  Enter a topic you would like to explore. 
                  Ex python, lofi, fishing \n
                  """)
    return page_title


def search_topic():
    user_input = print_main_screen()
    page = wiki_wiki.page(user_input)

    disambig_phrases = [
        "may refer to",
        "most commonly refers to",
        "can refer to",
        "is a disambiguation page"
    ]

    if page.exists():
        if any(phrase in page.summary.lower() for phrase in disambig_phrases):
            print(f"'{user_input}' is a disambiguation page. Possible topics include:")
            for link_title in page.links.keys():
                print(f"- {link_title}")
        else:
            # if page is NOT an dismabigious page
            print(f"Title: {page.title}")
            print(f"Summary: {page.summary}")        
    else:
        # if page does not exist
        print(f"No page found for '{user_input}'.")


search_topic()


# page_py = wiki_wiki.page('Python_(programming_language)')

# def print_language_content():
#     user_input = input("Enter a programming language\n")

#     # Define the page to fetch
#     program_page = wiki_wiki.page(f"{user_input} (programming language)")

#     if program_page.exists():
#         # Print the summary (introductory paragraph)
#         print(program_page.summary)
#     else:
#         print("Page for: " + user_input + "not found")
#     # # Print full text of the page if needed
#     # print(program_page.text[:1000])  # First 1000 characters, for example


 

