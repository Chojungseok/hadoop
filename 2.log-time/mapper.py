import sys
import re 


time_pattern = re.compile(r':(\d{2}):(\d{2}):(\d{2})')


for line in sys.stdin:
    line = line.strip()

    match = time_pattern.search(line)
    
    if match:
        hour = match.group(1)
        print(f'{hour}\t1')


# hadoop jar ~/hadoop-3.3.6/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar\
#  -input /input/access.log \
#  -output /output/log-time \
#  -mapper 'python3 /Users/chojungseok/damf2/hadoop/2.log-time/mapper.py' \
#  -reducer 'python3 /Users/chojungseok/damf2/hadoop/2.log-time/reducer.py'