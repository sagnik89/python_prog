# class Solution:
def findRelativeRanks(score):
    res = []
    res_final = []
    score_sort = score.sort()
    res.append("Gold Medal")
    res.append("Silver Medal")
    res.append("Bronze Medal")
        
    for i in score_sort:
        res.append(f'{i+1}th')

    for j in score_sort:
        for k in score:
            if j == k:
                res_final


    

scores = [1, 3, 4, 2, 7, 9]

findRelativeRanks(scores)
