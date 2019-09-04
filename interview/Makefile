# Makefile for interview

PROJECT ?= interview

USE_PYTHON3 := true
PYVENV_MAKE := ../tools/make_venv.sh
PYVENV_NAME ?= .venv


.PHONY: clean cover dev-setup show test
clean cover dev-setup show test:
	@echo
	cd .. && make $@



############################################################
# interview targets
############################################################
.PHONY: run run-main
run run-main:
	@echo
ifneq ("$(VIRTUAL_ENV)", "")
	PYTHONPATH=../.. python main.py
else
	USE_PYTHON3=$(USE_PYTHON3) VENV_NAME=$(PYVENV_NAME) $(PYVENV_MAKE) "$@"
endif
	@echo
	@echo "- DONE: $@"
