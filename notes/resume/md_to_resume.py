"""Render a resume markdown file (as exported from the doc) to an
ATS-friendly PDF: single column, plain text, no tables or images.
Usage: RES_BASE=10.0 python3 md_to_resume.py input.md output.pdf"""
import os
import re
import sys
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable

ACCENT = colors.HexColor("#1F3A5F")
FONT, BOLD = "Helvetica", "Helvetica-Bold"
BASE = float(os.environ.get('RES_BASE', '9.4'))
LEAD = BASE * 1.22
name_s = ParagraphStyle("name", fontName=BOLD, fontSize=18, leading=21, alignment=TA_CENTER, textColor=ACCENT)
head_s = ParagraphStyle("hl", fontName=FONT, fontSize=10.3, leading=12.5, alignment=TA_CENTER)
contact_s = ParagraphStyle("ct", fontName=FONT, fontSize=8.8, leading=11, alignment=TA_CENTER)
sec_s = ParagraphStyle("sec", fontName=BOLD, fontSize=10.3, leading=12, textColor=ACCENT, spaceBefore=5, keepWithNext=1)
body_s = ParagraphStyle("body", fontName=FONT, fontSize=BASE, leading=LEAD)
role_s = ParagraphStyle("role", parent=body_s, spaceBefore=2)
bullet_s = ParagraphStyle("bl", parent=body_s, leftIndent=10, firstLineIndent=-7, spaceAfter=0.5)
PLAIN_LIST_SECTIONS = {"SKILLS", "EDUCATION"}


def inline(t):
    t = t.replace("\\~", "~").replace("\\", "")
    t = t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"\[(.+?)\]\((.+?)\)", r'<link href="\2">\1</link>', t)
    t = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<i>\1</i>", t)
    return t


def build(md_path, out_path):
    lines = [l.rstrip() for l in open(md_path, encoding="utf-8")]
    story, section, header_lines = [], None, 0
    for line in lines:
        if not line.strip():
            continue
        if line.startswith("# "):
            story.append(Paragraph(inline(line[2:]), name_s))
            continue
        if line.startswith("## "):
            section = line[3:].strip().upper()
            # keep each section heading and its rule with the first line of the section
            hr = HRFlowable(width="100%", thickness=0.6, color=ACCENT, spaceBefore=1, spaceAfter=3)
            hr.keepWithNext = 1
            story += [Paragraph(inline(section), sec_s), hr]
            continue
        if section is None:  # headline, then contact line
            text = inline(line).replace("<b>", "").replace("</b>", "")
            story.append(Paragraph(text, head_s if header_lines == 0 else contact_s))
            header_lines += 1
            continue
        if line.startswith("- "):
            item = inline(line[2:])
            if section in PLAIN_LIST_SECTIONS:
                story.append(Paragraph(item, body_s))
            else:
                story.append(Paragraph("• " + item, bullet_s))
            continue
        style = role_s if line.startswith("**") else body_s
        story.append(Paragraph(inline(line), style))
    SimpleDocTemplate(out_path, pagesize=letter, leftMargin=0.6 * inch, rightMargin=0.6 * inch,
                      topMargin=0.45 * inch, bottomMargin=0.45 * inch,
                      title="Alakh Aggarwal Resume", author="Alakh Aggarwal").build(story)


if __name__ == "__main__":
    build(sys.argv[1], sys.argv[2])
