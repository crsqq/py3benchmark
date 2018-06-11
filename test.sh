#!/bin/sh

cwd=`pwd`


cd /tmp
mkdir mybenchmark
cd mybenchmark

python3 -m venv testenv
. /tmp/mybenchmark/testenv/bin/activate

pip install numpy==1.14.4 networkx==2.1
python $cwd/benchmarks.py
