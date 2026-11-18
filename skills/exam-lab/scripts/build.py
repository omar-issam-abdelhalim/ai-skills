#!/usr/bin/env python3
"""Usage: python3 build.py template.html data.js out.html  — injects data.js between the DATA markers."""
import sys,re
tpl,data,out=sys.argv[1:4]
t=open(tpl,encoding='utf-8').read(); d=open(data,encoding='utf-8').read()
s=t.index('/*__DATA_START__*/')+len('/*__DATA_START__*/'); e=t.index('/*__DATA_END__*/')
open(out,'w',encoding='utf-8').write(t[:s]+'\n'+d+'\n'+t[e:])
print('built',out,len(t[:s]+d+t[e:]),'chars')
