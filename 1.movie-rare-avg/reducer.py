import sys


currunt_movie_id = None
currunt_sum = 0
currunt_count = 0

for line in sys.stdin:
    movie_id, rating = line.split()

    try:
        rating = float(rating)
    except:
        continue

    if currunt_movie_id == movie_id :
        currunt_count += 1
        currunt_sum += rating
    else:
        if currunt_movie_id is not None:
            currunt_avg = currunt_sum / currunt_count
            print(f'{currunt_movie_id}\t{currunt_avg}')

        currunt_movie_id = movie_id
        currunt_count = 1
        currunt_sum = rating

currunt_avg = currunt_sum / currunt_count
print(f'{currunt_sum}\t{currunt_avg}')



# hadoop jar ~/hadoop-3.3.6/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar\
#  -input /input/ratings.csv \
#  -output /output/movie-rate-avg \
#  -mapper 'python3 ~/damf2/hadoop/1.movie-rate-avg/mapper.py' \
#  -reducer 'python3 ~/damf2/hadoop/1.movie-rate-avg/reducer.py'