from typing import List

def report_repair(expense_report: List[int], target: int) -> List[int]:
    num_dict = {}
    result = []
    for i in range(len(expense_report)):
        if target - expense_report[i] in num_dict:
            result.append(i)
            result.append(num_dict[target - expense_report[i]])
        else:
            num_dict[expense_report[i]] = i

    return [expense_report[result[0]], expense_report[result[1]], expense_report[result[0]]*expense_report[result[1]]]

def report_repair_part_2(expense_report: List[int], target: int) -> List[int] :
    for i in range(len(expense_report)):
        s = set()
        curr_sum = target - expense_report[i]
        for j in range(i + 1, len(expense_report)):
            if (curr_sum - expense_report[j]) in s:
                return [expense_report[i], expense_report[j], curr_sum - expense_report[j], expense_report[i]*expense_report[j]*(curr_sum - expense_report[j])]
            s.add(expense_report[j])