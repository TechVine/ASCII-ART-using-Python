import ascii_magic
output=ascii_magic.from_image_file('Hacktoberfest.jpg',columns=100,char="&")
ascii_magic.to_terminal(output)