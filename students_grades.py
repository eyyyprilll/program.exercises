def main():
    # Read student names and GWAs from file
    with open("students.txt", "r") as file:
        student_data = [line.strip().split(",") for line in file.readlines()]

    # Extract names and GWAs into separate lists
    names = []
    gwas = []
    for data in student_data:
        if len(data) == 2:  # Check if the line has two elements (name and GWA)
            names.append(data[0])
            gwas.append(float(data[1]))
        else:
            print(f"Illegal format in line: {data}")
        # Check if any data was extracted
    if not names or not gwas:
        print("No valid data found in the file.")
        return

    # Find the index of the student with the highest GWA
    highest_gwa_index = gwas.index(max(gwas))

    # Output the name and GWA of the student with the highest GWA
    print(f"Student with the highest GWA: {names[highest_gwa_index]} - GWA: {gwas[highest_gwa_index]}")

if __name__ == "__main__":
    main()

