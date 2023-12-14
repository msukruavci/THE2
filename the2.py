def check_month(month_calendar):


    week1 = month_calendar[0:5]
    week2 = month_calendar[5:10]
    week3 = month_calendar[10:15] 
    week4 = month_calendar[15:20]
    week5 = ["null","null","null","null","null"]
    def checkweek(week):
        if(len(week) < 5):
            week.append("null")
            if(len(week) < 5):
                week.append("null")
                if(len(week) < 5):
                    week.append("null")
                    if(len(week) < 5):
                        week.append("null")
                        if(len(week) < 5):
                            week.append("null")
    checkweek(week1)
    checkweek(week2)
    checkweek(week3)
    checkweek(week4)        
    if(len(month_calendar) > 20):
        week5 = month_calendar[20:]


    breaches = []

   
    


    mombreaches1 = week1.count("m")
    mombreaches2 = week2.count("m")
    mombreaches3 = week3.count("m")
    mombreaches4 = week4.count("m")
    motherbreaches = 0

    
    if(mombreaches1 > 1):
        motherbreaches = motherbreaches + 1
    if(mombreaches2 > 1):
        motherbreaches = motherbreaches + 1
    if(mombreaches3 > 1):
        motherbreaches = motherbreaches + 1        
    if(mombreaches4 > 1):
        motherbreaches = motherbreaches + 1


    momamount = month_calendar.count("m")

    if( motherbreaches > 0):
        breaches.append(1)
    
    elif("m" in month_calendar):
        if( momamount  > 1):
            momindex1 = month_calendar.index("m")
            momindex2 = month_calendar.index("m",momindex1 + 1 )
            
            if((momindex2 - momindex1) %5 != 0):
                    breaches.append(1)
            
            
            if(month_calendar.count("m") >= 3):
                momindex3 = month_calendar.index("m",momindex2 + 1 )
                if( (momindex3 - momindex2) %5 != 0) :
                    breaches.append(1)
                    
                if(month_calendar.count("m") >= 4):
                    momindex3 = month_calendar.index("m",momindex2 + 1 )           
                    momindex4 = month_calendar.index("m",momindex3 + 1 )

                    if(momindex4 - momindex3) %5 != 0:
                        breaches.append(1)

        if("m" in week5):
            if(week5.count("m") > 1):
                breaches.append(1)

            momindex1 = month_calendar.index("m")
            if(week5.index("m") != (momindex1)%5):
                breaches.append(1)
            

    
            




    dadmount = month_calendar.count("f")

    
    

    

    if ( dadmount > 2 ):
        breaches.append(2)
    
    

    elif(dadmount == 2):
        dadindex1 = month_calendar.index("f")
        month_calendar.pop(dadindex1)
        dadindex2 = month_calendar.index("f") + 1
        month_calendar.insert(dadindex1,"f")
       
        
        if((dadindex2 - dadindex1) == 1) and ((((dadindex2) %5 != 0))):
            breaches.append(2)

    
    




    

    gmweek1 = "g" == week1[2]
    gmweek2 = "g" == week2[2]
    gmweek3 = "g" == week3[2]
    gmweek4 = "g" == week4[2]

    if((gmweek1 + gmweek2 + gmweek3 + gmweek4) > 1):
        breaches.append(4)
   

    

    a1week1list = [week1[0], week1[2], week1[3]]
    a1week2list = [week2[0], week2[2], week2[3]]
    a1week3list = [week3[0], week3[2], week3[3]]
    a1week4list = [week4[0], week4[2], week4[3]]
    

    a1week1 = "a1" in a1week1list
    a1week2 = "a1" in a1week2list
    a1week3 = "a1" in a1week3list
    a1week4 = "a1" in a1week4list
    a1week5 = "a1" == week5[0]
    
    if( a1week1 or a1week2 or a1week3 or a1week4 or a1week5):
        breaches.append(5)
      




    

    def aunt2check (week):
        a = week.count("a1")
        b = week.count("a2")
        if(a > 0 and b > 0 ):
            a1 = week.index("a1")
            
            if(a1 != 4 and week[a1 + 1] == "a2" ):
                breaches.append(6)
            
            elif(a > 1):
                a2 = week.index("a1",a1 + 1) 
                if(a2 != 4 and week[a2 + 1] == "a2" ):
                    breaches.append(6)
                elif(a > 2):
                    a3 = week.index("a1",a2 + 1)
                    if(a3 != 4 and week[a3 + 1] == "a2" ):
                        breaches.append(6)
                    elif(a>3):
                        a4 = week.index("a1",a3 + 1)
                        if (a4 != 4 and week.index("a2") != 0):
                            breaches.append(6) 
    aunt2check(week1)
    aunt2check(week2)
    aunt2check(week3)
    aunt2check(week4)
    if("a1" in week5 and "a2" in week5):
        if(week5.index("a1") == 0):
            breaches.append(6)

        





    
    nweeklist1 = [week1[3],week1[4]]
    nweeklist2 = [week2[3],week2[4]]
    nweeklist3 = [week3[3],week3[4]]
    nweeklist4 = [week4[3],week4[4]]
   

    nweek1 = "n" in nweeklist1
    nweek2 = "n" in nweeklist2
    nweek3 = "n" in nweeklist3
    nweek4 = "n" in nweeklist4
    
    
    if( nweek1 or nweek2 or nweek3 or nweek4):
        breaches.append(7)
    
    

    

    cost = 0

    

    mom = month_calendar.count("m") 
    dad = month_calendar.count("f")
    gm = month_calendar.count("g")
    aunt1 = month_calendar.count("a1")
    aunt2 = month_calendar.count("a2")
    n = month_calendar.count("n")
    bmonth = month_calendar.count("b")
    

    
    ncost = 0
    if ("n" in month_calendar): 
        ncost = (1 - 5**n) / (1-5)  - 1
    
    cost = (mom * 10) + (dad *20) + (gm * 50) + (aunt1 * 32) + (aunt2 * 27) + ncost + (bmonth*30)
    

    

    def babysittercost():
        
        extracost1 = 0

        

        if(week1[4] == week2[0] and week1[4] == "b"):
            extracost1 += 60
        if(week2[4] == week3[0]) and week2[4] == "b":
            extracost1 += 60
        if(week3[4] == week4[0]) and week3[4] == "b":
            extracost1 += 60
        if(week4[4] == week5[0]) and week4[4] == "b":
            extracost1 += 60
        
        
        def checkekstra(week):
            extracost2 = 0
            b = week.count("b")
            if(b == 2):
                b1 = week.index("b")
                b2 = week.index("b", b1 + 1)
                if not(b1 == 0 and b2 == 4):
                    extracost2 += (b2 - b1 - 1)*30    
            if(b == 3):
                b1 = week.index("b")
                b2 = week.index("b", b1 + 1)
                b3 = week.index("b",b2 + 1)
                extracost2 += (b2 - b1 - 1)*30 
                extracost2 += (b3 - b2 - 1)*30
            if(b == 4):
                b1 = week.index("b")
                b2 = week.index("b", b1 + 1)
                b3 = week.index("b",b2 + 1)
                b4 = week.index("b", b3 + 1)
                if not(b1 != 0 or b4 != 4):
                    extracost2 += 30     
            
            return  extracost2
            
        weekextras = checkekstra(week1) + checkekstra(week2) + checkekstra(week3) + checkekstra(week4)

        return extracost1 + weekextras  
        
    cost = cost + babysittercost()
    
    
    
    if(len(breaches) == 0):
    	return cost
    else:
        breaches = set(breaches)
        breaches = list(breaches)

        return breaches
    
    	
    	
    	
    	





