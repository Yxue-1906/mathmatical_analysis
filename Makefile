all: main.tex
	/usr/bin/xelatex main.tex -synctex=1 -interaction=nonstopmode -file-line-error
	/usr/bin/xelatex main.tex -synctex=1 -interaction=nonstopmode -file-line-error

main.tex: base.tex build.py
	/usr/bin/python build.py base.tex

clean:
	find . \( -name '*.aux' -o -name '*.log' -o -name '*.out' -o -name '*.toc' -o -name '*.synctex.gz' \) -print0 | xargs -0 -I file rm 'file'

.PHONY: all clean
