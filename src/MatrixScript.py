# Problem Origin: Hacker Rank
# Difficulty: HARD
# Solution by: Jorge Vasquez-Collado 


# Neo has a complex matrix script. The matrix script is a X grid of strings. It consists of alphanumeric characters, spaces and symbols (!,@,#,$,%,&).

# [Capture.JPG]

# To decode the script, Neo needs to read each column and select only the alphanumeric characters and connect them. Neo reads the column from top to bottom and starts reading from the leftmost column.

# If there are symbols or spaces between two alphanumeric characters of the decoded script, then Neo replaces them with a single space '' for better readability.

# Neo feels that there is no need to use 'if' conditions for decoding.

# Alphanumeric characters consist of: [A-Z, a-z, and 0-9].

# Input Format

# The first line contains space-separated integers (rows) and (columns) respectively.
# The next lines contain the row elements of the matrix script.

# Constraints

# Note: A score will be awarded for using 'if' conditions in your code.

# Output Format

# Print the decoded matrix script.

# Sample Input 0

# 7 3
# Tsi
# h%x
# i #
# sM 
# $a 
# #t%
# ir!

# Sample Output 

# This is Matrix#  %!

# Explanation 

# The decoded script is:

# This$#is% Matrix#  %!

# Neo replaces the symbols or spaces between two alphanumeric characters with a single space   ' ' for better readability.

# So, the final decoded script is:

# This is Matrix#  %!


#!/bin/python3

import math
import os
import random
import re
import sys



nm = input().split()

n = int(nm[0])

m = int(nm[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

s = ""
for i in range(m):
    for j in range(n):
        mx = list(matrix[j])
        s = s + mx[i]
p = re.compile(r"([a-zA-Z])[^a-zA-Z]+([\ ]?[a-zA-z])")
s = re.sub(p, r"\1 \2", s)
print(s)
