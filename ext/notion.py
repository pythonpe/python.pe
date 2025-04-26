"""A directive to generate an iframe with a Notion page."""

from docutils import nodes
from docutils.parsers.rst import Directive
from sphinx.application import Sphinx
from sphinx.util import logging

logger = logging.getLogger(__name__)

TEMPLATE: str = """
<iframe src="{url}" width="100%" height="1200" frameborder="0" allowfullscreen>
</iframe>
"""


class Notion(Directive):
    has_content = True
    final_argument_whitespace = False

    def run(self):
        if not self.content:
            raise self.error("Notion directive requires a URL")
        if len(self.content) > 1:
            raise self.error("Notion directive only accepts a single URL")
        url = self.content[0]
        # Basic validation that it's a Notion URL
        if not url.startswith(("https://notion.site", "https://www.notion.so")) and "notion" not in url:
            raise self.error("URL does not appear to be a valid Notion URL")

        para = nodes.raw(
         para = nodes.raw(
-            "", TEMPLATE.format(url=url), format="html"
+            "", TEMPLATE.format(url=urllib.parse.quote(url, safe=":/?&=+")), format="html"
         )
        )
        return [para]


def setup(app: Sphinx):
    app.add_directive("notion",Notion)

    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
