#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re


def substitute(out):
    global directory
    for chapter in sorted(directory.get('Chapter',None)):
        out.write("\\chapter{" + re.sub("^\\d+-", "", chapter) + "}\n")
        for section in sorted(directory.get(os.path.join('Chapter', chapter),None)):
            out.write("\\input{" + re.sub("\\.tex$", "", os.path.join('Chapter', chapter, section)) + "}\n")
        out.write("\n")


directory = {}

# build directory structure
for path, dir_list, file_list in os.walk("Chapter"):
    for dir_name in dir_list:
        if not path in directory:
            directory[path] = set()
        directory[path].add(dir_name)
    for file_name in file_list:
        if not path in directory:
            directory[path] = set()
        directory[path].add(file_name)

base = open("base.tex", 'r')
output = open("main.tex", 'w')

try:
    line = base.readline()
    while line:
        if re.match("^\\s*%<SUBSTITUTION>%\\s*$", line):
            substitute(output)
        else:
            output.write(line)
        line = base.readline()

finally:
    base.close()
    output.close()
