#!/usr/bin/env python3
# coding: utf-8

import io
import torch
import unittest
from unittest.mock import patch
from PIL import Image
import requests
from predict import main, get_image, return_prediction


class TestGetImage(unittest.TestCase):
    def test_valid_path(self):
        path = "https://images.unsplash.com/photo-1608848461950-0fe51dfc41cb?auto=format&fit=crop&q=80&w=1000&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxleHBsb3JlLWZlZWR8Mnx8fGVufDB8fHx8fA%3D%3D"
        image = get_image(path)
        self.assertIsInstance(image, Image.Image)

    def test_invalid_file(self):
        path = "images/non_existant.jpg"
        image = get_image(path)
        self.assertIsNone(image)

    def test_invalid_url(self):
        path = "https://www.google.com/search?q=cat+photo&client=ubuntu-chr&hs=djk&sca_esv=577146942&tbm=isch&source=lnms&sa=X&ved=2ahUKEwiw2JeampaCAxUqKRAIHeBRAe0Q_AUoAXoECAIQAw&biw=1235&bih=611&dpr=1.5#imgrc=0LtKV6SSeh9FYM"
        image = get_image(path)
        self.assertIsNone(image)

    def test_unidentified_url(self):
        path = "https://example.com/blog/</div><div class="
        image = get_image(path)
        self.assertIsNone(image)

    

class TestReturnPrediction(unittest.TestCase):
    def test_cat_return_prediction(self):
        logits = torch.tensor([[10, -10]])
        result = return_prediction(logits)
        self.assertEqual(result, "a cat")

    def test_dog_return_prediction(self):
        logits = torch.tensor([[-10, 10]])
        result = return_prediction(logits)
        self.assertEqual(result, "a dog")

    def test_unidentified_return_prediction(self):
        logits = torch.tensor([[-10, -10]])
        result = return_prediction(logits)
        self.assertEqual(result, "an unidentified thing")

    def test_custom_threshold_return_prediction(self):
        logits = torch.tensor([[0.6, 0.4]])
        result = return_prediction(logits, thr=0.5)
        self.assertEqual(result, "a cat")

    

def mock_input(mock_values):
    return lambda prompt: mock_values.pop(0)

class MainTestCase(unittest.TestCase):
    @patch('builtins.input', side_effect=mock_input(['cat.jpg']))
    def test_main(self, mock_input):
        captured_output = io.StringIO()
        expected_output = "This is a cat!"

        with patch('sys.stdout', new=captured_output):
            main('cat.jpg')

            # Assert that the printed output matches with the expected output
            self.assertEqual(captured_output.getvalue().strip(), expected_output)


if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

