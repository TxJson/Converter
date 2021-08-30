run:
	npm run dev

clean:
	rm -rf node_modules

empty-log:
	rm -rf log

clean-all:
	rm -rf node_modules log

install-dev:
	rm -rf node_modules
	npm i
	pip install Pillow
	pip install colored

install-converter:
	pip install Pillow
	pip install colored