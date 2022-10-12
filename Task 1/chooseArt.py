import ascii_magic 

Hacktober = ascii_magic.from_image_file("Hacktoberfest.jpg", columns = 200, char='#')
Pikachu = ascii_magic.from_image_file("Pikachu.jpg", columns = 200, char='#')
TechVine = ascii_magic.from_image_file("TechVine.jpg", columns = 200, char='#')

inp = int(input('''Choose an ASCII - ART
[1] Hacktober
[2] Pikachu
[3] Tech Vine : '''))

if inp == 1:
    x = Hacktober
elif inp == 2:
    x = Pikachu
elif inp == 3:
    x = TechVine
else:
    print("Invalid Input")



ascii_magic.to_terminal(x)
