#!/usr/bin/bash
i=0
while [ $i -le 32768 ]
do
        acfsutil fshare create /mnt/oracle/bdpshote.mkv /mnt/oracle/cpy/bdpshote_copy$i.mkv
        i=$(($i +1))
        echo $i
 done
