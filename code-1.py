#This Program is to develop a software to analyse performance of vcrs based systems

print("***********************************************************")
print("This program is developed by ME-Grp5 -> Devesh,Sanjeev,Kirti & Shashank" )
print("Guide- Prof SP Kutar")
print("***********************************************************")

#for chosing refrigerant
# Ask the user to choose a refrigerant
print("Choose a refrigerant:")
print("1. R600a")
print("2. R290")
choice = input("Enter the number corresponding to your choice (1 or 2): ")
# #-----------------------------------------------------------------------------------
# Check the user's choice and provide information about the selected refrigerant
if choice == "1":
    refrigerant = "R600a"
    print(f"You selected {refrigerant}.")
    # Provide information about R600a
    print("R600a is an isobutane refrigerant commonly used in household refrigeration.")
elif choice == "2":
    refrigerant = "R290"
    print(f"You selected {refrigerant}.")
    # Provide information about R290
    
else:
    print("Invalid choice. Please select either 1 or 2.")

#-----------------------------------------------------------------------


# For getting Inputs (T1,T2,T3,T4,T5,Ps,Pd,)
print("All temp should be in Celsius and Pressure in bar")
T1 = float(input("Enter the value for Condenser temperature T1 (inlet): "))
T2 = float(input("Enter the value for Condenser temperature T2 (outlet): "))
T3 = float(input("Enter the value for Evaporator temperature T3 (inlet): "))
T4 = float(input("Enter the value for Evaporator temperature T4 (outlet): "))
P1 = float(input("Enter the value for Suction pressure Ps: "))
P2 = float(input("Enter the value for Discharge pressure Pd: "))
T5 = float(input("Enter the value for Inside temperature of cabin T5: "))

# Enthalpies at different temperatures(using f so that compiler can know T in curly braces is variable)
h1 = float(input(f"Enter the value of Enthalpy (h1) at {T1}°C: "))
h2 = float(input(f"Enter the value of Enthalpy (h2) at {T2}°C: "))
h3 = float(input(f"Enter the value of Enthalpy (h3) at {T3}°C: "))
h4 = float(input(f"Enter the value of Enthalpy (h4) at {T4}°C: "))

#compressor work
Q=(h3-h1)
print("Refrigeration effect is (in kw) : ",Q)

#Refrigeration effect calculation
W=(h4-h3)
print("Compressor work is (in kw) : ",W)
#cop calculation
cop=Q/W
print("COP of system is : ",cop)
print("Ideal COP : ", (T3+273.15)/(T1-T3))
                                    












