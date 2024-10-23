from unicodedata import numeric

import data

# Write your functions for each part in the space below.

# Part 1
def vowel_count(word:str) -> int:
    #input: input a string of choice.
    #output: an integer that is the number of vowels (uppercase or lowercase) in the inputted string
    #purpose: to count the amount of vowels in a word.
    list_word = list(word)
    num_vowels = 0
    vowels = "AEIOUaeiou"
    for x in list_word:
        if x in vowels:
            num_vowels = num_vowels + 1
    return num_vowels

# Part 2
def short_lists(input_list: list[list]) -> list:
    #input: an embedded list of integers.
    #output: the lists inside of the list that are of length 2.
    #purpose: to filter out and only keep the embedded lists that have length 2.
    new_list = []
    for i in range(len(input_list)):
        if len(input_list[i]) == 2:
            new_list.append(input_list[i])
    return new_list


# Part 3
def ascending_pairs(given: list[list]) -> list[list]:
    #input: an embedded list of integers.
    #output: the original list of integers, but for every element that has list of length two, they are in ascending order.
    #purpose: to return the same list, but for every element that has length two, return the ascending version of this element.
    new_list = []
    for i in range(len(given)):
        if len(given[i]) != 2:
            new_list.append(given[i])
        else:
            if given[i][0]>given[i][1]:
                new_list.append([given[i][1], given[i][0]])
            else:
                new_list.append(given[i])
    return new_list


# Part 4
def add_prices(given1: data.Price, given2: data.Price) -> data.Price:
    #input: two parameters of our class Price in the data file
    #output: the sum of input prices, with cents not going over 99
    #purpose: to output the total sum in a convention that is practical
    total_dollars = given1.dollars + given2.dollars
    total_cents = given1.cents + given2.cents
    if total_cents//100 >= 1:
        total_newcents  = total_cents -(total_cents//100)*100
        total_dollars  = total_dollars + total_cents//100
    else:
        total_newcents = total_cents
    return data.Price(total_dollars, total_newcents)

# Part 5
def rectangle_area(input: data.Rectangle) -> float:
    #input: one parameter of our class Rectangle found in data file
    #output: a float value that is the area of the rectangle
    #purpose: to return the area of a given rectangle
    y_distance = input.top_left.y-input.bottom_right.y
    x_distance = input.bottom_right.x-input.top_left.x
    area = y_distance*x_distance
    return area

# Part 6
def books_by_author(author: str, books: list[data.Book]) -> list[data.Book]:
    #input: one input is the author as a string, then a list of our class Book (class book has list of authors associated with a title)
    #output: return the list of books that are written by a certain author
    #purpose: to find a list of books by an author
    authors_books = []
    for book in books:
        for i in book.authors:
            if i == author:
                authors_books.append(book)
    return authors_books

# Part 7
def circle_bound(input: data.Rectangle) -> data.Circle:
    #input: a rectangle from our class Rectangle
    #output: a circle from our class Circle that is a "bounding circle" for the inputted rectangle
    #purpose: to convert a rectangle to a circle that bounds said rectangle
    center_y = .5*(input.top_left.y-input.bottom_right.y)
    center_x = .5*(input.bottom_right.x-input.top_left.x)
    center_point_orgin = data.Point(center_x, center_y)
    center_point_rectangle = data.Point(input.top_left.x+center_x, input.top_left.y-center_y)
    if center_x<center_y:
        radius = center_x
        center = center_point_rectangle
        return data.Circle(center, radius)
    else:
        radius = center_y
        center = center_point_rectangle
        return data.Circle(center, radius)

# Part 8
def below_pay_average(employees: list[data.Employee]) -> list[str]:
    #input: a list that's elements is from our class Employee
    #output: the names of employees that are paid less than the average pay of employees
    #purpose: to determine employees that are paid less than the average emplopyee in the inputted list
    net_pay = 0
    for i in employees:
        net_pay = net_pay + i.pay_rate
    pay_average = net_pay/len(employees)
    for i in employees:
        below_pay = [i.name for i in employees if i.pay_rate <pay_average]
    return below_pay


