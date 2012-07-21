UNITTEST_IGNORES := -d C0103 -d R0904

all: static/index.html static/style.css static/jquery.js static/script.js
static/index.html: index.html static
	cp -f index.html static/index.html
static/style.css: style.css static
	cp -f style.css static/style.css
static/jquery.js: jquery-1.7.2.min.js static
	cp -f jquery-1.7.2.min.js static/jquery.js
static/script.js: script.coffee static
	coffee --compile --output static script.coffee
static:
	mkdir static
pylint:
	pylint decisiverobot.py
	pylint $(UNITTEST_IGNORES) testdecisiverobot.py
	pylint web.py
clean:
	rm -rf *.pyc
	rm -rf static