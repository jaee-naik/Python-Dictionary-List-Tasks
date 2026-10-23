
import statistics


def calculate_average(data):
    return sum(data) / len(data)


def find_maximum(data):
    return max(data)


def find_minimum(data):
    return min(data)


def sort_data(data):
    return sorted(data, reverse=True)


def calculate_statistics(data):
    print("Mean:", statistics.mean(data))
    print("Median:", statistics.median(data))

    if len(data) > 1:
        print("Standard Deviation:", statistics.stdev(data))
    else:
        print("Standard Deviation: Not enough data")
