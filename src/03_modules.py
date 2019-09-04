"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import os
import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
for i in range(len(sys.argv)):
    print("this is the name of the argument", sys.argv[i])
# Print out the OS platform you're using:
# YOUR CODE HERE
print("this is the platform", sys.platform)
# Print out the version of Python you're using:
# YOUR CODE HERE
print(sys.version)


# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
pid = os.getpid()
print(pid)

# Print the current working directory (cwd):
# YOUR CODE HERE
cwd = os.getcwd()
print(cwd)
# Print out your machine's login name
# YOUR CODE HERE
machine_login = os.getlogin()
print(machine_login)
