largest_so_far = None
smallest_so_far = None

while True:
    i = input('Please enter an integer.')

    if i == 'done':
        print('Maximum is',largest_so_far)
        print('Minimum is',smallest_so_far)
        break

    else:
        try:
            i_converted = int(i)
        except:
            print('Invalid input')
            continue

        if largest_so_far == None:
            largest_so_far = i_converted

        elif i_converted > largest_so_far:
            largest_so_far = i_converted

        if smallest_so_far == None:
            smallest_so_far = i_converted

        elif i_converted < smallest_so_far:
            smallest_so_far = i_converted
