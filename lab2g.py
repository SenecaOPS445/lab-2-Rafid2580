#!/usr/bin/env python3
# Author: Rafid Al Fahim
# Author ID: rfahim1
# Date Created: 2024/05/24

import sys

if len(sys.argv) == 1:
    timer = 3
else:
    timer = int(sys.argv[1])

while timer > 0:
    print(timer)
    timer = timer - 1
print('blast off!')
