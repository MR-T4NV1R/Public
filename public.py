import os, sys
try:
    __import__("public").Main()
except Exception as e:
    exit(str(e))