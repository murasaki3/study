for x in `ls train*.txt`
do
    base=`basename $x ".txt"`
    echo $base
    cp $x ${base}_spoof.feat
done
