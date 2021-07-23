import hw5
#check first of function of exersice 1
schedule = {"Ayka": (14, 16), "3 FACES": (13, 15) , "Leto": (16, 18), "Dogman": (14, 17), "Sorry Angel": (21, 23) } #במו בעבודה
print(hw5.sort_movies(schedule) == ['3 FACES', 'Ayka', 'Dogman', 'Leto', 'Sorry Angel'])
schedule = { } #כשהיא ריקה
print(hw5.sort_movies(schedule) == [])
schedule = {"7":(18, 19), "6": (17, 20),"2": (11, 15), "1": (11, 14), "5": (17, 19), "9":(21, 22), "3":(12, 13), "4":(13, 14), "8":(19, 24)} # עוד כמה דוגמאות
print(hw5.sort_movies(schedule) == ['1', '2', '3', '4', '5', '6', '7', '8', '9'])
schedule = {"7":(11, 19), "6": (7, 20),"2": (2, 20), "1": (1, 7), "5": (6, 12), "9":(21, 22), "3":(4, 8), "4":(6, 9), "8":(11, 20)} # עוד כמה דוגמאות
print(hw5.sort_movies(schedule) == ['1', '2', '3', '4', '5', '6', '7', '8', '9'])

#check seconed function of exe1
movies = [("3 FACES", (13, 15)), ("Ayka", (14, 16)), ("Dogman", (14, 17)), ("Leto", (16, 18)), ("Sorry Angel", (21, 23))]
print(hw5.search_movie(movies, (14,16), 0, len(movies)) == "Ayka") #כמו בעבודה
print(hw5.search_movie(movies, (14,17), 0, len(movies)) == "Dogman")
print(hw5.search_movie(movies, (14,18), 0, len(movies)) == None)

print(hw5.search_movie(movies, (21,23), 0, len(movies)) == "Sorry Angel") #כשזה אחרון
print(hw5.search_movie(movies, (16,18), 0, len(movies)) == "Leto") #כשזה לפני אחרון
print(hw5.search_movie(movies, (13,15), 0, len(movies)) == "3 FACES") #כשזה ראשון

movies = [("3 FACES", (14, 17)), ("Ayka", (14, 16)), ("Dogman", (14, 17)), ("Leto", (16, 18)), ("Sorry Angel", (21, 23))] #כשיש כמה במקומות שונים
print(hw5.search_movie(movies, (14,17), 0, len(movies)) == "Dogman")
movies = [("3 FACES", (14, 17)), ("Ayka", (14, 16)), ("Dogman", (14, 17)), ("Leto", (16, 18)), ("Sorry Angel", (16, 18))]
print(hw5.search_movie(movies, (16,18), 0, len(movies)) == "Sorry Angel")

sequence = [45, 1, 21, 3, 33, 6, 53, 9, 0, 18] #כמו בדוגמה
print(hw5.max_sub_set(sequence) == 5)
sequence = []#כשזה ריק
print(hw5.max_sub_set(sequence) == 0)
sequence = [71, 84, 4, 6, 92, 57, 42, 99, 31, 16, 51, 29]
print(hw5.max_sub_set(sequence) == 4)
sequence = [77, 86, 11, 19, 69, 85, 72, 15, 60, 5, 26, 67]
print(hw5.max_sub_set(sequence) == 4)
sequence = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
print(hw5.max_sub_set(sequence) == 6)
sequence = [18,40,46,45,27,23,99,60,37,52,69,49,22,57,76,68,86,98,28,8,3,15,47,17,4]
print(hw5.max_sub_set(sequence) == 8)