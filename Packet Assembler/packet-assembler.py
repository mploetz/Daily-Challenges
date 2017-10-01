import fileinput

packets = {}

# change to test dif inputs
testinput = "input.txt"

#import file data
# X = message ID Y = packet ID Z = number of packets
for line in fileinput.input(testinput):
    X, Y, Z = line.split(maxsplit=3)[:3]
    if X not in packets:
        packets[X] = [int(Z)]
    packets[X].append([int(Y), line.strip()])
    if len(packets[X]) - 1 == packets[X][0]:
        for packet in sorted(packets[X][1:]):
            print(packet[1])