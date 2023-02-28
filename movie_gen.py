## import functions
from random import randrange, shuffle, randint
    
## Create Tree class to more easily create and sort through movies in a genre
class Tree:
    def __init__(self, value):
        self.value = value
        self.child_vals = []
        
    ## method to add movies to a genre tree
    def add_child(self, child_val):
        self.child_vals.append(child_val)
        
    ## method to help more easily move through needed movie values
    def traverse(self):
        traversed = []
        children_to_visit = [self]
        while len(children_to_visit) > 0:
            current_child = children_to_visit.pop()
            children_to_visit += current_child.child_vals
            traversed.append(current_child.get_value())
        return traversed

    ## method to see children nodes
    def get_children(self):
        return self.child_vals
    
    def get_value(self):
        return self.value
           
## creating global variables
genre_start_letter = ["R", "A", "H", "C", "S", "D"]
sort_by_options = ["Time", "Rating"]
sorted_nodes_indexs = []


    
## create list of lists of genre = [[movie, rating / 10, stars (2), length in MIN, rated],...]
    ## Romance = []
        # Can't Buy Me Love, Love Actually, The Notebook, The Titanic
romance = [["Can't Buy Me Love", 6.8, 94, "Patrick Dempsey and Amanda Peterson", "PG-13"],  ["Love Actually", 7.6, 135, "Hugh Grant and Keira Knightly", "R"], ["The Notebook", 7.8, 121, "Ryan Gosling and Rachel McAdams", "PG-13"], ["Titanic", 7.9, 196, "Kate Winslet and Leonardo DiCaprio", "PG-13"]]

    ## Action = []
        ## Die Hard, Maverick, Tron: Legacy, Tomb Raider
action = [["Die Hard", 8.2, 132, "Bruce Willis and Alan Rickman", "R"], ["Maverick", 8.3, 131, "Tom Cruise and Miles Teller", "PG-13"], ["Tron: Legacy", 6.8, 125, "Garrett Hedlund and Olivia Wilde", "PG"], ["Lara Corft: Tomb Raider", 5.7, 100, "Angelina Jolie and Daniel Craig", "PG-13"]]

    ## Horror = []
        ## Scream, Halloween, Friday the 13th, Scream 2
horror = [["Scream", 7.4, 111, "Neve Campbell and Courtney Cox", "R"], ["Halloween", 7.7, 91, "Jamie Lee Curtis and Nancy Kyes", "R"], ["Friday The 13th", 6.4, 95, "Betsy Palmer and Kevin Bacon", "R"], ["Scream 2", 6.3, 120, "Neve Campbell and David Arquette", "R"]]

    ## Comedy = []
        ## Spy, Teladega Nights, 21 Jump Street, The Spy Who dumped me
comedy = [["Spy", 7.0, 130, "Mellissa McCarthy and Jason Statham", "R"], ["Talladega Nights: The Ballad of Ricky Bobby", 6.6, 108, "Will Farrell and John C. Reilley", "PG-13"], ["21 Jump Street", 7.2, 109, "Jonah Hill and Channing Tatum", "R"], ["The Spy Who Dumped Me", 6.0, 118, "Mila Kunis and Kate McKinnon", "R"]]
 
    ## Scifi = []
        ## Star Wars, Avatar, Interstellar, Inception
scifi = [["Star Wars: Episode IV – A New Hope", 8.6, 121, "Harrison Ford and Carrie Fisher", "PG"], ["Avatar", 7.9, 161, "Zoe Saldana and Sam Worthington", "PG-13"], ["Interstellar", 8.6, 169, "Matthew McConaughey and Anne Hathaway", "PG-13"], ["Inception", 8.8, 148, "Tom Hardy and Leonardo DiCaprio", "PG-13"]]
  
    ## Drama = []
        ## Don't Worry Darling, Hidden Figures, 127 Hours, Luckiest Girl Alive
drama = [["Don't Worry Darling", 6.2, 123, "Florence Pugh and Harry Styles", "R"], ["Hidden Figures", 7.8, 127, "Taraji P. Henson and Octavia Spencer", "PG"], ["127 Hours", 7.6, 94, "James Franco and Kate Mara", "R"], ["Luckiest Girl Alive", 6.4, 115, "Mila Kunis and Chiara Aurelia", "R"]]
 
    ## append all into genre list
genres_string = ["Romance", "Action", "Horror", "Comedy", "Scifi", "Drama"]
genres_list = [romance, action, horror, comedy, scifi, drama]




## create quicksort function to sort quicker and can sort rating or movie length
def quicksort(lst, start_index, end_index):
    if start_index >= end_index:
        return 
    else:
        # find random element in list to be pivot point
        pivot_index = randrange(start_index, end_index + 1)
        pivot_val = lst[pivot_index]
        # swap random element with end value and make two new lists
        lst[end_index], lst[pivot_index] = lst[pivot_index], lst[end_index]
        ## looking at values in front of pivot now end and start element, and will move
        ## to the right when a value is less than the pivot by increasing the index and
        ## swapping the value with the start value then after all possible swaps switching 
        ## the pivot element with the pointer element
        less_than_pointer = start_index
        for index in range(start_index, end_index):
            # find elements out of order
            if lst[index] < pivot_val:
                lst[index], lst[less_than_pointer] = lst[less_than_pointer], lst[index]
                less_than_pointer += 1
        ## now swapping the pointer element and where the original start element is to be
        ## able to create two new sublists and call quicksort recurrsively unil the list is 
        ## sorted
        lst[end_index], lst[less_than_pointer] = lst[less_than_pointer], lst[end_index]                                                  
        quicksort(lst, start_index, less_than_pointer - 1)
        quicksort(lst, less_than_pointer + 1, end_index)
                                                     
## create tree based on sort by input function
## need some global variables for the dictionaries to access in different functions

sort_dict_time = {}
sort_dict_rating = {}

def sort_by_tree(genre, sort_by):
    genre_index = find_index(genre, genres_list)
    genre_tree = Tree(genres_string[genre_index])
    sorted_keys_time = []
    sorted_keys_rating = []
## make time branch on tree with creating dictionary mapping to genre and each movie index with time key
    time = Tree("Time")
    genre_tree.add_child(time)
    index_time = 0
    for movie in genres_list[genre_index]:
        time_num = movie[2]
        sort_dict_time[time_num] = index_time
        sorted_keys_time.append(movie[2])
        index_time += 1
    quicksort(sorted_keys_time, 0, len(sorted_keys_time) - 1)
    for key in sorted_keys_time:
        movie_index = sort_dict_time.get(key)
        movie_index = Tree(movie_index)
        time.add_child(movie_index)
## make rating branch on tree with creating dictionary mapping to genre and each movie index with time key   
    rating = Tree("Rating")
    genre_tree.add_child(rating)
    index_rating = 0
    for movie in genres_list[genre_index]:
        rating_num = movie[1]
        sort_dict_rating[rating_num] = index_rating
        sorted_keys_rating.append(movie[1])
        index_rating += 1
    quicksort(sorted_keys_rating, 0, len(sorted_keys_rating) - 1)
    for key in sorted_keys_rating:
        movie_index = sort_dict_rating.get(key)
        movie_index = Tree(movie_index)
        rating.add_child(movie_index)
    return genre_tree

## function to just find the index in a list
def find_index(value, lst):
    index = 0
    while index < len(lst):
        if lst[index] == value:
            return index
        index += 1
    return None

        
    
## movie title, rating, time, starring, rated
def lister(genre, sort_by):
    tree = sort_by_tree(genre, sort_by)
    ## this should give nodes_list a value of [rating, movie_idx, ..., last movie idx, time, movie idx, ...]
    nodes_list = tree.traverse()
    ## rating is the first to show up
    rating_index = find_index("Rating", nodes_list)
    ## time is second to show up
    time_index = find_index("Time", nodes_list)
    rating_lst = nodes_list[rating_index + 1:time_index]
    time_lst = nodes_list[time_index + 1:]
    info_string = ["Movie: ", "Rating out of 10: ", "Time: ", "Starring: ", "Rated: "]
    if sort_by == "Rating":
        for index in rating_lst:
            print("========================================================\n")
            print()
            info = genre[index]
            idx = 0
            for piece in info:
                print(info_string[idx] + str(piece))
                print()
                idx += 1
            print("========================================================\n")
    else:
        for index in time_lst:
            print("========================================================\n")
            info = genre[index]
            idx = 0
            for piece in info:
                print(info_string[idx] + str(piece))
                print()
                idx += 1
            print("========================================================\n")
                                                    
## Make title for fuction HANNAH'S FAVORITES MOVIE SUGGESTOR with a big star
print("                            *")
print("                           ***")
print("                          *****")
print("                         *******")
print("                        *********")
print("                       ***********")
print("                      *************")
print("     *************************************************")
print("        *******************************************")
print("          * HANNAH'S FAVORITES MOVIES SUGGESTOR * ")
print("           ************************************")
print("              *****************************")
print("                ************************")
print("                  ********************")
print("                ************************")
print("              ****************************")
print("             *************    *************")
print("            ************        ************")
print("           *********                *********")
print("          *******                      *******")
print("         *****                            *****")
print("")
print("")
print("")
print("Hello and Welcome to Hannah's Favorite Movie Suggestor")
## get input from user
    ## get input for movie genre first letter
        ## check if they meant that genre y/n
use_inputs = ["y", "n", "Y", "N"]
use = input("Would you like to use Hannah's Favorite Movie Suggestor? y/n: ")
while use not in use_inputs:
    print("Sorry, we didn't get that, please enter y/n")
    use = input("Would you like to use Hannah's Favorite Movie Suggestor? y/n: ")
## end program if input was no
if (use.upper() == "N"):
    print("We're sorry to hear that, feel free to come back at anytime!")
else:
    ## loop for program and while still wanting to use program again
    while (use.upper() == "Y"): 
        print("Awesome, we've got Romance, Action, Horror, Comedy, Scifi, and Drama")
        genre_letter_inputs = ["R", "A", "H", "C", "S", "D"]
        genre_letter = input("Please enter the first letter of the genre you want: ")
        correct = "n"
        genre = None
        genre_string = None
        if (genre_letter.upper() in genre_letter_inputs):
            genre_index = find_index(genre_letter.upper(), genre_start_letter)
            genre_string = genres_string[genre_index]
            genre = genres_list[genre_index]
        ## loop to get valid and correct genre input
        while (genre_letter.upper() not in genre_letter_inputs):
            genre_letter = str(input("Please enter the first letter of the genre you want: "))
            genre_index = find_index(genre_letter.upper(), genre_start_letter)
            genre_string = genres_string[genre_index]
            genre = genres_list[genre_index]
        print("Looks like the genre we have that starts with '{letter}' is {genre}".format(letter = genre_letter, genre = genre_string))
        correct = input("Is that correct? y/n: ")
        while (correct.upper() not in use_inputs):
            if (correct.upper() == "N"):
                genre_letter = str(input("Please enter the first letter of the genre you want: "))
                genre_index = find_index(genre_letter.upper(), genre_start_letter)
                genre_string = genres_string[genre_index]
                genre = genres_list[genre_index]
            print("Looks like the genre we have that starts with {letter} is {genre}".format(letter = genre_letter, genre = genre_string))
            correct = input("Is that correct? y/n: ")
        ## sort while loop
        sort_by_inputs= ["T", "R"]
        print("Sweet, would you like us to sort the {genre} movies by Time or Rating?".format(genre = genre_string))
        sort_by_letter = input("Enter the first letter of the sorting option T/R: ")
        sort_by = None
        if (sort_by_letter.upper() in sort_by_inputs):
            sort_by_letter = sort_by_letter.upper()
            sort_by_index = find_index(sort_by_letter, sort_by_inputs)
            sort_by = sort_by_options[sort_by_index]
        ## loop to get valid and correct sorting input
        while (sort_by_letter.upper() not in sort_by_inputs):
            sort_by_letter = input("Enter the first letter of the sorting option T/R: ")
            sort_by_letter = sort_by_letter.upper()
            sort_by_index = sort_by_inputs.index(sort_by_letter, 0, len(sort_by_inputs) - 1)
            sort_by = sort_by_options[sort_by_index]
        print("Looks like you'd like to sort {genre} by {sort_by}".format(genre = genre_string, sort_by = sort_by))
        correct = input("Is that correct? y/n: ")
        while (correct.upper() not in use_inputs):
            sort_by_letter = input("Enter the first letter of the sorting option T/R: ")
            sort_by_letter = sort_by_letter.upper()
            sort_by_index = sort_by_inputs.index(sort_by_letter, 0, len(sort_by_inputs) - 1)
            sort_by = sort_by_options[sort_by_index]
            print("Looks like you'd like to sort {genre} by {sort_by}".format(genre = genre_string, sort_by = sort_by))
            correct = input("Is that correct? y/n: ")
        print("Sweet! Here's a list of {genre} movies sorted by {sort_by}".format(genre = genre_string, sort_by = sort_by))
        lister(genre, sort_by)
        
        use = input("Would you like to use Hannah's Favorite Movie Suggestor angain? y/n: ")
        ## make loop to see if they want to use program again
        while use not in use_inputs:
            print("Sorry, we didn't get that, please enter y/n")
            use = input("Would you like to use Hannah's Favorite Movie Suggestor again? y/n: ")
                            
## thank user and end program
print("Thank you for using Hannah's Favorite Movies Suggestor! We hope you enjoy you're movie!")   
