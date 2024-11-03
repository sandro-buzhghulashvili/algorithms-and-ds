def hanoi(n, start, end):
    if n == 1: 
        print(start, ">", end)
        return
    free_rod = 6 - (start + end) 
    hanoi(n - 1, start, free_rod ) 
    print(start, ">", end)
    hanoi(n - 1, free_rod, end) 

hanoi(3,1,3)      


# visualization of recursion :

# hanoi(3, 1, 3)
# │
# ├── hanoi(2, 1, 2)        # Move 2 disks from first rod to second rod 
# │    │
# │    ├── hanoi(1, 1, 3)   # Move 1 disk from first to third
# │    │       └── prints : 1 > 3
# │    ├── prints : 1 > 2
# │    └── towerOfHanoi(1, 3, 2)   # Move 1 disk from third to second
# │            └── prints : 3 > 2
# │
# ├── Transfer disk 3 from first to second
# │
# └── hanoi(2, 2, 3)        # Move 2 disks from second to third 
#      │
#      ├── hanoi(1, 2, 1)   # Move 1 disk from second to first
#      │       └── prints : 2 > 1
#      ├── prints : 2 > 3
#      └── hanoi(1, 1, 3)   # Move 1 disk from first to third
#              └── prints : 1 > 3