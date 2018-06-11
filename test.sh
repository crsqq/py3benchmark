#!/bin/sh

cd /tmp
mkdir mybenchmark
cd mybenchmark

python3 -m venv testenv
. /tmp/mybenchmark/testenv/bin/activate

echo `python --version`

pip install numpy networkx

python /tmp/foo/benchmarks.py

