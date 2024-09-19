#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return

    total_weight = sum(weight for _, weight in my_list)
    weighted_sum = sum(score * weight for score, weight in my_list)

    return weighted_sum / total_weight if total_weight else 0
