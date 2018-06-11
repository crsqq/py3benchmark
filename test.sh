#!/bin/sh

CWD=`pwd`

TMPPTH=/tmp
TMPDIR=mybenchmark
TMPPTHFULL=$TMPPTH/$TMPDIR

if [ ! -d $TMPPTHFULL ]; then
    cd $TMPPTH
    mkdir $TMPDIR
    cd $TMPDIR

    python3 -m venv testenv
    . $TMPPTHFULL/testenv/bin/activate

    pip install numpy==1.14.4 networkx==2.1
else
    . $TMPPTHFULL/testenv/bin/activate
fi
python $CWD/benchmarks.py
