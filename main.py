# Initialize API for English Wikipedia

import wikipediaapi

wiki_wiki = wikipediaapi.Wikipedia('MyProjectName (merlin@example.com)', 'en')




# page_py = wiki_wiki.page('Python_(programming_language)')

def print_language_content():
    user_input = input("Enter a programming language\n")

    # Define the page to fetch
    program_page = wiki_wiki.page(f"{user_input} (programming language)")

    # Print the summary (introductory paragraph)
    print(program_page.summary)

    # Print full text of the page if needed
    print(program_page.text[:1000])  # First 1000 characters, for example

print_language_content()