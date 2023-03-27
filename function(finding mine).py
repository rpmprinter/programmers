def solution(board):
    answer = 0
    answer_list = [[0 for i in range(len(board[0]))] for j in range(len(board))]
    if len(board) == 1:
        if board[0][0] == 1:
            return 0
        else:
            return 1
    for i in range(len(board)):
        for j in range(len(board[i])):
            if i == 0 and j == 0:
                answer_list[i][j] = board[i][j]+board[i][j+1]+board[i+1][j]+board[i+1][j+1]
            elif i == 0 and j == len(board[i])-1:
                answer_list[i][j] = board[i][j]+board[i][j-1]+board[i+1][j]+board[i+1][j-1]
            elif i == len(board)-1 and j == 0:
                answer_list[i][j] = board[i][j]+board[i-1][j]+board[i][j+1]+board[i-1][j+1]
            elif i == len(board)-1 and j == len(board[i])-1:
                answer_list[i][j] = board[i][j]+board[i-1][j]+board[i][j-1]+board[i-1][j-1]
            elif i == 0:
                answer_list[i][j] = board[i][j]+board[i+1][j]+board[i][j-1]+board[i][j+1]+board[i+1][j-1]+board[i+1][j+1]
            elif j == 0:
                answer_list[i][j] = board[i][j]+board[i][j+1]+board[i-1][j]+board[i+1][j]+board[i-1][j+1]+board[i+1][j+1]
            elif i == len(board)-1:
                answer_list[i][j] = board[i][j]+board[i-1][j]+board[i][j-1]+board[i][j+1]+board[i-1][j-1]+board[i-1][j+1]
            elif j == len(board[i])-1:
                answer_list[i][j] = board[i][j]+board[i][j-1]+board[i-1][j]+board[i+1][j]+board[i-1][j-1]+board[i+1][j-1]
            else:
                answer_list[i][j] = board[i-1][j-1]+board[i-1][j]+board[i-1][j+1]+board[i][j-1]+board[i][j]+board[i][j+1]+board[i+1][j-1]+board[i+1][j]+board[i+1][j+1]
    
    for i in range(len(answer_list)):
        for j in range(len(answer_list[i])):
            if answer_list[i][j] == 0:
                answer += 1
            else:
                continue
    return answer
