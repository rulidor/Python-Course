import hw4_part2 

prefixes_dict = {}
hw4_part2.add_prefixes(prefixes_dict,"repair")
print(prefixes_dict == {'r': ['repair'], 're': ['repair'], 'rep': ['repair'], 'repa': ['repair'], 'repai': ['repair'], 'repair': ['repair']})

prefixes_dict = {}
hw4_part2.add_prefixes(prefixes_dict,"clean")
print(prefixes_dict == {'c': ['clean'], 'cl': ['clean'], 'cle': ['clean'], 'clea': ['clean'], 'clean': ['clean']})

hw4_part2.add_prefixes(prefixes_dict,"combining")
print(prefixes_dict == {'c': ['clean', 'combining'], 'cl': ['clean'], 'cle': ['clean'], 'clea': ['clean'], 'clean': ['clean'], 'co': ['combining'], 'com': ['combining'], 'comb': ['combining'], 'combi': ['combining'], 'combin': ['combining'], 'combini': ['combining'], 'combinin': ['combining'], 'combining': ['combining']})

hw4_part2.add_prefixes(prefixes_dict,"combining")
print(prefixes_dict == {'c': ['clean', 'combining'], 'cl': ['clean'], 'cle': ['clean'], 'clea': ['clean'], 'clean': ['clean'], 'co': ['combining'], 'com': ['combining'], 'comb': ['combining'], 'combi': ['combining'], 'combin': ['combining'], 'combini': ['combining'], 'combinin': ['combining'], 'combining': ['combining']})


prefixes_dict = {}
hw4_part2.add_all_prefixes(prefixes_dict,["clean","multiplication","addict"])
print(prefixes_dict == {'c': ['clean'], 'cl': ['clean'], 'cle': ['clean'], 'clea': ['clean'], 'clean': ['clean'], 'm': ['multiplication'], 'mu': ['multiplication'], 'mul': ['multiplication'], 'mult': ['multiplication'], 'multi': ['multiplication'], 'multip': ['multiplication'], 'multipl': ['multiplication'], 'multipli': ['multiplication'], 'multiplic': ['multiplication'], 'multiplica': ['multiplication'], 'multiplicat': ['multiplication'], 'multiplicati': ['multiplication'], 'multiplicatio': ['multiplication'], 'multiplication': ['multiplication'], 'a': ['addict'], 'ad': ['addict'], 'add': ['addict'], 'addi': ['addict'], 'addic': ['addict'], 'addict': ['addict']})

hw4_part2.add_all_prefixes(prefixes_dict,["clear","multiplication","grid"])
print(prefixes_dict == {'c': ['clean', 'clear'], 'cl': ['clean', 'clear'], 'cle': ['clean', 'clear'], 'clea': ['clean', 'clear'], 'clean': ['clean'], 'm': ['multiplication'], 'mu': ['multiplication'], 'mul': ['multiplication'], 'mult': ['multiplication'], 'multi': ['multiplication'], 'multip': ['multiplication'], 'multipl': ['multiplication'], 'multipli': ['multiplication'], 'multiplic': ['multiplication'], 'multiplica': ['multiplication'], 'multiplicat': ['multiplication'], 'multiplicati': ['multiplication'], 'multiplicatio': ['multiplication'], 'multiplication': ['multiplication'], 'a': ['addict'], 'ad': ['addict'], 'add': ['addict'], 'addi': ['addict'], 'addic': ['addict'], 'addict': ['addict'], 'clear': ['clear'], 'g': ['grid'], 'gr': ['grid'], 'gri': ['grid'], 'grid': ['grid']})


prefixes_dict = {}
prefixes_dict = hw4_part2.init_from_url("https://www.dropbox.com/s/0mpu0tag3wkzu2b/example1.txt?dl=1")
print(prefixes_dict == {'a': ['abba', 'abbey', 'aba'], 'ab': ['abba', 'abbey', 'aba'], 'abb': ['abba', 'abbey'], 'abba': ['abba'], 'abbe': ['abbey'], 'abbey': ['abbey'], 'aba': ['aba'], 's': ['small'], 'sm': ['small'], 'sma': ['small'], 'smal': ['small'], 'small': ['small']})

prefixes_dict = {}
prefixes_dict = hw4_part2.init_from_url("https://www.dropbox.com/s/5cqria10918p5o7/example2.txt?dl=1")
print(prefixes_dict == {'s': ['smell', 'smelly', 'small', 'snail'], 'sm': ['smell', 'smelly', 'small'], 'sme': ['smell', 'smelly'], 'smel': ['smell', 'smelly'], 'smell': ['smell', 'smelly'], 'smelly': ['smelly'], 'sma': ['small'], 'smal': ['small'], 'small': ['small'], 'sn': ['snail'], 'sna': ['snail'], 'snai': ['snail'], 'snail': ['snail'], 'g': ['gone', 'going', 'go'], 'go': ['gone', 'going', 'go'], 'gon': ['gone'], 'gone': ['gone'], 'goi': ['going'], 'goin': ['going'], 'going': ['going']})


print(hw4_part2.autocomplete(prefixes_dict,"s") == ['smell', 'smelly', 'small', 'snail'])

print(hw4_part2.autocomplete(prefixes_dict,"go") == ['gone', 'going', 'go'])

print(hw4_part2.autocomplete(prefixes_dict,"Noa") == [])