#!/bin/bash

cd "${BASE_DIR}/" && python -m pylint --rcfile .pylintrc assembler
