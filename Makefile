CXX = g++
RM = rm -rf
PY = python3

OBJS = print_result.o
SCR = scripts
SOURCE = source
PYFILE = $(SCR)/predict.py
EX = ./main

all: main

run:
	$(PY) ${PYFILE} ${img}
	$(EX)

main: $(OBJS)
	$(CXX) $^ -o $@ 

%.o: $(SOURCE)/%.cpp
	${CXX} -c $^ -o $@

clean:
	$(RM) main $(OBJS)
