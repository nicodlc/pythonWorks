import xlsxwriter
# Python program I made that manages a T-shirt inventory

# Define the four types of shirts
shirt_types = ["type1", "type2", "type3", "type4"]

# Define the six sizes of shirts
shirt_sizes = ["S", "M", "L", "XL", "2XL", "3XL"]

# Create a workbook
workbook = xlsxwriter.Workbook("main-shirt_inventory.xlsx")

# Create a worksheet
worksheet = workbook.add_worksheet()

# Write the header row
worksheet.write_row(0, 0, ["Type"])
worksheet.write_row(0, 1, ["S"])
worksheet.write_row(0, 2, ["M"])
worksheet.write_row(0, 3, ["L"])
worksheet.write_row(0, 4, ["XL"])
worksheet.write_row(0, 5, ["2XL"])
worksheet.write_row(0, 6, ["3XL"])

# Iterate through the shirt types
i = 0
indexRow = 1
indexCol = 0
for shirt_type in shirt_types:
    print("Entering quantity for: ", shirt_types[i])
    # Get the user input for the number of shirts per size
    quantity = []
    i = i + 1
    for shirt_size in shirt_sizes:
        quantity.append(int(input("Enter the quantity of {} shirts: ".format(shirt_size))))

    # Write the data to the worksheet
    worksheet.write_row(indexRow, indexCol, [shirt_type] + quantity)
    indexRow = indexRow + 1

# Calculate the total number of shirts
total_shirts = sum(quantity)

# Write the total number of shirts to the worksheet
worksheet.write_row(shirt_types.__len__() + 1, shirt_types.__len__() + 1, ["Total", total_shirts])

# Save the workbook
workbook.close()
