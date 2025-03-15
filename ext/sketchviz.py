"""A directive to generate an embedded svg image using Graphviz/Sketchviz
backend parsers
"""

import hashlib
import os
import subprocess
from tempfile import NamedTemporaryFile

from ablog.commands import find_confdir, read_conf
from docutils import nodes
from docutils.parsers.rst import Directive
from jinja2 import BaseLoader, Environment
from sphinx.application import Sphinx
from sphinx.util import logging

logger = logging.getLogger(__name__)

TEMPLATE = """
<div class="sketchviz-image">
    <object type="image/svg+xml" data="/{{ url }}"></object>
</div>
"""
FILENAME_EXT = ".svg"


class SketchvizError(Exception):
    pass


class Sketchviz(Directive):
    arguments = 1
    has_content = True
    final_argument_whitespace = False
    option_spec = {
        "static-subdir": lambda a: a.strip(),
    }

    def run(self):
        static_subdir = self.options.get("static-subdir", "images/sketchviz")
        confdir = find_confdir()
        conf = read_conf(confdir)
        html_static_path = getattr(conf, "html_static_path", [])

        if len(html_static_path) == 0:
            raise SketchvizError(
                "html_static_path should have at least one path configured"
            )

        # We choose the first path as the default path for the image
        save_path = os.path.join(html_static_path[0], static_subdir)

        # Try to make the dir if it doesn't exist
        os.makedirs(save_path, exist_ok=True)

        temp_name = None
        h = hashlib.new("sha256")
        with NamedTemporaryFile(
            mode="w", encoding="utf-8", delete=False, delete_on_close=False
        ) as fd:
            for content in self.content:
                line = f"{content}\n"
                h.update(line.encode())
                fd.write(line)
            temp_name = fd.name

        filename = h.digest().hex()
        filename = f"{filename}{FILENAME_EXT}"
        save_path = os.path.join(save_path, filename)
        # TODO: add a proper way to alert user when this binary is not found
        binary_path = os.environ.get("SKETCHVIZ_BINARY")
        subprocess.run([binary_path, temp_name, save_path], check=True)
        os.remove(temp_name)
        logger.info(f"Sketchviz: Created SVG image: {save_path}")

        template = Environment(loader=BaseLoader).from_string(TEMPLATE)

        out = template.render(url=save_path)
        # User a raw pass-through node
        para = nodes.raw("", out, format="html")
        return [para]


def setup(app: Sphinx):
    app.add_directive("sketchviz", Sketchviz)

    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
