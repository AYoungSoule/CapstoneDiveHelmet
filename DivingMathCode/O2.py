O2PIS = 8 #will be the actual data from the Oxygen pressure sensor
WPL = [7] #Will be the actual data from the water pressure sensor
ZAL = [9.8] #will be the actual descent acceleration from the accelerometer meter per sec
TV = 425 #will be replaced with actual volume of available oxygen tank
O2V = TV
BR = [15, 15, 15, 15, 15, 15]
BRA = sum(BR)/len(BR) #This is the list and average of said list that will be used to determine the average breathing rate of the user which helps tell how much time is left in trip
ROT = O2V/3 
DT = ROT
ER = ROT
AT = ROT #These are the rule of threes designated oxygen per section of trip amounts based on your starting oxygen volume
DDT = DT/BRA #this tells you how much time you have for your descent trip
DAT = AT/BRA
RDR = 18 #recomended average descent rate as we do not have access to the algorithims and mathmatical equations that dive computers use to calculate that stuff in m per sec
RAR = 9 #same as descent but for ascent meters per min
ASS_D = 5
ASS_T = 5 #these are the ascent safety stops recomended distances and times
CD = ((WP - 14.7)/.445)*.3048 #this gives current depths in meters based off water pressure
t0 = time.time()
CV = ZA*t + 0
O2V = O2P
ATT = AT/BRA #Ascent time in min
RD = ATT/.9 #recomended depth in meters
i = 0

while (DT > 0)
    i = i+1
    t1 = time.time()
    CV = ZA*t + CV
    CD = ((WP - 14.7)/.445)*.3048
    DTR = (O2PI*1.0332 * TV) - AT - ER
    if (t1 - t0) >= 15
       BR.append((DT - DTR)/4)
    t0 = t1
    DT = DTR
    BRA = sum(BR)/len(BR)
    ATT = AT/BRA #Ascent time in min
    RD = ATT/.9
    print("screen 1: Velocity "&CV)
    print("screen 2: Depth "&CD)
    print("screen 3: Descent Time "&DT)
    if CV > RDR
        WV = TRUE
    if RD <= CD
        WD = TRUE
    if BRA > 30
        WB = TRUE
    if WV == TRUE
        print("screen 4: TOO FAST SLOW DOWN")
    elif WB == TRUE
        print("screen 4: SLOW YOUR BREATHING")
    elif WD == TRUE
        print("screen 4: REC DEPTH REACHED")
    else
        print("screen 4: O2 Left "& O2V)
print("screen 4: Time to Ascend")
time.sleep(5)
AT = (O2PI*1.0332 * TV)/2
ER = AT
i = 0
while (AT > 0)
    i = i+1
    t1 = time.time()
    CV = ZA*t + CV
    CD = ((WP - 14.7)/.445)*.3048
    ATR = (O2PI*1.0332 * TV) - ER
    if (t1 - t0) >= 15
        BR.append((AT - ATR)/4)
    t0 = t1
    AT = ATR
    BRA = sum(BR)/len(BR)
    print("screen 1: Velocity "&CV)
    print("screen 2: Depth "&CD)
    print("screen 3: Ascent Time "&AT)
    if CV > RAR
        WV = TRUE
    if BRA > 30
        WB = TRUE
    if WS == TRUE
        print("screen 4: REC STOP REACHED")
        S = TRUE
        ST = time.time()
    elif WV == TRUE
        print("screen 4: TOO FAST SLOW DOWN")
    elif WB == TRUE
        print("screen 4: SLOW YOUR BREATHING")
    else
        print("screen 4: O2 Left "& O2V)
    while S == TRUE
        SC = time.time()
        SR = 300 - SC-ST
        CV = ZA*t + CV
        if CV > 0.5
            print("screen 4: STOP ASCENDING")
        i = i+1
        t1 = time.time()
        CV = ZA*t + CV
        CD = ((WP - 14.7)/.445)*.3048
        ATR = (O2PI*1.0332 * TV) - ER
        if (t1 - t0) >= 15
            BR.append((AT - ATR)/4)
        t0 = t1
        AT = ATR
        BRA = sum(BR)/len(BR)
        print("screen 1: Velocity "&CV)
        print("screen 2: Depth "&CD)
        print("screen 3: Ascent Time "&AT)
        if CV > RAR
            WV = TRUE
        if BRA > 30
            WB = TRUE
        elif WB == TRUE
            print("screen 4: SLOW YOUR BREATHING")
        else
            print("screen 4: O2 Left "& O2V)
        if SR <= 0
            S = FALSE
#####################

#Aden Simplified RGBM theorem: (AT/BR = ceiling(RecD/5m)+RecD/(9m/min))
