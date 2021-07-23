# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 21:44:24 2018

@author: Lidor
"""

def sort_movies(schedule):
    "Returns a sorted list of movies names, according to time of movie and duration"
    sorted_dict=sorted(schedule.items(),key=comperator)
    movies_names=[] #list of movies names that are sorted
    for i in sorted_dict:
        movies_names.append(i[0])
    return movies_names

def comperator(t):
    "Receives a tuple, returns value to determine order"
    return(t[1][0],t[1][1])

def search_movie(movies, free_time, start, end):
    "Checks if a movie is screened in the free time received. If yes, returns movie name. Else, return None"
    if start>end:
        return None
    middle=(start+end)//2
    if free_time[0]==movies[middle][1][0]:
        if free_time[1]==movies[middle][1][1]:
            return movies[middle][0] #returns movie name
        elif free_time[1]<movies[middle][1][1]:
            return search_movie(movies,free_time,start,middle-1)
        else: #ending time wanted is after the cur. movie ending time
            return search_movie(movies,free_time,middle+1,end)
    elif free_time[0]<movies[middle][1][0]:
        return search_movie(movies,free_time,start,middle-1)
    else: #starting time wanted is after the cur. movie srarting time
        return search_movie(movies,free_time,middle+1,end)

def max_sub_set(numbers_set):
    "Prints length of the largest increasing sub sequence"
    return longest_sub_set(numbers_set, len(numbers_set), 0, 0, 0)
    
    
def longest_sub_set(numbers_set, size, i, max_num, count):
    "Returns length of largest increasing sub sequence"
    if i==size: #reached to the end of list
        return count
    length1 = longest_sub_set(numbers_set, size, i + 1, max_num, count)
    if numbers_set[i] >= max_num: #there is an increasing order
        length2 = longest_sub_set(numbers_set, size, i + 1, numbers_set[i], count + 1);
        if length2 > length1:
            length1 = length2
    return length1
