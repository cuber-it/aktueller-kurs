#!/usr/bin/env python3
"""
md2pdf — Markdown-Handouts in schöne PDFs wandeln.

Setup (einmalig, im aktiven .venv):

    source .venv/bin/activate
    pip install -r extras/requirements.txt

Verwendung:

    python extras/md2pdf.py docs/tag1/01_variablen.md
    python extras/md2pdf.py docs/tag1/*.md
    python extras/md2pdf.py --all                   # alles aus docs/
    python extras/md2pdf.py --all --out pdfs/       # gesammelt in pdfs/

Ohne --out landet das PDF neben der Quelldatei.
"""

import argparse
import sys
from pathlib import Path

try:
    import markdown
    from weasyprint import CSS, HTML
except ImportError as fehler:
    print(f"Fehlende Abhängigkeit: {fehler.name}", file=sys.stderr)
    print("Installiere im aktiven venv:", file=sys.stderr)
    print("  pip install -r extras/requirements.txt", file=sys.stderr)
    sys.exit(1)


CSS_STYLES = """
@page {
    size: A4;
    margin: 2cm 2.2cm;
    @bottom-center {
        content: counter(page) " / " counter(pages);
        font-family: -apple-system, "Segoe UI", "Helvetica Neue", sans-serif;
        font-size: 9pt;
        color: #888;
    }
    @top-right {
        content: string(doc-title);
        font-family: -apple-system, "Segoe UI", "Helvetica Neue", sans-serif;
        font-size: 9pt;
        color: #888;
    }
}

html {
    font-family: -apple-system, "Segoe UI", "Helvetica Neue", sans-serif;
    font-size: 11pt;
    line-height: 1.5;
    color: #222;
}

h1, h2, h3, h4 {
    color: #1a4f8b;
    page-break-after: avoid;
}

h1 {
    font-size: 22pt;
    border-bottom: 2px solid #1a4f8b;
    padding-bottom: 0.2em;
    string-set: doc-title content();
    margin-top: 0;
}

h2 {
    font-size: 15pt;
    margin-top: 1.4em;
    color: #2a6cb0;
}

h3 { font-size: 12pt; }

p, li {
    text-align: left;
    hyphens: auto;
}

code {
    font-family: "JetBrains Mono", "SF Mono", Menlo, Consolas, monospace;
    font-size: 10pt;
    background: #f4f4f6;
    color: #b03030;
    padding: 1px 4px;
    border-radius: 3px;
}

pre {
    font-family: "JetBrains Mono", "SF Mono", Menlo, Consolas, monospace;
    font-size: 10pt;
    background: #f7f7fa;
    border-left: 3px solid #1a4f8b;
    padding: 0.7em 1em;
    border-radius: 3px;
    overflow-x: auto;
    page-break-inside: avoid;
    line-height: 1.4;
}

pre code {
    background: transparent;
    color: inherit;
    padding: 0;
}

table {
    border-collapse: collapse;
    margin: 1em 0;
    width: 100%;
    font-size: 10pt;
    page-break-inside: avoid;
}

th, td {
    border: 1px solid #ddd;
    padding: 6px 10px;
    text-align: left;
    vertical-align: top;
}

th {
    background: #f4f4f6;
    font-weight: 600;
}

blockquote {
    border-left: 3px solid #ccc;
    margin: 1em 0;
    padding: 0.3em 1em;
    color: #555;
}

a {
    color: #1a4f8b;
    text-decoration: none;
}

ul, ol { padding-left: 1.5em; }

/* Pygments-Klassen für Syntax-Highlighting */
.codehilite .k  { color: #cf222e; font-weight: 600; }   /* Keyword */
.codehilite .kn { color: #cf222e; font-weight: 600; }
.codehilite .nb { color: #6f42c1; }                      /* Built-in */
.codehilite .s, .codehilite .s1, .codehilite .s2 { color: #0a3069; }  /* String */
.codehilite .mi { color: #0550ae; }                      /* Number */
.codehilite .c, .codehilite .c1 { color: #6e7781; font-style: italic; }
.codehilite .o  { color: #0550ae; }                      /* Operator */
.codehilite .nf { color: #8250df; }                      /* Function */
"""


HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="utf-8">
    <title>{title}</title>
</head>
<body>
{body}
</body>
</html>
"""


def md_to_pdf(md_path: Path, output_path: Path) -> None:
    md_text = md_path.read_text(encoding="utf-8")

    html_body = markdown.markdown(
        md_text,
        extensions=[
            "tables",
            "fenced_code",
            "codehilite",
            "sane_lists",
            "smarty",
        ],
        extension_configs={
            "codehilite": {
                "css_class": "codehilite",
                "guess_lang": False,
            },
        },
    )

    full_html = HTML_TEMPLATE.format(title=md_path.stem, body=html_body)

    HTML(string=full_html, base_url=str(md_path.parent)).write_pdf(
        output_path,
        stylesheets=[CSS(string=CSS_STYLES)],
    )


def collect_files(args) -> list[Path]:
    if args.all:
        repo_root = Path(__file__).resolve().parent.parent
        return sorted((repo_root / "docs").rglob("*.md"))
    return [Path(p) for p in args.dateien]


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Wandelt Markdown-Handouts in schöne PDFs.",
    )
    parser.add_argument(
        "dateien",
        nargs="*",
        help="Eine oder mehrere Markdown-Dateien.",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Alle Markdown-Dateien aus docs/ konvertieren.",
    )
    parser.add_argument(
        "--out",
        type=Path,
        help="Ausgabe-Verzeichnis (Standard: neben der Quelldatei).",
    )
    args = parser.parse_args()

    files = collect_files(args)
    if not files:
        parser.error("keine Dateien angegeben — entweder Pfad(e) oder --all")

    out_dir = args.out
    if out_dir is not None:
        out_dir.mkdir(parents=True, exist_ok=True)

    fehler = 0
    for md in files:
        if not md.exists():
            print(f"  warn: {md} nicht gefunden, übersprungen", file=sys.stderr)
            fehler += 1
            continue

        ziel = (out_dir / md.with_suffix(".pdf").name) if out_dir else md.with_suffix(".pdf")
        try:
            md_to_pdf(md, ziel)
            print(f"  -> {ziel}")
        except Exception as e:
            print(f"  fehler bei {md}: {e}", file=sys.stderr)
            fehler += 1

    return 1 if fehler else 0


if __name__ == "__main__":
    sys.exit(main())
