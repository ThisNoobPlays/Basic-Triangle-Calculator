# By Minedani129
# Type in 2 or 3 side lengths and it will output the perimeter
import math

#Welcome message
print("Basic triangle calculator by Minedani129")
print("Global options currently available: --ROUND {int}")

#Get global options from input
globalOptions = input("Enter any global options. Else just leave empty and press enter: ")
OptionDict = {}
for i in globalOptions.split(","):
  if len(globalOptions) > 0:
    OptionDict[i.split()[0]] = i.split()[1]

#Globals
ROUND = 13 if not "--ROUND" in OptionDict.keys() else int(OptionDict["--ROUND"])



print("Press enter without typing anything if you do not know the side length")
while True:
  # Get user input
  inhypotenuse = input("Hypotenuse length: ")
  inleg1 = input("Leg 1 length: ")
  inleg2 = input("Leg 2 length: ")
  hypotenuse, leg1, leg2 = "", "", ""

  #Discard non-numeric characters
  for i in inhypotenuse:
    if i in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."]:
      hypotenuse += i

  for i in inleg1:
    if i in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."]:
      leg1 += i

  for i in inleg2:
    if i in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."]:
      leg2 += i

  #Prevent erroring due to input not being convertible to float
  try:
    float(leg1) if leg1 != "" else 0
    float(leg2) if leg2 != "" else 0
    float(hypotenuse) if hypotenuse != "" else 0
  except:
    print("Error trying to convert numbers. Try again and check your input.")
    continue

  #Convert to float
  hypotenuse = float(hypotenuse) if hypotenuse != "" else 0
  leg1 = float(leg1) if leg1 != "" else 0
  leg2 = float(leg2) if leg2 != "" else 0

  #Negative side length check
  if hypotenuse < 0 or leg1 < 0 or leg2 < 0:
    print("Error: At least one side length is negative")

  #Check for what to calculate
  if not hypotenuse and leg1 and leg2:
    print("Calculating hypotenuse length")
    hyp = math.sqrt(leg1 * leg1 + leg2 * leg2)
    print("Hypotenuse is :", round(hyp, ROUND))
    print("Perimeter is ", round(hyp + leg1 + leg2, ROUND))
    print("Area is", round(leg1 * leg2 / 2, ROUND))
  elif not leg1 and hypotenuse and leg2:
    print("Calculating leg1 length")
    leg = math.sqrt(hypotenuse * hypotenuse - leg2 * leg2)
    print("Leg1 is ", round(leg, ROUND))
    print("Perimeter is", round(leg + leg2 + hypotenuse, ROUND))
    print("Area is", round(leg * leg2 / 2, ROUND))
  elif not leg2 and hypotenuse and leg1:
    print("Calculating leg2 length")
    leg = math.sqrt(hypotenuse * hypotenuse - leg1 * leg1)
    print("Leg2 is", round(leg, ROUND))
    print("Perimeter is", round(leg + leg1 + hypotenuse,ROUND))
    print("Area is", round(leg * leg1 / 2))
  elif hypotenuse and leg1 and leg2:
    print("Perimeter is ", round(hypotenuse + leg1 + leg2, ROUND))
    print("Area is", round(leg1 * leg2 / 2))
  else:
    print("You supplied less than 2 sides or one side was 0.")

  