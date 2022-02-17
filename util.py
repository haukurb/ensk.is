#!/usr/bin/env python3
"""

    Ensk.is - English-Icelandic dictionary

    Copyright (c) 2022, Sveinbjorn Thordarson <sveinbjorn@sveinbjorn.org>
    All rights reserved.

    Redistribution and use in source and binary forms, with or without modification,
    are permitted provided that the following conditions are met:

    1. Redistributions of source code must retain the above copyright notice, this
    list of conditions and the following disclaimer.

    2. Redistributions in binary form must reproduce the above copyright notice, this
    list of conditions and the following disclaimer in the documentation and/or other
    materials provided with the distribution.

    3. Neither the name of the copyright holder nor the names of its contributors may
    be used to endorse or promote products derived from this software without specific
    prior written permission.

    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
    ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
    WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
    IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
    INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
    NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
    PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
    WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
    ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
    POSSIBILITY OF SUCH DAMAGE.

"""


from typing import List, Tuple

import os
import json


def read_pages() -> List[str]:
    """Read all text files in the data/dict directory,
    return as single list of all lines."""

    base_path = "data/dict/"
    files = sorted(os.listdir(base_path))
    result = []

    for file in files:
        fp = os.path.join(base_path, file)
        if os.path.isfile(fp) == False:
            continue
        if file.endswith(".txt") == False:
            continue

        with open(fp, "r") as file:
            file_contents = file.read()
        lines = file_contents.split("\n")

        for ln in lines:
            # Skip all empty lines and comments
            lns = ln.strip()
            if not lns or lns.startswith("#"):
                continue
            result.append(ln)

    return result


def read_all_words() -> List[str]:
    """Return a list of all dictionary words."""
    r = read_pages()
    words = []
    for line in r:
        w, d = parse_line(line)
        words.append(w)
    return words


def read_wordlist(fn: str) -> List[str]:
    """Read a file containing one word per line.
    Return all words as a list."""
    words = list()

    with open(fn, "r") as file:
        file_contents = file.read()
        lines = file_contents.split("\n")
        for line in lines:
            line = line.strip().replace("  ", " ")
            if not line:  # Skip empty lines
                continue
            if line.startswith("#"):  # Skip comments
                continue
            words.append(line)
    return words


CATEGORIES = read_wordlist("data/catwords.txt")


def parse_line(s: str) -> Tuple:
    """Parse a single line entry into its constitutent parts
    i.e. word and definition strings, and return as tuple."""
    comp = s.split()
    NO_VAL = 9999
    idx = NO_VAL
    for i, c in enumerate(comp):
        if c in CATEGORIES:
            idx = i
            break
    if idx == NO_VAL:
        raise Exception(f"No cat found!: {s}")

    wentries = list()
    for c in comp[:idx]:
        c = c.replace("\ufeff", "").strip().replace("  ", " ")
        if not c:
            continue
        if c.startswith("(") and c.endswith(")"):
            continue
        wentries.append(c)

    word = " ".join(wentries)
    definition = " ".join(comp[idx:])
    return (word, definition)


WORD_TO_PAGE = None


def page_for_word(w: str) -> int:
    """Look up the page at which a given word occurs in
    Geir T. Zoega's original dictionary."""
    global WORD_TO_PAGE
    if not WORD_TO_PAGE:
        with open("data/word2page.json", "r") as file:
            data = file.read()
            WORD_TO_PAGE = json.loads(data)
    return WORD_TO_PAGE.get(w, 0)
