def swapFileData():
    file_a = open('sample1.txt','r')
    file_b = open('sample2.txt','r')

    data_a = file_a.read()
    data_b = file_b.read()

    with open('sample1.txt','w') as a:
        a.write(data_b)
    
    with open('sample2.txt','w') as b:
        b.write(data_a)
    

swapFileData()