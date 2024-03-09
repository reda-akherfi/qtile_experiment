#!/bin/bash 

kill $(pgrep sxhkd)
sxhkd &
redshift -x
redshift -O 4000

