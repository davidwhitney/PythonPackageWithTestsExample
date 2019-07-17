import unittest
import pythonpackage.somemodule as somemodule

class SomeModuleTests(unittest.TestCase):
    
    def test_create_throws_if_not_alphabet_character(self):
        absolutely_not_a_letter = 2
        
        with self.assertRaises(Exception) as context:
            somemodule.create(absolutely_not_a_letter)

    def test_create_throws_if_lowercase(self):
        lowercase_letter = "a"
        
        with self.assertRaises(Exception) as context:
            somemodule.create(lowercase_letter)

    def test_create_first_and_last_line_contains_a(self):
        letter = "A"
        result = somemodule.create(letter)

        self.assertTrue('A' in result[0])
        self.assertTrue('A' in result[-1])

    def test_create_a_returns_only_a(self):
        result = somemodule.create('A')
        self.assertEqual(result[0], 'A')

    def test_create_not_a_a_is_first_and_last_line(self):
        result = somemodule.create('B')

        self.assertTrue('A' in result[0])
        self.assertTrue('A' in result[-1])

    def test_create_not_a_supplied_letter_is_on_midpoint(self):
        result = somemodule.create('B')

        self.assertTrue('B' in result[1])

    def test_create_not_a_midpoint_contains_two_instances_of_letter(self):
        result = somemodule.create('B')

        self.assertEqual(result[1].count('B'), 2)

    def test_create_not_a_whitespace_between_letters_is_correct(self):
        result = somemodule.create('B')

        self.assertEqual(result[1], "B B")

    def test_create_not_a_lines_correctly_padded(self):
        result = somemodule.create('B')

        self.assertEqual(result[0],  " A ")
        self.assertEqual(result[1],  "B B")
        self.assertEqual(result[-1], " A ")
    
if __name__ == '__main__':
    unittest.main()