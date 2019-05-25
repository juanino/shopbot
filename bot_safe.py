#!/usr/bin/python3

from subprocess import Popen
import subprocess
import sys

filename = "shopBot.py"
while True:
    print("\nStarting " + filename)
    p = Popen("python3 " + filename, shell=True)
    p.wait()
    subprocess.run(["python3", "send_discord.py", "death detected and issuing a restart"])
