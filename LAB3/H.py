def build_pre_order(in_order, post_order):
    idx_map = {val: idx for idx, val in enumerate(in_order)}
    post_index = [len(post_order) - 1]  

    def helper(in_start, in_end):
        if in_start > in_end:
            return []

        root_val = post_order[post_index[0]]
        post_index[0] -= 1

        in_index = idx_map[root_val]

        right_subtree = helper(in_index + 1, in_end)
        left_subtree = helper(in_start, in_index - 1)

        return [root_val] + left_subtree + right_subtree

    return helper(0, len(in_order) - 1)

# Input reading
N = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))

pre_order = build_pre_order(in_order, post_order)
print(' '.join(map(str, pre_order)))
