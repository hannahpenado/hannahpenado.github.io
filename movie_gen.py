## import functions
from random import randrange, shuffle

## create Node class
class Node:
    def __init__(self, value, next_node = None):
        self.value = value
        self.next_node = next_node
    
    def set_next_node(next_node):
        self.next_node = next_node
        
    def get_next_node(self):
        return self.next_node
    
    def get_value(self):
        return self.value

## create Stack class
class Stack:
    def __init__(self, limit = 6):
        self.limit = limit
        self.size = 0
        self.top_item = None
     
    def push(self, value):
        if self.has_room():
            movie = Node(value)
            movie.set_next_node(self.top_item)
            self.top_item = movie
            self.size += 1
        else:
            return "Limit reached, cannot add"
    
    def pop(self):
        if self.size > 0:
            item_to_remove = self.top_item 
            self.top_item = item_to_remove.get_next_node()
            self.size -= 1
            return item_to_remove.get_value()
        else:
            return None
      
    def has_space(self):
        if self.size < self.limit:
            return True
        else:
            return False
        
    def is_empty(self):
        return self.size == 0
        

   
## create empty list genres, and rating global constants
genres = []
g = ["G", 1]
pg = ["PG", 2]
pg13 = ["PG-13", 3]
r = ["R", 4]

## create list of dictionary genre = {movies{rating / 10, stars (2), length in MIN, rated},...}
    ## Romance = {}
        # Can't Buy Me Love, Love Actually, The Notebook, The Titanic
Romance = {"Can't Buy Me Love": [6.8, 94, "Patrick Dempsey", "Amanda Peterson", pg13],  "Love Actually": [7.6, 135, "Hugh Grant", "Keira Knightly", r], "The Notebook": [7.8, 121, "Ryan Gosling", "Rachel McAdams", pg13], "Titanic": [7.9, 196, "Kate Winslet", "Leonardo DiCaprio", pg13]}
    
    ## Action = {}
        ## Die Hard, Maverick, Tron: Legacy, Tomb Raider
Action = {"Die Hard": [8.2, 132, "Bruce Willis", "Alan Rickman", r], "Maverick": [8.3, 131, "Tom Cruise", "Miles Teller", pg13], "Tron: Legacy": [6.8, 125, "Garrett Hedlund", "Olivia Wilde", pg], "Lara Corft: Tomb Raider":[5.7, 100, "Angelina Jolie", "Daniel Craig", pg13]}
    ## Horror = {} 
        ## Scream, Halloween, Friday the 13th, Scream 2
Horror = {"Scream": [7.4, 111, "Neve Campbell", "Courtney Cox", r], "Halloween": [7.7, 91, "Jamie Lee Curtis", "Nancy Kyes", r], "Friday The 13th": [6.4, 95, "Betsy Palmer", "Kevin Bacon", r], "Scream 2": [6.3, 120, "Neve Campbell", "David Arquette", r]}
    
    ## Comedy = {}
        ## Spy, Teladega Nights, 21 Jump Street, The Spy Who dumped me
Comedy = {"Spy": [7.0, 130, "Mellissa McCarthy", "Jason Statham", r], "Talladega Nights: The Ballad of Ricky Bobby": [6.6, 108, "Will Farrell", "John C. Reilley", pg13], "21 Jump Street":[7.2, 109, "Jonah Hill", "Channing Tatum", r], "The Spy Who Dumped Me": [6.0, 118, "Mila Kunis", "Kate McKinnon", r]}
    
    ## Scifi = {}
        ## Star Wars, Avatar, Interstellar, Inception
Scifi = {"Star Wars: Episode IV – A New Hope": [8.6, 121, "Harrison Ford", "Carrie Fisher", pg], "Avatar": [7.9, 161, "Zoe Saldana", "Sam Worthington", pg13], "Interstellar": [8.6, 169, "Matthew McConaughey", "Anne Hathaway", pg13], "Inception": [8.8, 148, "Tom Hardy", "Leonardo DiCaprio", pg13]}
    
    ## Drama = {}
        ## Don't Worry Darling, Hidden Figures, 127 Hours, Luckiest Girl Alive
Drama = {"Don't Worry Darling": [6.2, 123, "Florence Pugh", "Harry Styles", r], "Hidden Figures": [7.8, 127, "Taraji P. Henson", "Octavia Spencer", pg], "127 Hours": [7.6, 94, "James Franco", "Kate Mara", r], "Luckiest Girl Alive": [6.4, 115, "Mila Kunis", "Chiara Aurelia", r]}
    
    ## append all into genre list
genres.append(Romance, Action, Horror, Comedy, Scifi, Drama)

## create quicksort function to sort quicker and can sort rating or movie length
def quicksort(lst, start_index, end_index):
    if start_index >= end_index:
        return
    else:
    # find random element in list to be pivot point
    pivot_index = rand(range(start, end + 1)
    pivot_val = lst[pivot_index]
    # swap random element with end value and make two new lists
    lst[end_index], lst[pivot_index] = lst[pivot_index, lst[end_index]
    ## looking at values in front of pivot now end and start element, and will move
    ## to the right when a value is less than the pivot by increasing the index and
    ## swapping the value with the start value then after all possible swaps switching 
    ## the pivot element with the pointer element
    less_than_pointer = start_index
    for index in range(start_index, end_index):
        # find elements out of order
        if lst[index] < pivot_element:
            lst[index], lst[less_than_pointer] = lst[less_than_pointer}, lst[index]
            less_than_pointer += 0
    ## now swapping the pointer element and where the original start element is to be
    ## able to create two new sublists and call quicksort recurrsively unil the list is 
    ## sorted
    lst[end_index], lst[less_than_pointer] = lst[less_than_pointer], lst[end_index]                                                  
    quicksort(lst, start_index, less_than_pointer - 1)
    quicksort(lst, less_than_pointer + 1, end_index)

## start backend knowledge of genres and movies through dictionary
## and using a stack of the movies for each genre to later sort through and
## hash map for movie values 
    ## want to map out the values for selected movies
        ## need to map out the rating values of the movies
        
    ## romance_stack 
        ## create stacks by lowest rated first to highest rated with quicksort function

        
        ## sort_genre(genre, movie_list) 
            ## list of genre movies movie_list = [rating[movie]]
    
    ## action_stack
        ## create stacks by lowest rated first to highest rated with quick sort function

        
        ## sort_genre(genre, movie_list) 
            ## list of genre movies movie_list = [rating[movie]]
    
    ## horror_stack
        ## create stacks by lowest rated first to highest rated with quick sort function

         
        ## sort_genre(genre, movie_list) 
            ## list of genre movies movie_list = [rating[movie]]
       
    ## comedy_stack
        ## create stacks by lowest rated first to highest rated with heap sort function
        ## and hashmaps
        
        ## sort_genre(genre, movie_list) 
            ## list of genre movies movie_list = [rating[movie]]
       
    ## scifi_stack
        ## create stacks by lowest rated first to highest rated with heap sort function
        ## and hashmaps
        
        ## sort_genre(genre, movie_list) 
            
            ## list of genre movies movie_list = [rating[movie]]
    
    ## drama_stack
        ## create stacks by lowest rated first to highest rated with heap sort function
        ## and hashmaps
        
        ## sort_genre(genre, movie_list) 
            ## list of genre movies movie_list = [rating[movie]]
    
    ## create a stack function that can go through and pop movie values
    ## and return the movie info

## Make title for fuction HANNAH'S FAVORITES MOVIE SUGGESTOR with a big star

## get input from user
    ## get input for movie genre first letter
        ## check if they meant that genre y/n

    ## want to create a stack or a queue for the movie genres and scope 
        ## then pop the top values for the movies

    ## ask user if they want to look at another genre y/n
        ## yes = loop through again for stacks and hasing out
            ## count user genres looked at, if more than 6 genres seen ask 
            ## and tell this
                ## that's all the genres we have and ask if they'd like to 
                ## see a genre again
 
        ## no = end program
    
## thank user and end program
