t = 500
p = 500  
h = 500
going = 0
w = -1
while going == 0:
    running = 0
    
    while running == 0:
        w += 1
        
        

        for t in range(w, 500):
            tri = ((t * (t + 1)) / 2)
            
           
            for p in range(0, 500):
                pen = ((p * ((3 * p) - 1)) / 2)
                
                
                if pen == tri:
                    
                    running = 1
                    
                    break
            break
    
                   
    running2 = 0
    

    for h in range(500):
        hex = float(h  * ((2 * h) - 1))
        
        if hex > 2 and hex == tri:
            print(tri)
            
            
            going = 1
            break