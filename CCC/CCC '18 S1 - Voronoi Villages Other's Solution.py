# Number of villages
N = int(input())
# List of village positions
villages = list()
for i in range(N):
    villages.append(float(input()))

# List of distances between villages
distances = list()

# Sort the villages, from small to large, based on their positions
villages.sort()

# First and last villages distances are infinite
for i in range(1, N - 1):
    # Calculate neighborhood size for each village other than the first and last
    distances.append((villages[i + 1] - villages[i]) / 2 + (villages[i] - villages[i - 1]) / 2)

# Sort distances from small to large
distances.sort()

# Print Smallest
print(distances[0])
