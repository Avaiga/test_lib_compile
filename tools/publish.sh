#!/bin/bash

python3.10 -m pip install build

cp -fR testlib/. tmp

compile() {
    PYTHON_PATH=$1
    ZIP_FILE=$2

    # create new working dir
    cp -R tmp testlib
    # generate pyi
    $PYTHON_PATH -O -m compileall testlib -b -f
    # Generate pyi
    $PYTHON_PATH -m pip install mypy
    stubgen testlib -o ./
    # Remove unnecessary files
    find testlib -name '*.py' -delete
    find testlib -type d -name  "__pycache__" -exec rm -r {} +
    # zip folder
    zip -r $ZIP_FILE testlib
    # remove current working dir
    rm -rf testlib
}

compile python3.8 ./testlib-3.8.zip
compile python3.9 ./testlib-3.9.zip
compile python3.10 ./testlib-3.10.zip
compile python3.11 ./testlib-3.11.zip
compile python3.12 ./testlib-3.12.zip

rm -rf tmp

find src -name '*.py' -delete

python3.10 -m build
