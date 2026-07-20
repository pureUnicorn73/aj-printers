from __future__ import annotations

import argparse
import html
import re
from pathlib import Path

from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import KeepTogether, Paragraph, SimpleDocTemplate, Spacer


URL_RE = re.compile(r"https?://[^\s,)]+|/pliki/[^\s,)]+")


def register_fonts() -> None:
    regular = Path(r"C:\Windows\Fonts\arial.ttf")
    bold = Path(r"C:\Windows\Fonts\arialbd.ttf")
    if not regular.exists() or not bold.exists():
        raise FileNotFoundError("Nie znaleziono fontow Arial w C:\\Windows\\Fonts")
    pdfmetrics.registerFont(TTFont("AJArial", str(regular)))
    pdfmetrics.registerFont(TTFont("AJArial-Bold", str(bold)))


def linked_text(text: str) -> str:
    parts: list[str] = []
    position = 0
    for match in URL_RE.finditer(text):
        parts.append(html.escape(text[position : match.start()]))
        display = match.group(0)
        href = display if display.startswith("http") else f"https://ajprinters.pl{display}"
        parts.append(
            f'<a href="{html.escape(href, quote=True)}" color="#1d5f99">'
            f"<b>{html.escape(display)}</b></a>"
        )
        position = match.end()
    parts.append(html.escape(text[position:]))
    return "".join(parts)


def footer(canvas, doc) -> None:
    canvas.saveState()
    canvas.setFont("AJArial", 7.5)
    canvas.setFillColor(HexColor("#667085"))
    canvas.drawCentredString(
        A4[0] / 2,
        14 * mm,
        f"aj printers | sklep@ajprinters.pl | strona {doc.page}",
    )
    canvas.restoreState()


def build_pdf(source: Path, output: Path) -> None:
    register_fonts()
    lines = source.read_text(encoding="utf-8").splitlines()
    if not lines:
        raise ValueError("Plik zrodlowy jest pusty")

    title = lines[0].strip()
    meta = lines[1].strip() if len(lines) > 1 else ""
    body_lines = lines[2:]

    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        "AJTitle",
        parent=styles["Title"],
        fontName="AJArial-Bold",
        fontSize=20,
        leading=24,
        alignment=TA_CENTER,
        textColor=HexColor("#1f2937"),
        spaceAfter=10,
    )
    meta_style = ParagraphStyle(
        "AJMeta",
        parent=styles["BodyText"],
        fontName="AJArial",
        fontSize=9,
        leading=12,
        alignment=TA_CENTER,
        textColor=HexColor("#5f6b7a"),
        spaceAfter=18,
    )
    heading_style = ParagraphStyle(
        "AJHeading",
        parent=styles["Heading2"],
        fontName="AJArial-Bold",
        fontSize=10.8,
        leading=13,
        textColor=HexColor("#1f2937"),
        spaceBefore=8,
        spaceAfter=4,
        keepWithNext=True,
    )
    body_style = ParagraphStyle(
        "AJBody",
        parent=styles["BodyText"],
        fontName="AJArial",
        fontSize=8.8,
        leading=11.2,
        textColor=HexColor("#111827"),
        spaceAfter=4.5,
        splitLongWords=True,
    )
    list_style = ParagraphStyle(
        "AJList",
        parent=body_style,
        leftIndent=10 * mm,
        firstLineIndent=0,
        spaceAfter=3,
    )

    output.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(
        str(output),
        pagesize=A4,
        leftMargin=19 * mm,
        rightMargin=19 * mm,
        topMargin=14 * mm,
        bottomMargin=20 * mm,
        title=title,
        author="aj printers",
        subject="Dokument informacyjny aj printers",
    )

    story = [Paragraph(linked_text(title), title_style)]
    if meta:
        story.append(Paragraph(linked_text(meta), meta_style))

    previous_blank = False
    for raw_line in body_lines:
        line = raw_line.strip().replace("\u2011", "-")
        if not line:
            if not previous_blank:
                story.append(Spacer(1, 1.2 * mm))
            previous_blank = True
            continue
        previous_blank = False

        if line.startswith("§ "):
            story.append(Paragraph(linked_text(line), heading_style))
            continue

        is_list = bool(re.match(r"^(?:[a-z]\)|-\s)", line, re.IGNORECASE))
        story.append(
            KeepTogether([Paragraph(linked_text(line), list_style if is_list else body_style)])
        )

    doc.build(story, onFirstPage=footer, onLaterPages=footer)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    build_pdf(args.source, args.output)


if __name__ == "__main__":
    main()
