'''Car'''
#List of cars and number of seats
car = ["Suzuki Van", "Toyota Corolla", "Honda CRV", "Suzuki Swift", "Mitsubishi Airtrek", "Nissan DC Ute", "Toyota Previe", "Toyota Hi Ace", "Toyota Hi Ace"]
seats = [2,4,4,4,4,4,7,12,12]
#lp stand for list position
lp = len(car)
for i in range(lp):
    print(f"{lp} - {car[i]} - {seats[i]} seats")
takeout = input("What car number would you like to take out?")



