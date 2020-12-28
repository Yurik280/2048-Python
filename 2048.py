from random import randint
import TableIt

cells = 3
random_base = 3
matrix = []


def main():
    create_matrix()
    for i in range(3):
        rand_cell_fill()
    while space_check():
        print_matrix()    
        press_key()
        rand_cell_fill()
        print()
    print('Game over!')


def space_check():
    for i in range(cells):        
        for j in range(cells):        
            if matrix[i][j] == ' ':
                return True
    return False


def create_matrix():
    for i in range(cells):
        matrix.append([])
        for j in range(cells):        
            matrix[i].append(' ')


def rand_cell_fill():
    while True:    
        x_cell = randint(1,cells-1)
        y_cell = randint(1,cells-1)
        if matrix[x_cell][y_cell] == ' ':
            matrix[x_cell][y_cell] =  2 ** randint(1,random_base)
            break
                        

def print_matrix():
    TableIt.printTable(matrix)
    # for i in range(cells):
    #     print(matrix[i])


def press_key():
    key = input('wasd: ')
    if key == 'w':
        move_up()
    elif key == 'a':
        move_left()
    elif key == 's':
        move_down()
    elif key == 'd':
        move_right()        


def move_up():    
    print('UP')
    for i in range(cells): #rows       
        for j in range(cells): #columns
            if matrix[i][j] == ' ':
                for k in range(i+1,cells):
                    if matrix[k][j] != ' ':
                        for l in range(k+1,cells):
                            if matrix[l][j] != ' ':
                                if matrix[k][j] == matrix[l][j]:
                                    matrix[k][j] *= 2
                                    matrix[l][j] = ' '
                                    break
                                else:
                                    break
                        matrix[i][j] = matrix[k][j]
                        matrix[k][j] = ' '
                        break
            else:
                for k in range(i+1,cells):
                    if matrix[k][j] != ' ':
                        if matrix[i][j] == matrix[k][j]:
                            matrix[i][j] *= 2
                            matrix[k][j] = ' '
                            break
                        else:
                            break        
    
    

def move_down():
    print('DOWN')
    for i in range(cells-1,-1,-1): #rows       
        for j in range(cells): #columns
            if matrix[i][j] == ' ':
                for k in range(i-1,-1,-1):
                    if matrix[k][j] != ' ':
                        for l in range(k-1,-1,-1):
                            if matrix[l][j] != ' ':
                                if matrix[k][j] == matrix[l][j]:
                                    matrix[k][j] *= 2
                                    matrix[l][j] = ' '
                                    break
                                else:
                                    break
                        matrix[i][j] = matrix[k][j]
                        matrix[k][j] = ' '
                        break
            else:
                for k in range(i-1,-1,-1):
                    if matrix[k][j] != ' ':
                        if matrix[i][j] == matrix[k][j]:
                            matrix[i][j] *= 2
                            matrix[k][j] = ' '
                            break
                        else:
                            break  
    
    

def move_left():   
    print('LEFT')
    for i in range(cells): #rows       
        for j in range(cells): #columns   
            if matrix[i][j] == ' ':         
                for k in range(j+1,cells): #
                    if matrix[i][k] != ' ':
                        for l in range(k+1,cells):
                            if matrix[i][l] != ' ':
                                if matrix[i][k] == matrix[i][l]:
                                    matrix[i][k] *= 2
                                    matrix[i][l] = ' '
                                    break
                                else:
                                    break
                        matrix[i][j] = matrix[i][k]
                        matrix[i][k] = ' '
                        break
            else:
                for k in range(j+1,cells):
                    if matrix[i][k] != ' ':
                        if matrix[i][j] == matrix[i][k]:
                            matrix[i][j] *= 2
                            matrix[i][k] = ' '
                            break
                        else:
                            break        
    
    

def move_right():
    print('RIGHT')   
    for i in range(cells): #rows        
        for j in range(cells-1,-1,-1): #columns
            if matrix[i][j] == ' ':
                for k in range(j-1,-1,-1):
                    if matrix[i][k] != ' ':
                        for l in range(k-1,-1,-1):
                            if matrix[i][l] != ' ':
                                if matrix[i][k] == matrix[i][l]:
                                    matrix[i][k] *= 2
                                    matrix[i][l] = ' '
                                    break
                                else:
                                    break
                        matrix[i][j] = matrix[i][k]
                        matrix[i][k] = ' '
                        break
            else:
                for k in range(j-1,-1,-1):
                    if matrix[i][k] != ' ':
                        if matrix[i][j] == matrix[i][k]:
                            matrix[i][j] *= 2
                            matrix[i][k] = ' '
                            break
                        else:
                            break        


main()
