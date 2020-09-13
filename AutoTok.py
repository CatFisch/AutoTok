#!/usr/bin/env python3

# Copyright 2020 Catharina Fischer

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

# http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import glob
import os
import subprocess
import argparse

#define base parameters
def process_file(files):
    base_name = files.split('.')[0]
    output = base_name + "_neu.xlsx"
#run .pl script un .txt files
    tokenized = open(output, "w")
    subprocess.call(["perl", "utf8-tokenize.pl", files, output], stdout=tokenized)
# print final message
    print(os.path.basename(base_name), "was tokenized successfully")

#end function for optionality of input files
parser = argparse.ArgumentParser()
parser.add_argument("--file", nargs="*")
args = parser.parse_args()

#tokenize list of files in folder
if args.file:
    for f in args.file:
          process_file(f)
#tokenize all files in folder
else:
      txtfiles =  glob.glob(os.getcwd() + '/*.txt')

      for files in txtfiles:
          process_file(files)

print("\n selected files are tokenized altogeter \n ฅ^•ﻌ•^ฅ")
