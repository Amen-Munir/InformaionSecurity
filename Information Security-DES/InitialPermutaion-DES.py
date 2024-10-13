permutationTable =[
    58,50,42,34,26,18,10,2,
    60,52,44,36,28,20,12,4,
    62,54,46,38,30,22,14,6,
    64,56,48,40,32,24,16,8,
    57,49,41,33,25,17,9,1,
    59,51,43,35,27,19,11,3,
    61,53,45,37,29,21,13,5,
    63,55,47,39,31,23,15,7
                   ]
 

def binarytoHex(binary_str):
    hex_str = hex(int(binary_str, 2))[2:].zfill(16)
    return hex_str

binary="0000000000000000000000001000000000000000000000000000000000000010"

def convertTo8by8Matrix(binary):
    matrix = []
    for i in range(0, 64, 8): 
        row = list(binary[i:i+8]) 
        matrix.append(row)
    return matrix

def ConvertBacktoStr(matrix):
    binary = ""
    for row in matrix:
        binary += "".join(row)
    return binary


matrix=convertTo8by8Matrix(binary)

indicesOfOnesInInput = [(row_index, col_index) 
                   for row_index, row in enumerate(matrix) 
                   for col_index, value in enumerate(row) if value == '1'] # gives indexes of those bits whch have 1s in the matrix 

# my LOGIC-----i am going to map those on the ip table and swap both of the index 



def permutation(matrix, ipTable, indexOfOnes): # matrix pay jis index pay meri 1 value this usko map kiya on permutation table and swapped that value with whatever bit ip table has in matrix 
    
    newMatrix = [row[:] for row in matrix]   # matrix ki copy banai
    for rowInd, colInd in indexOfOnes: #iterate throw the list that has ones walay index 
        ipTableIndex = ipTable[rowInd * 8 + colInd] - 1    # formula for calculating the elemt is row*8+col (-1 isliye kyon k list start from zero and ip table and bits start from 1 - desired element ek peechay huga )
        newRowInd = ipTableIndex // 8
        newColInd = ipTableIndex % 8
        #swap 
        #temp=25th bit
        #25th bit =64th bit 
        #64th bit = temp

        temp = newMatrix[newRowInd][newColInd]  
        newMatrix[newRowInd][newColInd] = newMatrix[rowInd][colInd]  
        newMatrix[rowInd][colInd] = temp  

    return newMatrix


permuted_matrix = permutation(matrix, permutationTable, indicesOfOnesInInput)

binary=ConvertBacktoStr(permuted_matrix)    
hex= binarytoHex(binary)
print(hex)







