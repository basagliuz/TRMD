#!/bin/bash

echo Hello!
date "+DATE: %Y-%m-%d%nTIME: %H:%M:%S"

touch output

echo 'Hello!' > output
date "+DATE: %Y-%m-%d%nTIME: %H:%M:%S" >> output