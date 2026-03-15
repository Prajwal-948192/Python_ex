"""In a month of 30 days my schedule is as follows

            booked = [ 1, 3, 9, 12, 13, 18, 26, 27, 28, 29 ]

            travel = [ 4, 5, 15, 16, 21, 22 ]

            Write a function that takes these two lists as parameters and

            returns a list of days when I am free to study
            """


def free_days(booked, travel):
    
    total_busy = booked + travel
    free_days = []
    total_days = list(range(1, 31))

    for day in total_days:
        if day not in total_busy:
            free_days.append(day)

    return free_days

    
    

    

booked = [ 1, 3, 9, 12, 13, 18, 26, 27, 28, 29 ]

travel = [ 4, 5, 15, 16, 21, 22 ]

print(free_days(booked, travel))



#total_busy = booked + travel

#total_days = list(range(1, 31))

##free_days = []

