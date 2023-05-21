if __name__ == '__main__':
    # Read in the number of students
    n = int(input())
    
    # Initialize an empty list to store the student records
    records = []
    
    # Read in the student records
    for i in range(n):
        name = input()
        score = float(input())
        records.append([name, score])
    
    # Find the second lowest score
    scores = set([record[1] for record in records])
    second_lowest_score = sorted(scores)[1]
    
    # Collect the names of students with the second lowest score
    names = [record[0] for record in records if record[1] == second_lowest_score]
    
    # Sort the names alphabetically
    names.sort()
    
    # Print each name on a new line
    for name in names:
        print(name)
