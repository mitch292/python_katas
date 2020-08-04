def crossword_puzzle(crossword, words):
    # Big assumption were going to make is that the words are always connected
    # iterate through the words 
    # iterate through the board
    # for the board does this word fit in the first gap we find
    # if yes, lets continue with each of the other words off of the other games 
    

if __name__ == "__main__":
    board = [
        ['+-++++++++'],
        ['+-++++++++'],
        ['+-++++++++'],
        ['+-----++++'],
        ['+-+++-++++'],
        ['+-+++-++++'],
        ['+++++-++++'],
        ['++------++'],
        ['+++++-++++'],
        ['+++++-++++'],
    ]

    words = ['LONDON','DELHI','ICELAND','ANKARA']

    print(crossword_puzzle(board, words))
