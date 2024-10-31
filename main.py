# Initialize API for English Wikipedia

import wikipediaapi

wiki_wiki = wikipediaapi.Wikipedia('MyProjectName (merlin@example.com)', 'en')

page_py = wiki_wiki.page('Python_(programming_language)')

# Define the page to fetch
page = wiki_wiki.page("Python (programming language)")

# Print the summary (introductory paragraph)
print(page.summary)

# Print full text of the page if needed
print(page.text[:1000])  # First 1000 characters, for example