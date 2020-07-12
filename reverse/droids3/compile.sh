#!/bin/bash -e
if ! [ "$1" ]; then
	    echo "usage: $0 <original.apk>"
	        exit -1
fi

fn=${1%.apk}

rm -f $fn.unaligned.apk $fn.smali.apk
rm -rf smali/build

apktool b -f smali/ -o $fn.unaligned.apk
jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 -keystore ./my-release-key.keystore  -storepass password  $fn.unaligned.apk alias_name
zipalign -v 4 $fn.unaligned.apk $fn.smali.apk
rm -rf smali/build
