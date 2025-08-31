import unittest
from ltp_app.app import parse_args, main


class TestArguments(unittest.TestCase):

    def test_ok(self):
        args = parse_args(['--name', 'M3oW'])
        app_obj = main(args)
        self.assertEqual(str(app_obj), 'Hello, this is the M3oW LTP app.')

    def test_too_long(self):
        with self.assertRaises(SystemExit) as cm:
            args = parse_args(['--name', 'abcdef'])
            main(args)
            self.assertEqual(str(cm.exception), "Name too long")

    def test_missing(self):
        args = parse_args([])
        app_obj = main(args)
        self.assertIsNotNone(app_obj)

if __name__ == "__main__":
    unittest.main()
