#!/bin/bash

for i in {1000..1};
do
	tar -xvf *.tar;
	rm $i.tar;
done

