#!/bin/bash
#echo $1 $2
./a2q -a 1 -c -o $1 $2
echo "exit 0;" >> $1
