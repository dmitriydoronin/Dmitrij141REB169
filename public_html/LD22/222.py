# Dmitrijs Doronins
# 221.py > 222.py(HTML)

f = open("222.html", "w")
print >>f, "<html>"
print >>f, '<table border="1">'
rt = raw_input("ievadiet rezistora R1 sakuma vertibu: ")
rt1 = int(rt)
rtt = raw_input("ievadiet rezistora R1 beigu vertibu: ")
rt2 = int(rtt)
rsolis = raw_input("ievadiet rezistora sola vertibu starp sakuma un beigu vertibam: ")
rt3 = float(rsolis)
r2 = 50
u = 23.4
k1 = (rt2-rt1)/rt3
k = int(k1)
print >>f, "<tr>"
print >>f, "<td>R1, Ohm</td>"
print >>f, "<td>I, A</td>"
print >>f, "<td>U2, V</td>"
print >>f, "</tr>"
for z in range(k+1):
    i = u/(rt1+z*rt3+r2)
    u2 = u*r2/(rt1+z*rt3+r2)
    xx = rt1+z*rt3
    print >>f, "<tr>"
    print >>f, "<td>%.0f</td>" % xx
    print >>f, "<td>%.3f</td>" % i
    print >>f, "<td>%.3f</td>" % u2
print >>f, "</html>"
f.close()
