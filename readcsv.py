import csv

filename = '/home/weichu/Desktop/logfile4.csv'
Delay = []
Throughput = []
Droprate = []

with open(filename) as f:
	reader = csv.reader(f)
	iterreader = iter(reader)
	next(iterreader)
	for i in iterreader:
		Delay.append(i[0])
		Throughput.append(i[1])
		Droprate.append(i[2])
print(Delay)
print(Throughput)
print(Droprate)


		
