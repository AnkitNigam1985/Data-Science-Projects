score_list=[]
print("How many scores you want to add?")
nm_score=int(input())

for i in range(nm_score):
    score=int(input())
    score_list.append(score)

print("Maximum score is :", max(score_list))
