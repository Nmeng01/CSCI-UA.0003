"""
This script tests the summarize_text function from ma6918_summarized_test

Submitted by Nicholas Meng, NetID: ndm9914
The script takes a list of strings and a list of the correct outputs and compares them to ensure that
the summarize_text function is returning the correct outputs.
"""

import unittest
from ma6918_summarized_text import summarize_text

test_strings = ["This is a simple, but useful example! However, "
                "there are many cases not included here...",
                "This is pre-made lemonade. However, it tastes like "
                "it was 'homemade' a week ago.",
                """Testing the behavior of empty words ;: "; ""."""]

summaries = ['T2s is a s4e, b1t u4l e5e! H5r, t3e a1e m2y c3s n1t i6d '
             'h2e...',
             "T2s is p6e l6e. H5r, it t4s l2e it w1s 'h6e' a w2k a1o.",
             'T5g t1e b6r of e3y w3s ;: "; "".']

summariesX = ['T2s is a s4e, b1t u4l e5e! H5r, t3e a1e m2y c3s n1t i6d '
              'h2e..',
              "T2s is p6e l6e. H5r, it t4s l2e it w1s 'h6e' a w2k a1o.",
              'T5g t1e b6r of e3y w3s ;: "; "".']


class TestIncrement(unittest.TestCase):
    def test_summarizes_string1(self):
        self.assertEqual(summarize_text(test_strings[0]), summaries[0])

    def test_summarizes_string2(self):
        self.assertEqual(summarize_text(test_strings[1]), summaries[1])

    def test_summarizes_string3(self):
        self.assertEqual(summarize_text(test_strings[2]), summaries[2])


if __name__ == "__main__":
    unittest.main()
