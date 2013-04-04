#!/bin/sh

if [ ! -f selenium-server-standalone-2.31.0.jar ]
then
    wget http://selenium.googlecode.com/files/selenium-server-standalone-2.31.0.jar
fi

java -jar selenium-server-standalone-2.31.0.jar