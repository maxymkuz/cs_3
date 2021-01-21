C ?= gcc
LDFLAGS ?= -O3

BIN_DIR = bin
OBJS =  main.o unsigned_sum.o
SOURCES = src/main.c src/unsigned_sum.c
HEADERS = function_file_name.h
RESULT_OUT = main

all: make_dirs $(BIN_DIR)/$(RESULT_OUT)

make_dirs:
	mkdir -p $(BIN_DIR)
	#mkdir -p $(OBJ_DIR)

$(BIN_DIR)/$(RESULT_OUT): $(SOURCES)
	$(C) -o $@ $^ -I/src

.PHONY: clean
clean:
	rm -rf $(BIN_DIR)
