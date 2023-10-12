#!/bin/bash
for i in {1..100}; do
	if [ $i -lt 10 ]; then
		echo $i
	else continue
	fi
done; unset $i
