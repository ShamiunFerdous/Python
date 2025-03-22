with open('demo.txt','r') as file:
    i = 0
    while True:
        i += 1
        line = file.readline()
        if not line:
            break
        
        l1 = line.split(',')[0]
        l2 = line.split(',')[1]
        l3 = line.split(',')[2]
        
        print(f"Line {i}: {l1} {l2} {l3}")
    

""" output: 
Line 1: 76 81 72

Line 2: 75 73 79

Line 3: 70 72 77
"""
        

''' readline method is used to read a single line from the file.'''