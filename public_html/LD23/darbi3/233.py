#Fails 231.py
#Autors: Dmitrijs Doronins
from PythonMagick import Image


bilde =Image("33x33", "#00FF00")

# Izveidojam mainigos x un y

#Uzstaada objekta 'bilde' x,y pixela kraasu

bilde.pixelColor( 4,4, "#eeff23")
bilde.pixelColor( 4,5, "#eeff23")
bilde.pixelColor( 4,6, "#eeff23")
bilde.pixelColor( 4,7, "#eeff23")
bilde.pixelColor( 4,8, "#eeff23")
bilde.pixelColor( 4,9, "#eeff23")
bilde.pixelColor( 4,10, "#eeff23")
bilde.pixelColor( 4,11, "#eeff23")
bilde.pixelColor( 3,11, "#eeff23")
bilde.pixelColor( 2,11, "#eeff23")
bilde.pixelColor( 2,10, "#eeff23")
bilde.pixelColor( 2,9, "#eeff23")
bilde.pixelColor( 3,9, "#eeff23")
bilde.pixelColor( 2,10, "#eeff23")

bilde.pixelColor( 5,10, "#eeff23")
bilde.pixelColor( 6,11, "#eeff23")
bilde.pixelColor( 7,11, "#eeff23")
bilde.pixelColor( 8,11, "#eeff23")
bilde.pixelColor( 9,10, "#eeff23")
bilde.pixelColor( 10,9, "#eeff23")
bilde.pixelColor( 10,8, "#eeff23")

bilde.pixelColor( 10,7, "#eeff23")
bilde.pixelColor( 10,6, "#eeff23")
bilde.pixelColor( 9,5, "#eeff23")

bilde.pixelColor( 8,4, "#eeff23")
bilde.pixelColor( 7,3, "#eeff23")
bilde.pixelColor( 6,2, "#eeff23")

bilde.pixelColor( 5,1, "#eeff23")
bilde.pixelColor( 4,1, "#eeff23")
bilde.pixelColor( 3,1, "#eeff23")
bilde.pixelColor( 2,2, "#eeff23")
bilde.pixelColor( 1,3, "#eeff23")
bilde.pixelColor( 2,10, "#eeff23")
bilde.pixelColor( 7,2, "#eeff23")

bilde.pixelColor( 8,3, "#eeff23")
bilde.pixelColor( 9,4, "#eeff23")
bilde.pixelColor( 10,5, "#eeff23")






# 3x3 pixels palielina liidz 200x200
bilde.scale ("500x500")

#Objektu 'bilde' ieraksta failaa
bilde.write("233.png") 





