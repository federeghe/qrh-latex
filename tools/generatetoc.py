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