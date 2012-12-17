#!/bin/sh

# Helper script to build all jni codes.

ROOT=$(dirname $0)/../..

# Run gyp to generate Android.mks.
${ROOT}/build/gyp_android

# Here we go.
ndk-build -j4
