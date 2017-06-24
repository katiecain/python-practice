import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py.'"""
    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        self.assertEqual(get_formatted_name('janis', 'joplin'), 'Janis Joplin')