main:
	source-highlight *.py
	"ls" *.py | awk '{print "mv "$$1".html "$$1".raw.html"}' | bash
	source-highlight -d *.py
