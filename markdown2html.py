#!/usr/bin/python3
"""Module to convert markdown to html"""
import sys
import os
import re


def markdown_to_html(markdown):
    """Function to convert markdown to html"""
    markdown = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', markdown)
    markdown = re.sub(r'__(.+?)__', r'<em>\1</em>', markdown)
    markdown = re.sub(r'\*(.+?)\*', r'<em>\1</em>', markdown)
    markdown = re.sub(r'_([^_]+)_', r'<em>\1</em>', markdown)
    markdown = re.sub(r'^(.+)\n-+$', r'<h2>\1</h2>', markdown)
    markdown = re.sub(r'^(.+)\n=+$', r'<h1>\1</h1>', markdown)
    for i in range(6, 0, -1):
        markdown = re.sub(r'^#{%d}(.+)$' % i, r'<h%d>\1</h%d>' % (i, i),
                          markdown)
    markdown = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2">\1</a>',
                      markdown)
    markdown = re.sub(r'\!\[(.+?)\]\((.+?)\)', r'<img alt="\1" src="\2">',
                      markdown)
    return markdown


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        sys.exit(1)
    if not os.path.exists(sys.argv[1]):
        print("Missing {}".format(sys.argv[1]), file=sys.stderr)
        sys.exit(1)
    with open(sys.argv[1], 'r') as md:
        markdown = md.read()
    html = markdown_to_html(markdown)
    with open(sys.argv[2], 'w') as html_file:
        html_file.write(html)
    sys.exit(0)
