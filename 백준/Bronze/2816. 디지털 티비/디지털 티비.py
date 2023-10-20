n = int(input())
channels = []

kbs1_idx = 0
kbs2_idx = 0
result = ""

for _ in range(n):
    channel = input()
    channels.append(channel)
    if channel == "KBS1":
        kbs1_idx = len(channels) - 1
    elif channel == "KBS2":
        kbs2_idx = len(channels) - 1

if kbs1_idx < kbs2_idx:
    result += "1" * kbs1_idx + "4" * kbs1_idx
    result += "1" * kbs2_idx + "4" * (kbs2_idx - 1)
elif kbs1_idx > kbs2_idx:
    result += "1" * kbs1_idx + "4" * kbs1_idx
    result += "1" * (kbs2_idx + 1) + "4" * kbs2_idx

print(result)
