import webbrowser
from voiceReader import speak


def search_web_direct(query):
    """Opens a browser search for the given query, and shows the
    search URL in the terminal."""
    url = f"https://www.google.com/search?q={query.replace(' ', '+')}"

    speak(f"Searching the web for {query}.")


    print(f"Search query : {query}")
    print(f"Search URL   : {url}")
  

    webbrowser.open(url)
