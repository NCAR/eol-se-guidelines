#! /bin/env python
"""
Extract documentation content by div from sundog pages.
"""
import sys
import subprocess as sp
import tempfile
from io import StringIO
from pathlib import Path
import logging

from bs4 import BeautifulSoup


logger = logging.getLogger(__name__)


def convert_path(path: Path or str):
    path = Path(path)
    title = path.name.replace(' - sundog.ucar.edu.html', '')
    logger.info("Page title: %s", title)
    with path.open() as html:
        soup = BeautifulSoup(html, 'html.parser')
        document = soup.find('div', id="page-content-container")
        if not document:
            # only front page has content in a PageSummary instead of a
            # page-content-container
            document = soup.find('div', {'class': "PageSummary"})
        if not document:
            logger.error("no document element found in %s", path)
            return
        outname = title.replace(' ', '-') + ".md"
        logger.info("Writing %s...", outname)
        outfile = open(outname, "w")
        infile = tempfile.TemporaryFile("w")
        infile.write(str(document))
        infile.seek(0)
        sp.call(["html2text", "-d"], stdin=infile, stdout=outfile)


def main(argv):
    """
    Given a list of html files on the command-line, parse the filename for a
    title, extract a document div element, and save it to another file in the
    current directory.
    """
    logging.basicConfig(level=logging.DEBUG)

    for path in argv:
        convert_path(path)


if __name__ == "__main__":
    main(sys.argv[1:])
