
def cartesian_product(A, B):
    return {(a, b) for a in A for b in B}

def cartesian_power(A, n):
    result = {()}  # Start with the Cartesian product of 0 sets, which is {()}
    for _ in range(n):
        result = {prev_tuple + (a,) for prev_tuple in result for a in A}
    return result

def union(A, B):
    result = set(A)  # Start with all elements in A
    for b in B:
        if b not in result:
            result.add(b)
    return result

def intersection(A, B):
    result = set()
    for a in A:
        if a in B:  # Only include elements present in both A and B
            result.add(a)
    return result

def difference(A, B):
    result = set()
    for a in A:
        if a not in B:  # Include elements in A but not in B
            result.add(a)
    return result

def symmetric_difference(A, B):
    result = set()
    for a in A:
        if a not in B:
            result.add(a)
    for b in B:
        if b not in A:
            result.add(b)
    return result

def power_set(s):
    s = list(s)
    result = [set()]
    for elem in s:
        result += [subset | {elem} for subset in result]
    return set(frozenset(subset) for subset in result)

def uniform_probability(omega, event):
    if not event.issubset(omega):
        raise ValueError("Event is not a subset of the sample space.")
    return len(event) / len(omega)

# Define omega, sigma algebra, and measure for a single dice
omega_die = set(range(1, 7))
P_die = lambda event: uniform_probability(omega_die, event)

# Define events
event_even = {2, 4, 6}
event_gt_3 = {4, 5, 6}
print("One die:")
print("P(Even):", P_die(frozenset(event_even)))           # Expected: 0.5
print("P(Greater than 3):", P_die(frozenset(event_gt_3)))  # Expected: 0.5
print("P(Even ∪ Greater than 3):", P_die(frozenset(union(event_even, event_gt_3))))  # Expected: 0.666...
print("P(Even ∩ Greater than 3):", P_die(frozenset(intersection(event_even, event_gt_3))))  # Expected: 0.333...

n_die = 2
omega_die =  set(cartesian_power(range(1, 7), n_die))
P_die = lambda event: uniform_probability(omega_die, event)

# Define independent events
event_sum_gt_7 = {outcome for outcome in omega_die if sum(outcome) > 7}
event_all_even = {outcome for outcome in omega_die if all(x % 2 == 0 for x in outcome)}
event_even_sum = {outcome for outcome in omega_die if sum(outcome) % 2 == 0}
event_at_least_one_six = {outcome for outcome in omega_die if 6 in outcome}
event_all_different_numbers = {outcome for outcome in omega_die if outcome[0] != outcome[1]}
event_sum_is_8 = {outcome for outcome in omega_die if sum(outcome) == 8}

# Combining events
event_even_sum_or_at_least_one_six = union(event_even_sum, event_at_least_one_six)
event_even_sum_and_at_least_one_six = intersection(event_even_sum, event_at_least_one_six)
event_complement_even_sum = difference(omega_die, event_even_sum)
event_even_sum_and_not_all_different = intersection(event_even_sum, difference(omega_die, event_all_different_numbers))
event_sum_8_or_at_least_one_six = union(event_sum_is_8, event_at_least_one_six)

print("Two Dice:")
print("P(Even Sum):", P_die(event_even_sum))
print("P(At Least One Six):", P_die(event_at_least_one_six))
print("P(All Different Numbers):", P_die(event_all_different_numbers))
print("P(Sum = 8):", P_die(event_sum_is_8))
print("P(Sum > 7):", P_die(event_sum_gt_7))
print("P(All Even):", P_die(event_all_even))
print("P(Even Sum or At Least One Six):", P_die(event_even_sum_or_at_least_one_six))
print("P(Even Sum and At Least One Six):", P_die(event_even_sum_and_at_least_one_six))
print("P(Not Even Sum):", P_die(event_complement_even_sum))
print("P(Even Sum and Not All Different):", P_die(event_even_sum_and_not_all_different))
print("P(Sum = 8 or At Least One Six):", P_die(event_sum_8_or_at_least_one_six))
