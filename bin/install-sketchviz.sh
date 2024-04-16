#!/usr/bin/env sh
pushd ./deps/sketchviz
npm pack
npm i -g sketchviz-0.0.1.tgz
popd
