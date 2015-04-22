# Autors: Dmitrijs Doronins
# Studenta apliecibas numurs: 141REB169
# Programma aprekinas un izvadis datora terminala aprekinatas izeja.V un V1.I pie minimalas x vertibas

x = raw_input("Vai jus gribat aprekinos izmantojot vienu R1 vertibu ? (Yes/No): ")
if(x == "Yes"):
    r = raw_input("Ievadiet rezistora R1 vertibu: ")
    r1=float(r)
    r2 = 50
    u = 16.9
    i = u/(r1+r2)
    u2 = u*r2/(r1+r2)
    print "Strava kede ir %s A, Spriegums U2 ir %s V" %(i, u2)
elif(x == "No"):
    rt = raw_input("Ievadiet rezistora R1 vertibu: ")
    rt1 = int(rt)
    rtt = raw_input("Ievadiet rezistora R2 vertibu: ")
    rt2 = int(rtt)
    rsolis = raw_input("Ievadiet rezistora sola starp sakuma un beigu vertibam: ")
    rt3 = float(rsolis)
    r2 = 50
    u = 16.9
    k1 = (rs2-rs1)/rt3
    k = int(k1)
    for z in range(k+1):
        i = u/(rt1+z*rt3+r2)
        u2 = u*r2/(rt1+z*rt3+r2)
        print "%s) Stravas kede ir %s A, Spriegums U2 or %s V, R1 = %s Ohm" %(z+1, i, u2, rs1+z*rs3)
elif(x != "No" or x != "Yes"):
    print "Nepareizi ievadita atbilde. Palidiet programmu velreiz. Izmantojiet (Yes/No)"
        
