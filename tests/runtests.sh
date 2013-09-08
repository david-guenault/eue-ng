#!/bin/bash

export base=$(readlink -f $(dirname $0)/..)
export PYTHONPATH=$base

echo "base=$base"
echo "PYTHONPATH=$PYTHONPATH"

tests="test_mongo.py test_auth.py  test_user.py"
tests="test_mongo.py"

for test in $tests
do
    echo "Running test $test"
    python $test
done
