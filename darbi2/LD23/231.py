# Fails 231.py
# Autors Dmitrijs Doronins

from PythonMagick import Image

bilde = Image ( "3x3" , "#22aaff" )

x = y = 0

bilde.PixelColor ( x, y, "eeff22" )

bilde.Scale ( "200x200" )

bilde.write ( "231.png" )
