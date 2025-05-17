# Problem 205


s = "foo"

t = "bar"


# Solution 1

# char_map_s = {}
# char_map_t = {}

# next_counter_s = 1
# next_counter_t = 1

# pattern_s = []

# pattern_t = []

# for char in s:
#     if char not in char_map_s:
#         char_map_s[char] = next_counter_s
#         next_counter_s += 1
#         pattern_s.append(char_map_s[char])
#     else:
#         pattern_s.append(char_map_s[char])

# for char in t:
#     if char not in char_map_t:
#         char_map_t[char] = next_counter_t
#         next_counter_t += 1
#         pattern_t.append(char_map_t[char])
#     else:
#         pattern_t.append(char_map_t[char])


# print(pattern_s == pattern_t)
        
# Solution 2

char_map_s = {}
char_map_t = {}

next_counter_s = 1
next_counter_t = 1

for i in range(len(s)):
    if s[i] not in char_map_s:
        char_map_s[s[i]] = next_counter_s
        next_counter_s += 1
    
    if t[i] not in char_map_t:
        char_map_t[t[i]] = next_counter_t
        next_counter_t += 1

    if char_map_t[t[i]] != char_map_s[s[i]]:
        print(False)
        break




print(True)