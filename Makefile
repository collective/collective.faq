# convenience makefile to boostrap & run buildout

version = 2.7

all: build

build: bin/buildout *.cfg
	bin/buildout

bin/buildout: bin/pip
	bin/pip install --upgrade pip
	bin/pip install -r requirements.txt
	@touch -c $@

bin/python bin/pip:
	virtualenv --clear --python=python$(version) .

clean:
	git clean -Xdf

test:
	bin/test

.PHONY: all clean
