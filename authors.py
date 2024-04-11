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


def get_authors() -> Tuple[str, str]:
    req = Request(URL, headers=HEADERS)
    with urlopen(req) as fd:
        for author_line in fd.readlines():
            author_line = author_line.decode("utf-8")
            tokens = author_line.split("<")
            email = tokens[1].strip()[:-1]
            tokens = tokens[0].strip().split("(")
            name = tokens[0]
            nickname = tokens[1][:-1]
            yield (nickname, name, f"mailto:{email}")
