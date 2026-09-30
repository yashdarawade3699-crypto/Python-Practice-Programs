try:
    with open ('student.csv', 'r') as file:
        lines=file.readlines()

    count=len(lines)
    print(count)
