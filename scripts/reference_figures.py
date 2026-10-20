"""Native HTML and SVG figures from Paul's captured Meta reference.

Four templates retain the supplied static DOM, utility classes and SVG paths.
The flywheel follows Paul's later minimal diagram with native, localized labels.
Technical design notes and source font styles are removed. All visible copy is
localized in EN, PT and ES; SVG and glyph icons are decorative. Source card order
is Trust, Asymmetry, Model, Flywheel, Moats. The public API retains its existing
Trust, Model, Asymmetry, Flywheel, Moats numbering.

API: reference_figure(number, lang, dark=False) -> HTML
"""

from html import escape
import json
from pathlib import Path
import re


_ROOT = Path(__file__).resolve().parents[1]
_TEMPLATES = Path(__file__).resolve().parent / "templates" / "native-figures"
COPY = json.loads((_ROOT / "content" / "native-figure-copy.json").read_text(encoding="utf-8"))
FIGURES = {
    1: ("trust", 1000),
    2: ("model", 1000),
    3: ("asymmetry", 1000),
    4: ("flywheel", 1000),
    5: ("moats", 1000),
}
_TOKEN = re.compile(r"\{\{t(\d{2})\}\}")


def reference_figure(n, lang, dark=False):
    """Render a native figure, retaining the existing site-slot API.

    ``dark`` is retained for existing call sites. Figure text remains normal
    accessible HTML. Paul requested no external captions or number badges.
    """
    kind, max_width = FIGURES[n]
    copy = COPY[lang][kind]
    template = (_TEMPLATES / f"{kind}.html").read_text(encoding="utf-8")
    markup = _TOKEN.sub(lambda match: escape(copy["texts"][int(match.group(1))], quote=True), template)
    classes = "reference-figure" + (" reference-figure--dark" if dark else "")
    return (
        f'<figure class="{classes}" style="--figure-max:{max_width}px">'
        f'<div class="native-diagram" data-kind="{kind}">{markup}</div>'
        '</figure>'
    )
