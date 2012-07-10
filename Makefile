#can possibly get rid of some of these disables after installing pyjamas properly
PYJS_IGNORES := -d C0103 -d F0401 -d E1101 -d W0613 -d R0903 -d R0201
UNITTEST_IGNORES := -d C0103 -d R0904

all: static/index.html static/style.css
static/index.html: index.py
	pyjsbuild --output=static index.py
static/style.css: style.css
	cp -f style.css static/style.css
pylint:
	pylint decisiverobot.py
	pylint $(UNITTEST_IGNORES) testdecisiverobot.py
	pylint web.py
	pylint $(PYJS_IGNORES) index.py
clean:
	rm -rf *.pyc
	rm -rf static