import os
from typing import Tuple
from urllib.request import Request, urlopen

REPO_OWNER = "pythonpe"
REPO = "pythonpe-blog"
BRANCH = "main"
AUTHORS_FILENAME = "AUTHORS"
HEADERS = {"Accept": "application/vnd.github.VERSION.raw"}
URL = (
    f"https://api.github.com/repos/{REPO_OWNER}/{REPO}/contents/"
    f"{AUTHORS_FILENAME}?ref={BRANCH}"
)
AUTHORS_FILENAME = "AUTHORS"
AUTHORS_FILEPATH = os.path.join(os.path.dirname(__file__), AUTHORS_FILENAME)


def get_authors() -> Tuple[str, str]:
    author_lines = set()
    with open(AUTHORS_FILEPATH, "r") as fd:
        author_lines = {line for line in fd.readlines()}

    req = Request(URL, headers=HEADERS)
    with urlopen(req) as fd:
        author_lines.update({line.decode("utf-8") for line in fd.readlines()})

    for author_line in author_lines:
        tokens = author_line.split("<")
        email = tokens[1].strip()[:-1]
        tokens = tokens[0].strip().split("(")
        name = tokens[0]
        nickname = tokens[1][:-1]
        yield (nickname, name, f"mailto:{email}")
