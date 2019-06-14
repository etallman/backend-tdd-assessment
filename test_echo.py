import echo
import unittest
import subprocess

class TestMethods(unittest.TestCase):
    
    def setUp(self):
        self.parser = echo.create_parser()
    
    def test_parser(self):
        args = ["--lower", "--upper", "--title", "HELLO"]
        ns = self.parser.parse_args(args)
        self.assertTrue(ns.lower)
        self.assertTrue(ns.upper)
        self.assertTrue(ns.title)
        self.assertTrue(ns.text)
        self.assertEquals(echo.main(args), "Hello")
        
    #Tests below call main and compares them to the string in the second argument.
    def test_lower(self):
        """ Running the program should show a lowercase string. """
        args = ["--lower", "HELLO"]
        self.assertEquals(echo.main(args), "hello")
        
    def test_upper(self):
        """ Running should show an uppercase string. Calls main and compares it to the string in the second argument. """
        args = ["--upper", "hello"]
        self.assertEquals(echo.main(args), "HELLO")

    def test_title(self):
        """ Running the program should show a titlecase string. """
        args = ["--title", "hello"]
        self.assertEquals(echo.main(args), "Hello")
        
    def test_help(self):
        """ Running the program without arguments should show usage. """
        # Run the command `python ./echo.py -h` in a separate process, then
        # collect it's output.
        process = subprocess.Popen(
            ["python", "./echo.py", "-h"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        usage = open("./USAGE", "r").read()
        self.assertEquals(stdout, usage)

if __name__ == '__main__':
    unittest.main()