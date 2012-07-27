UNITTEST_IGNORES := -d C0103 -d R0904

all: static/style.css static/jquery.js static/script.js static/decisiverobot.svg static/decisiverobot.png static/speechtick.svg static/robots.txt
static/style.css: style.css static
	cp -f style.css static/style.css
static/jquery.js: jquery-1.7.2.min.js static
	cp -f jquery-1.7.2.min.js static/jquery.js
static/script.js: script.coffee static
	coffee --compile --output static script.coffee
static/robots.txt: robots.txt static
	cp -f robots.txt static/robots.txt
static/decisiverobot.svg: decisiverobot.svg static
	cp -f decisiverobot.svg static/decisiverobot.svg
static/decisiverobot.png: decisiverobot.png static
	cp -f decisiverobot.png static/decisiverobot.png
static/speechtick.svg: speechtick.svg static
	cp -f speechtick.svg static/speechtick.svg
static:
	mkdir static
pylint:
	pylint decisiverobot.py
	pylint $(UNITTEST_IGNORES) testdecisiverobot.py
	pylint web.py
	pylint twitterbot.py
clean:
	rm -rf *.pyc
	rm -rf static