#!/bin/bash
urllist=()
urllist+=(`youtube-dl -g -f mp4 -i -q $1`)
for ((i = 0; i < ${#urllist[@]}; i++)) {
    omxplayer -o local `echo ${urllist[i]}`
}