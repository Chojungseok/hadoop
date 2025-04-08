#!/usr/bin/env python3
import sys 

for line in sys.stdin:
    line = line.strip()
    words = line.split()

    for word in words:
        print(f'{word}\t1')


# hadoop jar ~/hadoop-3.3.6/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar\
#  -input /input/text.txt \
#  -output /output/wordcount \
#  -mapper 'python3 /Users/chojungseok/damf2/hadoop/0.wordcount/mapper.py' \
#  -reducer 'python3 /Users/chojungseok/damf2/hadoop/0.wordcount/reducer.py'