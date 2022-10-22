#import ascii magic
import ascii_magic

output = ascii_magic.from_image_file("TechVine.jpeg",columns=100,char="&")

# to print the ascii art in terminal
ascii_magic.to_terminal(output)
