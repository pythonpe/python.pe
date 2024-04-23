"""A directive to generate an image tag with a Gravatar pic.
"""

from docutils import nodes
from docutils.parsers.rst import Directive
from libgravatar import Gravatar
from sphinx.application import Sphinx
from sphinx.util import logging

logger = logging.getLogger(__name__)


def _split(value: str) -> list:
    return [v.strip() for v in value.split(",")]


class GravatarImage(Directive):
    arguments = 1
    has_content = True
    final_argument_whitespace = False
    option_spec = {
        "alt": lambda a: a.strip(),
        "class": _split,
        "width": lambda a: a.strip(),
    }

    def run(self):
        email = self.content[0]
        alt = self.options.get("alt", "Python developer")
        klass = self.options.get("class")
        width = self.options.get("width")

        logger.info(f"Getting Gravatar image for email: {email}")
        url = Gravatar(email).get_image()
        if width is not None:
            url = f"{url}?s={width}"
        logger.info(f"Got image URL: {url}")

        data = {}
        if klass is not None:
            data['classes'] = klass

        image = nodes.image(alt=alt, classes=klass, uri=url)
        return [image]


def setup(app: Sphinx):
    app.add_directive("gravatar", GravatarImage)

    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
