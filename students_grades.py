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
