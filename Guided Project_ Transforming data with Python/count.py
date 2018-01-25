import read

df = read.load_data()

long_string = ""
for headline in df['headline']:
    long_string = long_string+" "+str(headline)
    
words = long_string.split(" ")

print( words[0] )
