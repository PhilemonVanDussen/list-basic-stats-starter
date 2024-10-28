# PJ VanDusse
# 10/28/2024
# List Basic Stats Starter
scores = [81, 62, 73, 61, 52, 67]
divide = len(scores)
average_score = sum(scores) / divide
print(f'My average quiz score from chemistry is {average_score}')

distances = [ 685, 1366, 1385, 490, 854] 
# nashiville/658 houston/1366 tampa/1385 cincinnati/490 new york city/ 854
short_trip = min(distances)
long_trip = max(distances)
sum = sum(distances)
average = sum / len(distances)
print(f'The shortest trip from Traverse city is Cincinnati which is {short_trip} miles away. ')
print(f'The longest trip from traverse city is Tampa which is {long_trip}')
print(f'Average distance of all the trips is {average:2f}')
