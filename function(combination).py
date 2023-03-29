def solution(balls, share):
    answer = 0
    if share == 1:
        return balls
    return solution(balls-1, share-1)+solution(balls-1, share)
