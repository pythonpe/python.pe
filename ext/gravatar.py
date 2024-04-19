"""A directive to generate an image tag with a Gravatar pic.
"""

from docutils import nodes
from docutils.parsers.rst import Directive
from jinja2 import BaseLoader, Environment
from libgravatar import Gravatar
from sphinx.application import Sphinx
from sphinx.util import logging

logger = logging.getLogger(__name__)

GRAVATAR_TEMPLATE = """
<div class="{{ klass }}">
    <img src={{ url }}
    {% if align %} align="{{ align }}"{% endif %}
    {% if klass %} class="{{ klass }}"{% endif %}
    {% if style %} style="{{ style }}"{% endif %}
    {% if width %} width="{{ width }}" height="{{ width }}"{% endif %}>
</div>
"""


class GravatarImage(Directive):
    arguments = 1
    has_content = True
    final_argument_whitespace = False
    option_spec = {
        "align": lambda a: a.strip(),
        "class": lambda a: a.strip(),
        "style": lambda a: a.strip(),
        "width": lambda a: a.strip(),
    }

    def run(self):
        email = self.content[0]
        align = self.options.get("align")
        klass = self.options.get("class")
        style = self.options.get("style")
        width = self.options.get("width")

        logger.info(f"Getting Gravatar image for email: {email}")
        url = Gravatar(email).get_image()
        if width is not None:
            url = f"{url}?s={width}"
        logger.info(f"Got image URL: {url}")

        template = Environment(
            loader=BaseLoader, trim_blocks=True, lstrip_blocks=True
        ).from_string(GRAVATAR_TEMPLATE)

        out = template.render(
            url=url,
            align=align,
            klass=klass,
            style=style,
            width=width,
        )
        # User a raw pass-through node
        para = nodes.raw("", out, format="html")
        return [para]


def setup(app: Sphinx):
    app.add_directive("gravatar", GravatarImage)

    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
