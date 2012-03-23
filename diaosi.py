import sdict
import os
import string

alphabets='abcdefghijklmnopqrstuvwxyz'

def current_file_directory():
			import os, sys, inspect
			path = os.path.realpath(sys.path[0])        # interpreter starter's path
			if os.path.isfile(path):                    # starter is excutable file
				path = os.path.dirname(path)
				return os.path.abspath(path)            # return excutable file's directory
			else:                                       # starter is python script
				caller_file = inspect.stack()[1][1]     # function caller's filename
				return os.path.abspath(os.path.dirname(caller_file))# return function caller's file's directory

def edits1(W):
	N = len(W)
	splits = [(W[:i],W[i:]) for i in xrange(N)]
	deletes = [ x+y[1:] for x,y in splits if y]
	trans = [a + b[1] + b[0] +b[2:] for a,b in splits if len(b)>1]
	replaces = [a + c + b[1:] for a,b in splits for c in alphabets if b]
	inserts =  [a + c + b for a,b in splits for c in alphabets]
	return set(deletes+trans+replaces+inserts)
	
index = sdict.Dict()
_localDir=current_file_directory()

_curpath=os.path.normpath(os.path.join(os.getcwd(),_localDir))
		
dic_name = os.path.join(_curpath,"endict.txt")

for line in open(dic_name,"rb"):
	#print line
	tup = line.rstrip().split('\t')
	en_word = tup[0]
	chn_word = tup[1:]
	low_word= en_word.lower()
	chn_word = ' '.join(chn_word)
	index[en_word] = chn_word
	if en_word != low_word:
		index[low_word] = chn_word

while True:	
	try:
		word = raw_input(">> ")
	except:
		break
	rel_words = index.prefix(word)

	for w in rel_words:
		print w,index[w]

	if len(rel_words)==0:
		cor_words = edits1(word)
		for w in cor_words:
			if w in index:
				print '? ',w
