import string
import random

def set_players():
    
    players = []
    pieces = ['x', 'o']
    random.shuffle(pieces)
    
    #set for comparison checks and ask atlas about .casefold()
    while len(players) < 2:
        new_player = input(f"Player {len(players)+1}, please enter your name: ").strip()
        if new_player and new_player != ' ' and new_player not in players:
            players.append(new_player)
        else:
            print("Duplicate or invalid name!")
            
    return {player: piece for player, piece in zip(players, pieces)}



def set_grid(n):
    return [[' ' for _ in range(n)] for _ in range(n)]

def get_pos_map(n):
    return {f'{string.ascii_lowercase[col]}{row+1}': (row, col)
            for row in range(n)
            for col in range(n)
            }

def player_move(grid, token, player, pos):
    n = len(grid)
    
    print(f"{player}'s turn ({token.upper()}):")
    
    while True:
        move = input("Please enter your move: ").strip().lower()
        
        if move in pos:
            row, col = pos[move]
            
            if grid[row][col] == ' ':
                grid[row][col] = token
                return (row, col)
            
            else:
                print("Position not empty!")
        
        else:
            print("Invalid Move")

def check_win(grid, token, row, col):
    n = len(grid)
    
    #horizontal win
    if all(token == c for c in grid[row]):
        return True
    
    #vertical win
    if all(token == r[col] for r in grid):
        return True
    
    #diagonal win
    if row == col and all(token == grid[rc][rc] for rc in range(n)):
        return True
    
    #anti-diagonal win
    if row + col == n - 1:
        return all(token == grid[rc][n - 1 - rc] for rc in range(n))
    
    return False

def display(grid):
    n = len(grid)
    header = "   | " + " | ".join(string.ascii_uppercase[:n]) + " "
    
    print(header)
    print("-" * len(header))
    for i, row in enumerate(grid, start = 1):
        print(f"{i:>2} | " + " | ".join(cell.upper() for cell in row))
        print("-" * len(header))
        
    print("")
    return None
        
def main():
    n = 3
    limit = 0
    pos_map = get_pos_map(n)
    grid = set_grid(n)
    players = list(set_players().items())
    
    display(grid)
    
    while True:
        
        for player, token in players:
            
            if limit == n**2:
                print("It's a draw!")
                return None
            
            row, col = player_move(grid, token, player, pos_map)
            display(grid)
            limit += 1
            
            if check_win(grid, token, row, col):
                print(f"{player} are winner!")
                return None

if __name__ == "__main__":
    main()
