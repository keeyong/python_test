import sys

def compute_average(numbers):
    if not numbers:
        return None
    total = 0
    for number in numbers:
        total += number
    return total/len(numbers)

def main():
    list = []
    for argv in sys.argv[1:]:
        list.append(int(argv))
    print("Average: " +   
         str(compute_average(list)))

if __name__ == "__main__":
    main()
