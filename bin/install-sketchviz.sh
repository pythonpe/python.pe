#!/usr/bin/env sh
pushd ./deps/sketchviz
npm pack
npm i -g sketchviz*.tgz
rm sketchviz*.tgz
popd
