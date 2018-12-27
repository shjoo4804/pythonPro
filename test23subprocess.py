#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import subprocess
print("subprocess")

### 참고 documents
# https://docs.python.org/2.7/library/subprocess.html

#subprocess.call("ls -al | more", shell=True)
#subprocess.call("sh ./test23.sh", shell=True)

lst = [11,22,33]
subprocess.call("echo {}".format(lst[0]), shell=True)


lst = ["test23.sh", "test24.sh"]
ext23 = os.path.exists("/home/pi/pythonPro/test23.sh")
ext24 = os.path.exists("/home/pi/pythonPro/test24.sh")

if (ext23 == "True"):
	value = "cat {}".format(lst[0])
	subprocess.call(value, shell=True)
