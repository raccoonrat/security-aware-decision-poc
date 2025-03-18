import re
from pathlib import Path

class LawParser:
    ARTICLE_PATTERN = re.compile(r"第(\d+)条 (.*)")

    def __init__(self, law_dir):
        self.laws = {}
        for p in Path(law_dir).glob("*.txt"):
            with p.open() as f:
                self.laws[p.stem] = self._parse(f.read())

    def _parse(self, text):
        articles = {}
        for line in text.split("\n"):
            if match := self.ARTICLE_PATTERN.match(line):
                articles[int(match.group(1))] = match.group(2)
        return articles
