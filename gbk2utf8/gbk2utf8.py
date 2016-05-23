# coding=utf8

import codecs
import sys
sys.path.insert(0, "..")
from basic import dirtool as dirtool
import traceback
def doConvert(filename, suffix):
		hasError = False
		try:
			f = codecs.open(filename, 'r', 'gbk')
			s = f.readlines()
		except:
			traceback.print_exc() 
			hasError = True
#			print("return")
#			return
		finally:
			f.close()
		if hasError:
			return

		print(filename + suffix)
		#s.insert(0, u"--中文\n")
		try:
			out = codecs.open(filename + suffix, 'w', 'utf-8')
			out.writelines(s)
		except:
			print traceback.print_exc()
		finally:
			out.close()

def dofile():
	if len(sys.argv) != 3 and len(sys.argv) != 4:
		print('usage: python gbk2utf8.py folder filter [outsuffix]')
		return
	rootdir = sys.argv[1]
	filtername = sys.argv[2]
	outsuffix = ""
	if len(sys.argv) == 4:
		outsuffix = sys.argv[3]
	rootdir = dirtool.removeHeadTailSep(rootdir)
	files, dirs = dirtool.getAllFileInRootDir(rootdir, filtername)

	for filename in files:
		print(filename)
		doConvert(filename, outsuffix)

if __name__ == "__main__":
	dofile()