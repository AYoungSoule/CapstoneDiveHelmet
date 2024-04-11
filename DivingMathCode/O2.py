O2P = 8 #will be the actual data from the Oxygen pressure sensor
WP = 7 #Will be the actual data from the water pressure sensor
ZA = 9.8 #will be the actual descent acceleration from the accelerometer
TV = 425 #will be replaced with actual volume of available oxygen tank
O2VS = TV
O2V = O2VS #Calcultion of volume of tank filled with oxygen
BR = [15, 15, 15, 15, 15, 15]
BRA = sum(BR)/len(BR) #This is the list and average of said list that will be used to determine the average breathing rate of the user which helps tell how much time is left in trip
ROT = O2V/3 
DT = ROT
ER = ROT
AT = ROT #These are the rule of threes designated oxygen per section of trip amounts based on your starting oxygen volume
DDT = DT/BRA #this tells you how much time you have for your descent trip
DAT = AT/BRA
RDR = 18/60 #recomended average descent rate as we do not have access to the algorithims and mathmatical equations that dive computers use to calculate that stuff
RAR = 9/60 #same as descent but for ascent
ASS_D = 5
ASS_T = 5 #these are the ascent safety stops recomended distances and times
CD = ((WP - 14.7)/.445)*.3048 #this gives current depths in meters based off water pressure
#tO = 0 #time old 
CV = ZA*t + 0
wait(1000)
O2V = O2P * TV
#t1 = 1 #current time
#BRC = (O2VS - O2V)/(t1 - t0)
#BR.append(BRC)
#BRA = sum(BR)/len(BR)
#t0 = t1



while (DT > 0)
    #ZA = sensor
    #WP = sensor
    #O2P = sensor
    CV = ZA*t + CV
    CD = ((WP - 14.7)/.445)*.3048
    DT = O2V - 2*O2VS/3
    if CV > RDR
        WV = TRUE
    print("screen 1: Velocity "&CV)
    print("screen 2: Depth "&CD)
    print("screen 3: Descent Time "&DT)
    if RD <= CD
        WD = TRUE
    if WV == TRUE
        print("screen 4: TOO FAST SLOW DOWN")
    elif WD == TRUE
        print("screen 4: REC DEPTH REACHED")
    else
        print("screen 4: O2 Left "& O2V)
#    t1 = t1+1
#    BRC = (O2VS - O2V)/(t1 - t0)
#    BR.append(BRC)
#    BRA = sum(BRA)/len(BRA)
#    t0 = t1
print("screen 4: Time to Ascend")
AT = ROT
while (AT > 0)
    #ZA = sensor
    #WP = sensor
    #O2P = sensor
    CV = ZA*t + CV
    CD = ((WP - 14.7)/.445)*.3048
    if CV > RAR
        WV = TRUE
    print("screen 1: Velocity "&CV)
    print("screen 2: Depth "&CD)
    print("screen 3: Ascent Time "&AT)
    

    if WV == TRUE
        print("screen 4: TOO FAST SLOW DOWN")
    elif WS == TRUE
        print("screen 4: REC STOP REACHED")
        S = TRUE
    else
        print("screen 4: O2 Left "& O2V)
    while S == TRUE
        #ZA = sensor
        #WP = sensor
        #O2P = sensor
        CV = ZA*t + CV
        CD = ((WP - 14.7)/.445)*.3048
        wait(5000)
        S == FALSE


#####################

#Aden Simplified RGBM theorem: (AT/BR = ceiling(RecD/5m)+RecD/(9m/min))