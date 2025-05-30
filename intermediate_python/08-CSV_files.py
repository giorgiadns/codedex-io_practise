# CSV FILES

# A CSV (comma-separated values) file is a common format
# for organizing data. Python provides a csv module
# to read and write data in this format.

# READING A CSV FILE
# The reader() mehod creates a CSV reader object 
# that displays our files content row by bow:
#  import csv
#  with open('example.csv','r') as file:
#   csv_reader = csv.reader(file)
#   for row in csv_reader:
#    print(row)

# WRITING TO CSV FILES
# The writer() method creates a CSV writer object, 
# and then use its methods to write rows to the file.
#-----------------------------------------------

# PRACTISE
# Create a program to read a CSV file and find the
# best-selling book of al time:
# 1. Download the bestseller.csv file
# 2. Open the Bestseller - Sheet1.csv file in read mode
# 3. Use the CSV reader to navigate through the data
#    and find the book with the highest sales
# 4. Create a new file called bestseller_info.csv 
# 5. In the new file, use writerow() to add new CSV data.
#-----------------------------------------------

import csv 

max_sales = 0
best_selling_book = None

#Open the csv file in 'read' mode
with open('Bestseller-Sheet1.csv','r',encoding="utf-8") as file:

    csv_reader = csv.reader(file)

    # Skip the header row
    file.readline()

    for row in csv_reader:

        # Print each row of the csv file
        print(row)

        # Extract sales (column 5)
        current_sales = float(row[4])

        if current_sales > max_sales:

            max_sales = current_sales
            best_selling_book = row

    # Write a CSV file with the best-selling book found 
    with open('bestseller_info.csv','w', newline='') as file:

        csv_writer = csv.writer(file)

        csv_writer.writerow(['Book', 'Author', 'Sales in Millions'])

        csv_writer.writerow([best_selling_book[0], best_selling_book[1], best_selling_book[4]])


print('Bestselling info written to', 'bestseller_info.csv',)
