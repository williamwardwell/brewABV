def calcABV(OG,FG):
    return (OG - FG) * 131

OG = float(raw_input("What was the original gravity reading? "))
FG = float(raw_input("What was the final gravity reading? "))
abv = calcABV(OG,FG)
print "Your ABV is %.2f." % abv
