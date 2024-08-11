import csv
import copy

# Define the template for vehicle
myVehicle = {
    "vin": "<empty>",
    "make": "<empty>",
    "model": "<empty>",
    "year": 0,
    "range": 0,
    "topSpeed": 0,
    "zeroSixty": 0.0,
    "mileage": 0
}

# Print the default values of the vehicle template
for key, value in myVehicle.items():
    print("{} : {}".format(key, value))

# Initialize an empty inventory list
myInventoryList = []

# Open and read the CSV file
with open('car_fleet.csv', mode='r') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    lineCount = 0
    for row in csvReader:
        if lineCount == 0:
            # Print the header
            print(f'Column names are: {", ".join(row)}')
            lineCount += 1
        else:
            # Print the current row of data
            print(f'vin: {row[0]}, make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')

            # Deep copy the vehicle template
            currentVehicle = copy.deepcopy(myVehicle)
            
            # Populate the current vehicle with data from the CSV row
            currentVehicle["vin"] = row[0]
            currentVehicle["make"] = row[1]
            currentVehicle["model"] = row[2]
            currentVehicle["year"] = int(row[3]) if row[3].isdigit() else 0
            currentVehicle["range"] = int(row[4]) if row[4].isdigit() else 0
            currentVehicle["topSpeed"] = int(row[5]) if row[5].isdigit() else 0
            currentVehicle["zeroSixty"] = float(row[6]) if row[6].replace('.', '', 1).isdigit() else 0.0
            currentVehicle["mileage"] = int(row[7]) if row[7].isdigit() else 0

            # Append the populated vehicle to the inventory list
            myInventoryList.append(currentVehicle)
            lineCount += 1

    # Print the number of processed lines
    print(f'Processed {lineCount - 1} lines.')

# Print the contents of the inventory list
for myCarProperties in myInventoryList:
    for key, value in myCarProperties.items():
        print("{} : {}".format(key, value))
    print("-----")
