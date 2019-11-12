from decimal import Decimal
import pandas as pd


# Because division doesn't always divide without loss, especially when dealing with rounded values
def reassign_sums_difference(output_costs, input_sum, output_sum):
    sum_difference = input_sum - output_sum
    if sum_difference == 0:
        return output_costs
    cent = Decimal(str(0.01)) if sum_difference > 0 else Decimal(str(-0.01))
    difference_in_cents = abs(int(sum_difference / cent))
    iter_difference = iter([cent] * difference_in_cents)
    # Just randomly reassign it to items. It can be redone to add difference to the biggest or the smallest costs etc
    output_costs = output_costs.apply(lambda cost: cost + next(iter_difference, 0))
    return output_costs


# The second part of task one - with **
def task_part_two(input_dict, output_m3):
    input_df = pd.DataFrame(input_dict)
    output_df = pd.DataFrame().assign(m3=output_m3)
    output_df['m3'] = output_df['m3'].apply(lambda x: Decimal(str(round(x, 3))))
    input_df['m3'] = input_df['m3'].apply(lambda x: Decimal(str(round(x, 3))))
    input_df['cost'] = input_df['cost'].apply(lambda x: Decimal(str(round(x, 2))))
    output_df['cost'] = output_df.apply(lambda row:
                                        Decimal(str(round(input_df['cost'].sum()*row['m3']/output_df['m3'].sum(), 2))),
                                        axis=1)
    output_df['cost'] = reassign_sums_difference(output_df['cost'], input_df['cost'].sum(), output_df['cost'].sum())
    return output_df.to_dict('records')


if __name__ == "__main__":
    input_structure = [{'m3': 31.302, 'cost': 1000.01}]
    result = task_part_two(input_structure, [3.478 for _ in range(6)])
    print(result)
    print(sum([a['cost'] for a in result]))