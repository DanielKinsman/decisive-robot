all: static/index.html static/style.css
static/index.html: index.py
	pyjsbuild --output=static index.py
static/style.css: style.css
	cp -f style.css static/style.css
clean:
	rm -rf *.pyc
	rm -rf static