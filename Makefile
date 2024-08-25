.SUFFIXES: .md .html

markdown:
	@find . | grep -e "\.md$$" | grep -v reveal.js | grep -v node_modules | sed s/.md$$/.html/g | awk '{print "make -s "$$1}' | bash
	@/bin/cp -f readme.html index.html

.md.html:
	pathprefix=`echo $< | tr -d -c '/' | sed -r 's/\//..\//g'` && \
		pandoc --standalone -V "pagetitle:$$(head -1 $<)" -f markdown -c $$pathprefix"markdown.css" --columns=9999 -t html5 -o $@ $<
	@echo wrote $@

clean:
	/bin/rm -rf *~ */*~ */*/*~ */*/*/*~

syllabuspdf:
	pandoc -V geometry:margin=1in -f markdown -c markdown.css -t pdf -o syllabus.pdf syllabus.md
