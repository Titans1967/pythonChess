import pprint, time
chessBoard1 = {
    'a1':'wrook1','b1':'wknight1','c1':'wbishop1','d1':'wking1','e1':'wqueen1','f1':'wbishop2','g1':'wknight2','h1':'wrook2',
    'a2':'wpawn1','b2':'wpawn2','c2':'wpawn3','d2':'wpawn4','e2':'wpawn5','f2':'wpawn6','g2':'wpawn7','h2':'wpawn8',
    'a3':' ','b3':' ','c3':' ','d3':' ','e3':' ','f3':' ','g3':' ','h3':' ',
    'a4':' ','b4':' ','c4':' ','d4':' ','e4':' ','f4':' ','g4':' ','h4':' ',
    'a5':' ','b5':' ','c5':' ','d5':' ','e5':' ','f5':' ','g5':' ','h5':' ',
    'a6':' ','b6':' ','c6':' ','d6':' ','e6':' ','f6':' ','g6':' ','h6':' ',
    'a7':'bpawn1','b7':'bpawn2','c7':'bpawn3','d7':'bpawn4','e7':'bpawn5','f7':'bpawn6','g7':'bpawn7','h7':'bpawn8',
    'a8':'brook1','b8':'bknight1','c8':'bbishop1','d8':'bking1','e8':'bqueen1','f8':'bbishop2','g8':'bknight2','h8':'brook2',
                }
#TODO: setup logfile system

piecesNeeded ={
'pawn': 8,
'rook': 2,
'knight': 2,
'bishop': 2,
'king': 1,
'queen': 1
}

whitePieces = {
    'pawn':0,
    'rook':0,
    'knight':0,
    'bishop':0,
    'king':0,
    'queen':0
}

blackPieces = {
    'pawn':0,
    'rook':0,
    'knight':0,
    'bishop':0,
    'king':0,
    'queen':0
}

#checks to makes sure each side has the correct number of pieces (16 per side)
whitePiecesCount = 0
blackPiecesCount = 0

for k,v in chessBoard1.items():
    if v.startswith('w'):
        whitePiecesCount += 1
    if v.startswith('b'):
        blackPiecesCount += 1
if blackPiecesCount == 16 and whitePiecesCount == 16:
    print(f'OK: number of pieces is {whitePiecesCount + blackPiecesCount}')
else:
    if whitePiecesCount != 16:
        print('ERROR: White has ' + str(whitePiecesCount) + ' pieces.')
    if blackPiecesCount != 16:
        print('ERROR: Black has ' + str(blackPiecesCount) + ' pieces.')
        
for k,v in chessBoard1.items():
    if v.startswith('w'):
        whitePieces[str(v)[1:]] += 1
    if v.startswith('b'):
        blackPieces[str(v)[1:]] += 1
        
 #game begins here. White moves first
 
turn = 'w'
 
while turn == 'w':
    pieceToMove = input('Which piece would you like to move?')
    space = input('Where would you like to move it?')
    chessBoard1[space] = pieceToMove
    turn = 'b'