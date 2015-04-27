###############################################################################
# QRH - Quick Reference Handbook in LaTeX
# Repository: https://github.com/federeghe/qrh-latex
# Author: Federico Reghenzani <federico §DOT§ dev §AT§ reghe §DOT§ net>
###############################################################################
#    This file is part of qrh-latex.
#
#    qrh-latex is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    qrh-latex is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with qrh-latex.  If not, see <http://www.gnu.org/licenses/>.
###############################################################################
import sys
import re


def int_to_roman(num):
   ints = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
   nums = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
   result = ""
   for i in range(len(ints)):
      count = int(num / ints[i])
      result += nums[i] * count
      num -= ints[i] * count
   return result


def main():
    if len(sys.argv) != 2:
        print("Usage: qrh-toc filename.tex")
        print("Wrong arguments number.")
        sys.exit(1)

    try:
        f_source = open(sys.argv[1], 'r')
    except FileNotFoundError:
        print("File not found.")
        return

    re_splitcommands = re.compile("\\\\")
    commands_list = re_splitcommands.split(f_source.read())

    f_source.close()

    counter_part = counter_body = 0

    for c in commands_list:
        if "QRHpart" in c:
            counter_part += 1
            counter_body = 0
            print("")
            print("\contentsline {part}{", end="")
            print(c[c.index("{") + 1 : c.index("}")], end="")
            print("}{"+int_to_roman(counter_part)+"}", end="")
            
            print("")
        if "QRHbody" in c:

            print("\contentsline {section}{", end="")
            print(c[c.index("{") + 1 : c.index("}")], end="")
            print("}{"+str(counter_part)+"."+str(counter_body)+"}", end="")
            
            print("")
            
        if "newpage" in c:
            counter_body += 1

main()