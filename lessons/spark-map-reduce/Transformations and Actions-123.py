## 1. Introduction to the Data ##

raw_hamlet = sc.textFile("hamlet.txt")

print(raw_data.take(5))

## 2. The Map Method ##

split_hamlet = raw_hamlet.map(lambda x: (x.split('\t')))

print( split_hamlet.take(5) )

## 4. The FlatMap Method ##

def hamlet_speaks(line):
    id = line[0]
    speaketh = False
    
    if "HAMLET" in line:
        speaketh = True
    
    if speaketh:
        yield id,"hamlet speaketh!"

hamlet_spoken = split_hamlet.flatMap(lambda x: hamlet_speaks(x))
print( hamlet_spoken.take(10))

## 5. Filter Using a Named Function ##

def filter_hamlet_speaks(line):
    if "HAMLET" in line:
        return True    
    return False

hamlet_spoken_lines = split_hamlet.filter(lambda line: filter_hamlet_speaks(line))
hamlet_spoken_lines.take(5)

## 6. Actions ##

spoken_count = hamlet_spoken_lines.count()

spoken_collect = hamlet_spoken_lines.collect()
spoken_101 = spoken_collect[100]