run: main.py
	python main.py
	display image.png

clean:
	rm *.pyc
	rm *~

all: run
