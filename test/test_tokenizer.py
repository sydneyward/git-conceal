import unittest
import sys

sys.path.append("./app")
from app.tokenizer import tokenize

class testGitConceal(unittest.TestCase):
  def test_tokenize(self):
    """ Tests tokenize() """
    dct = tokenize("test/test.txt")
    self.assertEqual(dct, {0: ['here are some words'], 1: ['here are some more words']})
    