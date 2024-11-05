SLIDE_SETS: dp.html announcements.html reductions.html graphdev.html
.SUFFIXES: .qmd .html
.PHONY: slides all clean

slides: $(SLIDE_SETS)
	@echo conversion done

.qmd.html:
	quarto render $< --to revealjs

clean:
	/bin/rm -rf *~ */*~ */*/*~ */*/*/*~

all:
	touch *.qmd
	make $(SLIDE_SETS)
