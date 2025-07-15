def build_post_order(in_order, pre_order):
    idx_map = {val: idx for idx, val in enumerate(in_order)}
    pre_index = [0] 

    def helper(in_start, in_end):
        if in_start > in_end:
            return []

        root_val = pre_order[pre_index[0]]
        pre_index[0] += 1

        in_index = idx_map[root_val]

        left_subtree = helper(in_start, in_index - 1)
        right_subtree = helper(in_index + 1, in_end)

        return left_subtree + right_subtree + [root_val]

    return helper(0, len(in_order) - 1)

# Input reading
N = int(input())
in_order = list(map(int, input().split()))
pre_order = list(map(int, input().split()))

post_order = build_post_order(in_order, pre_order)
print(' '.join(map(str, post_order)))
