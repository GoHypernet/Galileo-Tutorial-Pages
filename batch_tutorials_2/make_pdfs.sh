#!/bin/bash
for OUTPUT in $(find -name "*.md")
do
    echo "CONVERTING $OUTPUT TO MARKDOWN"
    NEWNAME=$(basename $OUTPUT .md)
    pandoc -f markdown -t html5 $OUTPUT -o $NEWNAME.pdf
done
