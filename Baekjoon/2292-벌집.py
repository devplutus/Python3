n = int(input())
room = 1
room_max = 1
while True:
    if n <= room_max:
        print(room)
        break
    room_max += 6 * room
    room += 1