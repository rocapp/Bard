"""code_feedback.py: get feedback on a code project."""
import sys
from os import environ
from Bard import Chatbot
from pathlib import Path
from pypager.source import GeneratorSource
from pypager.pager import Pager
import re
import io

phrase = """
Could you give me feedback on this code?

{}
"""


def main():
    global phrase
    token = environ.get("BARD_TOKEN")
    chatbot = Chatbot(token)
    if len(sys.argv) > 1:
        fpath = sys.argv[1]
    else:
        fpath = input('Filepath to code: ')
    filepath = Path(fpath).absolute()
    with open(filepath, 'r') as f:
        code_str = f.read()
    complete_phrase = phrase.format(code_str)
    print(complete_phrase)
    feedback = chatbot.ask(complete_phrase)
    return feedback


if __name__ == '__main__':
    feedback = main()
