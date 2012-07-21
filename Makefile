UNITTEST_IGNORES := -d C0103 -d R0904

all: static/index.html static/style.css
static/index.html: index.html static
	cp -f index.html static/index.html
static/style.css: style.css static
	cp -f style.css static/style.css
static:
	mkdir static
pylint:
	pylint decisiverobot.py
	pylint $(UNITTEST_IGNORES) testdecisiverobot.py
	pylint web.py
clean:
	rm -rf *.pyc
	rm -rf static