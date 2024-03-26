# Function that calculates the delta time in hh:mm between two timestamps in given in milliseconds

import datetime


def delta_time(timestamp1, timestamp2):
    # Convert the timestamps to datetime objects
    time1 = datetime.datetime.fromtimestamp(timestamp1 / 1000)
    time2 = datetime.datetime.fromtimestamp(timestamp2 / 1000)

    # Calculate the difference in time
    delta = time2 - time1

    # Convert the difference to hours and minutes
    hours, remainder = divmod(delta.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    # Return the difference in hh:mm format
    return "{:02d}:{:02d}".format(hours, minutes)


print(delta_time(1702407540, 1702112235))  # 00:01

