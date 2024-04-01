# team = input().strip()
# Players_positions = list(team)
# print(Players_positions)


def is_dangerous(s):
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
            if count >= 7:
                return "YES"
        else:
            count = 1
    return "NO"

# Read input
situation = input().strip()

# Check if the situation is dangerous
print(is_dangerous(situation))
