score = input('Please enter your score.')
score_float = float(score)

if (score_float >= 0.9 and score_float < 1.0) :
    grade = 'A'
elif (score_float >= 0.8 and score_float < 1.0) :
    grade = 'B'
elif (score_float >= 0.7 and score_float < 1.0) :
    grade = 'C'
elif (score_float >= 0.6 and score_float < 1.0) :
    grade = 'D'
elif (score_float < 0.6 and score_float > 0.0) :
    grade = 'F'
else:
    grade = 'Error'

print(grade)
