#Fails 231.py
#Autors: Dmitrijs Doronins
from PythonMagick import Image

# Izgatavojam jaunu objektu - bilde
# Objekta izmers 3x3 pixels
bilde =Image("3x3", "#22aaff")

# Izveidojam mainigos x un y
x=y=0
#Uzstaada objekta 'bilde' x,y pixela kraasu
bilde.pixelColor( x,y, "#eeff22")

# 3x3 pixels palielina liidz 200x200
bilde.scale ("200x200")

#Objektu 'bilde' ieraksta failaa
bilde.write("231.png")
