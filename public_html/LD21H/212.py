# Vards Uzvards: Dmitrijs Doronins
# Datums: 08.02.2015
# Studenta apliecibas numurs: 141REB169
# Versija: 0.1
# Programma aprekina katru nakoso krasi, ko lietos tekosajam skaitlim

print '<html>'
print '<pre>'
for i in range (11):

    k=i*i;
    print '<br>'
    print "<font color=\"#%f%f0000\">" % (i, i)
    print "Skaitlis: %d \t Kvadrats: %d" % (i, k)
    print "</font>"

print '</pre>'
print '</html>'
