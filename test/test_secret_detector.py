import unittest
import sys

sys.path.append("./app")
from app.secret_detector import get_entropy_report, entropy_check, regex_match

class testGitConceal(unittest.TestCase):
  def test_get_entropy_report_1(self):
    """ Tests get_entropy_report() """
    secret_dict = get_entropy_report({0: ['here are some words'], 1: ['here are some more words']}, [[], []])
    self.assertEqual(secret_dict, [[], []])
  def test_get_entropy_report_2(self):
    """ Tests get_entropy_report() """
    secret_dict = get_entropy_report({0: ['asfgdhfjhdsdgkdfkjldgldfsdlkgjd43543853']}, [[]])
    self.assertEqual(secret_dict, [['Token: asfgdhfjhdsdgkdfkjldgldfsdlkgjd43543853 returned a shannon entropy of 3.49631407755924']])
  def test_entropy_check(self):
    """ Tests entropy_check() """
    self.assertEqual(entropy_check('asfgdhfjhdsdgkdfkjldgldfsdlkgjd43543853'), 3.49631407755924)
  def test_regex_match_1(self):
    """ Tests regex_match() """
    secret_dict = regex_match({0: ['password=help, username=help']})
    self.assertEqual(secret_dict, [['A regex was matched against: password=help, username=help']])
  def test_regex_match_2(self):
    """ Tests regex_match() """
    secret_dict = regex_match({0: ['will not trigger']})
    self.assertEqual(secret_dict, [[]])