CXX = g++
RM = rm -rf
PY = python

OBJS = print_result.o
PYFILE = predict.py
EX = ./main

all: main

run:
        $(PY) ${PYFILE}
        $(EX)

main: $(OBJS)
        $(CXX) -o $@ $^

%.o: %.c
        ${CXX} -o $a

clean:
        $(RM) main $(OBJS)
