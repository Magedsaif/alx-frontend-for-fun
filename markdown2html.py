#!/usr/bin/python3
"""  Markdown to HTML  """
import sys
import os
import re


def convert_markdown_to_html(input_file, output_file):
    """
    Transforms a Markdown file into HTML and saves the result into a file.

    Args:
        input_file (str): The path to the input Markdown file.
        output_file (str): The path to the output HTML file.

    Returns:
        None
    """
    # Validate that the Markdown file is present and it's a file
    if not (os.path.exists(input_file) and os.path.isfile(input_file)):
        print(f"{input_file} is not found", file=sys.stderr)
        sys.exit(1)

    # Open the Markdown file, read its content and convert it into HTML
    with open(input_file, encoding="utf-8") as f:
        html_lines = []
        for line in f:
            # Look for Markdown header syntax
            match = re.match(r"^(#+) (.*)$", line)
            if match:
                heading_level = len(match.group(1))
                heading_text = match.group(2)
                html_lines.append
                (f"<h{heading_level}>{heading_text}</h{heading_level}>")
            else:
                html_lines.append(line.rstrip())

    # Save the HTML result into a file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(html_lines))


if __name__ == "__main__":
    # Validate that the right number of arguments were given
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py <input_file> <output_file>",
              file=sys.stderr)
        sys.exit(1)

    # Get the input and output file names from the command-line arguments
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Convert the Markdown file to the HTML and write the output to a file
    convert_markdown_to_html(input_file, output_file)

    # Exit  with a successful status code
    sys.exit(0)
