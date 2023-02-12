import re
title = "green: channel fan"
pattern = re.compile(r'\:')
if pattern.findall(title):
    title1 = title.replace(':','')
else:
    title1 = title