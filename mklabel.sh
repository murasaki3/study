for s in genuine spoof
do
    echo $s
    for x in `ls *${s}*feat`
    do
	echo $x
	base=`basename $x ".feat"`
	if [ $s = "genuine" ];  then
	    echo 1 > ${base}.lbl
	else
	    echo 0 > ${base}.lbl
	fi
    done
done



# for x in `ls *spoof*feat`
# do
#     echo $x
#     base=`basename $x ".feat"`
#     echo 0 > ${base}.lbl
# done
