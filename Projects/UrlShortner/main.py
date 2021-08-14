#protocol/domain/path

import pyshorteners as sh

link=input('Enter the link: ')

s=sh.Shortener()
print(s.tinyurl.short(link))