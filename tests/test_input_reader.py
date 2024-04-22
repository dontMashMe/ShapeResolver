from unittest import TestCase, mock
from input_reader import InputReader


class TestInputReader(TestCase):
    def setUp(self):
        self.sample_file_name = "sample.txt"
        self.sample_content = "Line 1\nLine 2\nLine 3"
        self.input_reader = InputReader(self.sample_file_name)

    def test_load_file_with_existing_file(self):
        # Test loading an existing file
        with mock.patch("builtins.open", mock.mock_open(read_data=self.sample_content)):
            expected_output = self.sample_content
            actual_output = self.input_reader.load_file()
            self.assertEqual(actual_output, expected_output)

    def test_load_file_with_empty_file(self):
        # Test loading an empty file
        with mock.patch("builtins.open", mock.mock_open(read_data="")):
            expected_output = ""
            actual_output = self.input_reader.load_file()
            self.assertEqual(actual_output, expected_output)
