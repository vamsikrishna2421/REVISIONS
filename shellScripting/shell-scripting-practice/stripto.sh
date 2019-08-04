#!/bin/sh
if [ ! $1 ]; then
    echo "need first argument" >&2
    exit 1
fi
while [ `read -r` ] 
do
    if [ $REPLY =~ $1 ];then
        echo "$REPLY"
        break
    fi
done

while `read -r` ; do
    echo $REPLY
done
exit 0

