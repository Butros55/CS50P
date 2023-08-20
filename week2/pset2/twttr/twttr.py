def main():
    user = input("Input: ")
    rmvowels(user)


def rmvowels(user):

    vowels = ["a","e","i","o","u","A","E","I","O","U"]
    print("Output: ", end="")
    for i in user:
        for j in vowels:
            if j == i:
                test = ""
                break
            else:
                test = i
        print(test, end="")

    print()

main()