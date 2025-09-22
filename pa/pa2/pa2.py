# PA2 Skeleton Code
# DSA2, fall 2025

# This code will read in the input, and put the values into data structures.
# This skeleton code only reads in the input.

devices = {}
[num_devices,num_usages] = [int(x) for x in input().split(" ")]
for _ in range(num_devices):
	devices[input().strip()] = []
for _ in range(num_usages):
	[device_name,start_time,finish_time,usage_load] = input().split(" ")
	devices[device_name].append( (int(start_time),int(finish_time),int(usage_load)) )
print(devices) # REMOVE THIS LINE when submitting, as it will cause output checking problems otherwise
