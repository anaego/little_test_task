# The second part of task one - with **
from decimal import Decimal


def task_part_two(input_dict, output_m3):
    # Just bringing it to a format that's a little more readable & easier to process
    m3_cost_input_dict = {item['m3']: item['cost'] for item in input_dict}
    return {m3: Decimal(str(round(sum(m3_cost_input_dict.values())*m3/sum(output_m3), 2))) for m3 in output_m3}


if __name__ == "__main__":
    m3_in = [1.323, 0.561, 2.312, 1.567, 0.997]
    cost_in = [113.67, 213.5, 317.22, 522.3, 325.14]
    m3_out = [1.1, 0.313, 0.467, 1.2, 0.951, 1.113, 1.363]
    # Taking sum of the initial cost and evenly distributing it onto the output m3 values
    cost_out = {m3: Decimal(str(round(sum(cost_in)*m3/sum(m3_out), 2))) for m3 in m3_out}
    print(cost_out)
    task_2_input = [{'m3': 1.33, 'cost': 200.1}, {'m3': 2.33, 'cost': 300.1}]
    result = task_part_two(task_2_input, [1, 2.5])
    print(result)
    print(sum(result.values()))
