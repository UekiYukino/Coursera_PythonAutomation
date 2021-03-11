#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(attachment, title, paragraph):
    styles= getSampleStyleSheet()
    report= SimpleDocTemplate(attachment) 
    report_title= Paragraph(title, styles["h1"])
    report_content= Paragraph(paragraph, styles["BodyText"])
    empty_space= Spacer(1,10)
    report.build([report_title,empty_space,report_content])


