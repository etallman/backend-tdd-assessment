# import unittest

# def test_help(self):
#     """ Running the program without arguments should show usage. """

#     # Run the command `python ./echo.py -h` in a separate process, then
#     # collect it's output.
#     process = subprocess.Popen(
#         ["python", "./echo.py", "-h"],
#         stdout=subprocess.PIPE)
#     stdout, _ = process.communicate()
#     usage = open("./USAGE", "r").read()

#     self.assertEquals(stdout, usage)