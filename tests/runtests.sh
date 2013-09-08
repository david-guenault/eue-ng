#!/bin/bash
export scripts="$(dirname $0)/.."
export base=$(readlink -f $scripts)
export tests=$(readlink -f $scripts/tests)
export PYTHONPATH=$base

echo "base=$base"
echo "tests=$tests"
echo "PYTHONPATH=$PYTHONPATH"

cd $tests

tests="test_mongo.py test_user.py"

for test in $tests
do
    echo "Running test $test"
    python $test
done
