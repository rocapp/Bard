"""code_feedback.py: get feedback on a code project."""
import sys
from os import environ
from Bard import Chatbot
from pathlib import Path
from pypager.source import GeneratorSource
from pypager.pager import Pager

phrase = """
Could you give me feedback on this code?
```
{}
```
"""


def main():
    global phrase
    token = environ.get("BARD_TOKEN")
    chatbot = Chatbot(token)
    filepath = Path(sys.argv[1]).absolute()
    code_str = filepath.read_text()
    complete_phrase = phrase.format(code_str)
    feedback = chatbot.ask(complete_phrase)
    return feedback


if __name__ == '__main__':
    feedback = main()
    pager = Pager()
    pager.add_source(GeneratorSource(main()))
    pager.run()
