import unittest
import main
import test_data


class TestMain(unittest.TestCase):

    def test_parse_request(self):
        method, url = main.parse_request(test_data.request.decode('utf-8'))
        expected_method = "GET"
        expected_url = "/"
        print("ress", method, url)
        self.assertEqual(expected_method, method)
        self.assertEqual(expected_url, url)



if __name__ == "__main__":
    unittest.main()