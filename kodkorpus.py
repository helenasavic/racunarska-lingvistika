with open("korpus.xml", "r", encoding="utf-8") as fajl:
    recnik_imenica=dict()
    for red in fajl:
          if not red.startswith("<"):
           try:
               rec,mala_rec,lema,pos=red.split("\t")
               if pos.startswith("N"):
                   if lema in recnik_imenica.keys():
                       recnik_imenica[lema]=recnik_imenica[lema]+1
                   else: 
                       recnik_imenica[lema]=1
           except:
               print(red)
                      
                      
                    
    with open("recnik_imenica.txt", "a+", encoding="utf-8") as izlaz:
        for l, f in recnik_imenica.items():
            izlaz.write(l + "\t\t" + str(f) + "\n")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
        
        

                
                
        

