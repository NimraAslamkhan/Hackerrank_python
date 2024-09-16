# Enter your code here. Read input from STDIN. Print output to STDOUT

k = int(input())


room_numbers = list(map(int, input().split()))


unique_rooms = set(room_numbers)


captain_room = (sum(unique_rooms) * k - sum(room_numbers)) // (k - 1)


print(captain_room)
