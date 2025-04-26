"""A directive to generate an iframe with a Notion page."""

from docutils import nodes
from docutils.parsers.rst import Directive
from sphinx.application import Sphinx
from sphinx.util import logging

logger = logging.getLogger(__name__)

TEMPLATE: str = """
<iframe src="{url}" width="100%" height="1200" frameborder="0" allowfullscreen />
"""


class Notion(Directive):
    has_content = True
    final_argument_whitespace = False

    def run(self):
        para = nodes.raw(
            "", TEMPLATE.format(url=self.content[0]), format="html"
        )
        return [para]


def setup(app: Sphinx):
    app.add_directive("notion",Notion)

    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
