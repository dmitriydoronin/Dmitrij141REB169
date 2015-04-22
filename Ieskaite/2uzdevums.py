# Fails: 2.uzdevums ieskaite
# Autors: Dmitrijs Doronins

from PythonMagick import Image

bilde = Image ("6x6",'white')

bilde.pixelColor( 1,1, "#48D1CC")

bilde.pixelColor( 2,1, "#3CB371")
bilde.pixelColor( 1,2, "#3CB371")

bilde.pixelColor( 3,1, "#9ACD32")
bilde.pixelColor( 2,2, "#9ACD32")
bilde.pixelColor( 1,3, "#9ACD32")

bilde.pixelColor( 4,1, 'yellow')
bilde.pixelColor( 3,2, 'yellow')
bilde.pixelColor( 2,3, 'yellow')
bilde.pixelColor( 1,4, 'yellow')

bilde.pixelColor( 5,1, "#FF8C00")
bilde.pixelColor( 4,2, "#FF8C00")
bilde.pixelColor( 3,3, "#FF8C00")
bilde.pixelColor( 2,4, "#FF8C00")
bilde.pixelColor( 1,5, "#FF8C00")

bilde.pixelColor( 5,2, "#FF4500")
bilde.pixelColor( 4,3, "#FF4500")
bilde.pixelColor( 3,4, "#FF4500")
bilde.pixelColor( 2,5, "#FF4500")

bilde.pixelColor( 5,3, "#FF69B4")
bilde.pixelColor( 4,4, "#FF69B4")
bilde.pixelColor( 3,5, "#FF69B4")

bilde.pixelColor( 5,4, "#C71585")
bilde.pixelColor( 4,5, "#C71585")

bilde.pixelColor( 5,5, "#8B008B")



bilde.scale("200x200")

bilde.write("2uzd.png")
