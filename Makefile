UNITTEST_IGNORES := -d C0103 -d R0904

all: static/style.css static/jquery.js static/script.js static/decisiverobot.svg static/decisiverobot.png
static/style.css: style.css static
	cp -f style.css static/style.css
static/jquery.js: jquery-1.7.2.min.js static
	cp -f jquery-1.7.2.min.js static/jquery.js
static/script.js: script.coffee static
	coffee --compile --output static script.coffee
static/decisiverobot.svg: static
	cp -f decisiverobot.svg static/decisiverobot.svg
static/decisiverobot.png: static
	cp -f decisiverobot.png static/decisiverobot.png
static:
	mkdir static
pylint:
	pylint decisiverobot.py
	pylint $(UNITTEST_IGNORES) testdecisiverobot.py
	pylint web.py
clean:
	rm -rf *.pyc
	rm -rf static