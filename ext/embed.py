"""Allows embedding generic iframes into the docs.
"""

from docutils import nodes
from docutils.parsers.rst import Directive
from jinja2 import BaseLoader, Environment
from sphinx.application import Sphinx

TEMPLATE = """
<div id="embed"{% if klass %}
    class="{{ klass }}"{% endif %}{% if style %}
    style="{{ style }}"{% endif %}>
</div>
<script>
function applyBlob(element, blob) {
  blob.text().then(value => element.innerHTML = value);
}

fetch('{{ url }}')
  .then(
    resp => resp.status === 200 ? resp.blob() :
      Promise.reject('something went wrong')
  )
  .then(blob => {
    const div = document.getElementById('embed');
    applyBlob(div, blob);
  })
  .catch(() => alert('oh no!'));
</script>
"""


def _split(a):
    return {s.strip() for s in (a or "").split(",")}


def _to_boolean(argument: str) -> str:
    return argument.lower().strip() == "true"


class Embed(Directive):
    arguments = 1
    has_content = True
    final_argument_whitespace = False
    option_spec = {
        "class": lambda a: a.strip(),
        "style": lambda a: a.strip(),
    }

    def run(self):
        url = self.content[0]
        klass = self.options.get("class")
        style = self.options.get("style")

        template = Environment(loader=BaseLoader).from_string(TEMPLATE)
        out = template.render(
            url=url,
            klass=klass,
            style=style,
        )
        # Use a raw pass-through node
        para = nodes.raw("", out, format="html")
        return [para]


def setup(app: Sphinx):
    app.add_directive("embed", Embed)

    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
