"""Restaurant rating lister."""


# put your code here
def get_restaurant_ratings():
    """" Returns restaurant name and rating
    
    """

    file = open("scores.txt")
    restaurant_ratings = {}
    
    for line in file:
        line = line.rstrip()
        words = line.split(":")

        for word in words:
            restaurant_name = words[0]
            rating = words[1]

            restaurant_ratings[restaurant_name] = rating
        # rating = words[1]

        #print(sorted(restaurant_name))
    #print(restaurant_ratings)

        for restaurant_name, rating in restaurant_ratings.items():
            print(f'{restaurant_name} is rated at {rating}.')
            


get_restaurant_ratings()
#["Florean Fortescue's Ice Cream Parlour", '4']