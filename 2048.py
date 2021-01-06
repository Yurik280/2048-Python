from random import randint
import TableIt

CELLS = 3
RANDOM_BASE = 3

matrix = []


def main():
    create_matrix()
    for i in range(3):
        rand_cell_fill()
    while space_check():
        print_matrix(matrix)    
        if not press_key():
            continue
        rand_cell_fill()
        print()
    print_matrix(matrix)    
    print('Game over!')


def space_check():
    for row in range(CELLS):        
        for column in range(CELLS):        
            if matrix[row][column] == 0:
                return True
    return False


def create_matrix():
    for i in range(CELLS):
        matrix.append([])
        for j in range(CELLS):        
            matrix[i].append(0)


def rand_cell_fill():
    while True:    
        row = randint(0,CELLS-1)
        column = randint(0,CELLS-1)
        if matrix[row][column] == 0:
            matrix[row][column] =  2 ** randint(1,RANDOM_BASE)
            break
                        

def print_matrix(matrix):
    new_matrix = []
    for i in range(CELLS):
        new_matrix.append([])
        for j in range(CELLS):        
            new_matrix[i].append('')
    for k in range(CELLS):
        for l in range(CELLS):                    
            if matrix[k][l] != 0:
                new_matrix[k][l] = matrix[k][l]
    TableIt.printTable(new_matrix)


def press_key():
    key = input('wasd: ')
    move_key = True
    if key == 'w':
        move_up()
    elif key == 'a':
        move_left()
    elif key == 's':
        move_down()
    elif key == 'd':
        move_right()   
    else:
        move_key = False
    return move_key


def move_up():    
    print('UP')
    for row in range(CELLS):       
        for column in range(CELLS): 
            if matrix[row][column] == 0:
                for k in range(row+1,CELLS): #looking for the first no-empty-cell
                    if matrix[k][column] != 0:
                        for l in range(k+1,CELLS): # #looking for the second no-empty-cell
                            if matrix[l][column] != 0:
                                if matrix[k][column] == matrix[l][column]:
                                    matrix[k][column] *= 2
                                    matrix[l][column] = 0
                                    break
                                else:
                                    break
                        matrix[row][column] = matrix[k][column]
                        matrix[k][column] = 0
                        break
            else: # if the cell in not empty
                for k in range(row+1,CELLS): #looking for the next no-empty-cell
                    if matrix[k][column] != 0: 
                        if matrix[row][column] == matrix[k][column]:
                            matrix[row][column] *= 2
                            matrix[k][column] = 0
                            break
                        else:
                            break        
    
    

def move_down():
    print('DOWN')
    for row in range(CELLS-1,-1,-1): #rows       
        for column in range(CELLS): #columns
            if matrix[row][column] == 0:
                for k in range(row-1,-1,-1):
                    if matrix[k][column] != 0:
                        for l in range(k-1,-1,-1):
                            if matrix[l][column] != 0:
                                if matrix[k][column] == matrix[l][column]:
                                    matrix[k][column] *= 2
                                    matrix[l][column] = 0
                                    break
                                else:
                                    break
                        matrix[row][column] = matrix[k][column]
                        matrix[k][column] = 0
                        break
            else:
                for k in range(row-1,-1,-1):
                    if matrix[k][column] != 0:
                        if matrix[row][column] == matrix[k][column]:
                            matrix[row][column] *= 2
                            matrix[k][column] = 0
                            break
                        else:
                            break  
    
    

# def move_left():   
#     print('LEFT')
#     for row in range(CELLS): #rows       
#         for column in range(CELLS): #columns   
#             if matrix[row][column] == 0:         
#                 for k in range(column+1,CELLS): #
#                     if matrix[row][k] != 0:
#                         for l in range(k+1,CELLS):
#                             if matrix[row][l] != 0:
#                                 if matrix[row][k] == matrix[row][l]:
#                                     matrix[row][k] *= 2
#                                     matrix[row][l] = 0
#                                     break
#                                 else:
#                                     break
#                         matrix[row][column] = matrix[row][k]
#                         matrix[row][k] = 0
#                         break
#             else:
#                 for k in range(column+1,CELLS):
#                     if matrix[row][k] != 0:
#                         if matrix[row][column] == matrix[row][k]:
#                             matrix[row][column] *= 2
#                             matrix[row][k] = 0
#                             break
#                         else:
#                             break        


def move_left():   
    print('LEFT')
    is_order_direct = True
    for row in range(CELLS):        
        for column in range(CELLS):    
            if matrix[row][column] == 0: 
                first_no_empty_cell = find_next_no_empty_cell_in_row(row, column, is_order_direct)
                if first_no_empty_cell != -1:  
                    second_no_empty_cell = find_next_no_empty_cell_in_row(first_no_empty_cell, column+1, is_order_direct)
                    if second_no_empty_cell != -1:
                        if matrix[row][first_no_empty_cell] == matrix[row][second_no_empty_cell]:
                            sum_and_remove(row, first_no_empty_cell, second_no_empty_cell)
                move(row, column, first_no_empty_cell)
            else: # if the cell is not empty
                next_no_empty_cell = find_next_no_empty_cell_in_row(row, column, is_order_direct)
                if next_no_empty_cell != -1:      
                    if matrix[row][column] == matrix[row][next_no_empty_cell]:
                            sum_and_remove(row, column, next_no_empty_cell)


def sum_and_remove(row, column1, column2):
    matrix[row][column1] *= 2
    matrix[row][column2] = 0


def move(row, column1, column2):
    matrix[row][column1] = matrix[row][column2]
    matrix[row][column2] = 0

    
def find_next_no_empty_cell_in_row(row, column, is_order_direct):
    if is_order_direct:    
        search_range = range(column+1,CELLS)
    else:
        search_range = range(column-1,-1,-1)
        
    for k in search_range:
        if matrix[row][k] != 0:
            return k
    return -1
    


def move_right():
    print('RIGHT')   
    for row in range(CELLS): #rows        
        for column in range(CELLS-1,-1,-1): #columns
            if matrix[row][column] == 0:
                for k in range(column-1,-1,-1):
                    if matrix[row][k] != 0:
                        for l in range(k-1,-1,-1):
                            if matrix[row][l] != 0:
                                if matrix[row][k] == matrix[row][l]:
                                    matrix[row][k] *= 2
                                    matrix[row][l] = 0
                                    break
                                else:
                                    break
                        matrix[row][column] = matrix[row][k]
                        matrix[row][k] = 0
                        break
            else:
                for k in range(column-1,-1,-1):
                    if matrix[row][k] != 0:
                        if matrix[row][column] == matrix[row][k]:
                            matrix[row][column] *= 2
                            matrix[row][k] = 0
                            break
                        else:
                            break        


main()
