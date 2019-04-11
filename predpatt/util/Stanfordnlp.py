"""
Wrapper around the stanfordnlp parser.
"""

import sys, os

import stanfordnlp
from predpatt.UDParse import UDParse, DepTriple

DEFAULT_LANGUAGE = 'ja'

class Parser():
    """
    Interface for parsing to universal dependency syntax (UD). 
    Uses the stanfordnlp parser for constituency parsing.
    """

    def __init__(self, lang=DEFAULT_LANGUAGE):
        self.ud_parser = stanfordnlp.Pipeline(lang=lang)

    def __call__(self, *args, **kwargs):
        x = self.fresh(*args, **kwargs)
        return x
    
    def release_ud_parser(self):
        self.ud_parser = None
    
    def parse(self, sentence):
        sentence = self.ud_parser(sentence).sentences[0]
        deps = sentence.words
        tokens = [e.text for e in deps]
        tags = [e.upos for e in deps]

        # stanfordnlp indexing starts at one, but we want
        # indexing to start at zero. Hence the -1 below.
        triples = list(map(lambda e:DepTriple(rel=e.dependency_relation, gov=e.governor-1, dep=int(e.index)-1), deps))

        return UDParse(tokens=tokens, tags=tags, triples=triples)

    def fresh(self, s):
        s = str(s.strip())
        assert '\n' not in s, "No newline characters allowed %r" % s
        return self.parse(s)

    @staticmethod
    def get_instance(CACHE=True, lang=DEFAULT_LANGUAGE):
        """
        Do whatever it takes to get parser instance
        """
        # TODO: , including downloading the external dependencies.
        return Parser(lang=lang)

if __name__ == "__main__":
    parser = Parser(lang='ja')
    parse_string = "今日はいい天気ですね"
    sent = parser(parse_string)
    print(sent.pprint())