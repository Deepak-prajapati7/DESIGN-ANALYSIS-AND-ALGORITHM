def knapsack(weights, values, capacity):
    n = len(weights)

    
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Build DP table
    for i in range(1, n + 1):
        for w in range(capacity + 1):

            if weights[i - 1] <= w:
                
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
               
                dp[i][w] = dp[i - 1][w]

    
    selected_items = []
    w = capacity

    for i in range(n, 0, -1):

        # If value changed, item i was selected
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append({
                "item": i,
                "weight": weights[i - 1],
                "value": values[i - 1]
            })

            w -= weights[i - 1]

    # Reverse because we found items from last to first
    selected_items.reverse()

    return dp[n][capacity], selected_items


# Example
weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
capacity = 7

max_value, selected_items = knapsack(weights, values, capacity)

print("Maximum Value:", max_value)
print("Selected Items:")

total_weight = 0
total_value = 0

for item in selected_items:
    print(
        f"Item {item['item']}: "
        f"Weight = {item['weight']}, "
        f"Value = {item['value']}"
    )

    total_weight += item["weight"]
    total_value += item["value"]

print("Total Weight:", total_weight)
print("Total Value:", total_value)