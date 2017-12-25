
import sys
s='aaaaa'
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

print(s.translate(non_bmp_map))
