"""A directive to generate an image tag with a Gravatar pic.
"""

import os
import urllib.request
from hashlib import sha256

from ablog.commands import find_confdir, read_conf
from docutils import nodes
from docutils.parsers.rst import Directive
from jinja2 import BaseLoader, Environment
from libgravatar import Gravatar
from PIL import Image, ImageDraw
from sphinx.application import Sphinx
from sphinx.util import logging

logger = logging.getLogger(__name__)

GRAVATAR_TEMPLATE = """
<div class="{{ klass }}">
    <img src=/{{ url }}
    {% if align %} align="{{ align }}"{% endif %}
    {% if klass %} class="{{ klass }}"{% endif %}
    {% if style %} style="{{ style }}"{% endif %}
    {% if width %} width="{{ width }}" height="{{ width }}"{% endif %}>
</div>
"""
FILENAME_EXT = ".png"


class GravatarError(Exception):
    pass


def _to_boolean(argument: str) -> str:
    # Weird behavior, but true~
    return argument is None


class GravatarImage(Directive):
    arguments = 1
    has_content = True
    final_argument_whitespace = False
    option_spec = {
        "align": lambda a: a.strip(),
        "class": lambda a: a.strip(),
        "style": lambda a: a.strip(),
        "width": lambda a: a.strip(),
        "with-circle-clip": _to_boolean,
        "with-grayscale": _to_boolean,
        "static-subdir": lambda a: a.strip(),
    }

    def _process_image(
        self, filepath: str, with_circle_clip: bool, with_grayscale: bool
    ):
        original_image = Image.open(filepath)

        if with_grayscale:
            # Convert the original image to grayscale
            original_image = original_image.convert("L")

        if with_circle_clip:
            # Create a mask image with a white circle on a black background
            mask = Image.new("L", original_image.size, 0)
            draw = ImageDraw.Draw(mask)
            width, height = original_image.size
            draw.ellipse((0, 0, width, height), fill=255)

            # Convert the mask to use an alpha channel
            result = original_image.copy()
            result.putalpha(mask)
        else:
            result = original_image
        result.save(filepath)

    def run(self):
        email = self.content[0]
        align = self.options.get("align")
        klass = self.options.get("class")
        style = self.options.get("style")
        width = self.options.get("width")
        with_circle_clip = self.options.get("with-circle-clip")
        with_grayscale = self.options.get("with-grayscale")
        static_subdir = self.options.get("static-subdir")
        confdir = find_confdir()
        conf = read_conf(confdir)
        html_static_path = getattr(conf, "html_static_path", [])

        if len(html_static_path) == 0:
            raise GravatarError(
                "html_static_path should have at least one path configured"
            )

        # We choose the first path as the default path for the image
        save_path = os.path.join(html_static_path[0], static_subdir)

        # Try to make the dir if it doesn't exist
        os.makedirs(save_path, exist_ok=True)

        logger.info(f"Gravatar: Getting Gravatar image for email: {email}")
        url = Gravatar(email).get_image()
        if width is not None:
            url = f"{url}?s={width}"
            logger.info(f"Gravatar: Requesting Gravatar image from URL: {url}")

        filename = sha256(url.encode()).digest().hex()
        filename = f"{filename}{FILENAME_EXT}"
        save_path = os.path.join(save_path, filename)
        urllib.request.urlretrieve(url, save_path)
        logger.info(f"Gravatar: Retrieving image into: {save_path}")

        if with_circle_clip or with_grayscale:
            self._process_image(save_path, with_circle_clip, with_grayscale)
            logger.info("Gravatar: Applying image post-processing")

        template = Environment(
            loader=BaseLoader, trim_blocks=True, lstrip_blocks=True
        ).from_string(GRAVATAR_TEMPLATE)

        out = template.render(
            url=save_path,
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
