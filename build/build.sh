#!/bin/bash
set -e

mkdir -p build_output/WEB-INF/classes
cp app/HelloWorld.java build_output/WEB-INF/classes/
javac build_output/WEB-INF/classes/HelloWorld.java

cp app/web.xml build_output/WEB-INF/

mkdir -p build_output
cp app/index.jsp build_output/

cd build_output
jar -cvf hello.war *
cd ..
