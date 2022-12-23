
#Student input grading system
#credits for SDPT SOLUTIONS on youtube

Science = float(input("ENTER YOUR SCIENCE GRADE : "))
Math = float(input("ENTER YOUR MATH GRADE : "))
TLE = float(input("ENTER YOUR TLE GRADE : "))
AP = float(input("ENTER YOUR AP GRADE : "))
English = float(input("ENTER YOUR ENGLISH GRADE : "))
ESP = float(input("ENTER YOUR ESP GRADE : "))
Mapeh = float(input("ENTER YOUR MAPEH GRADE : "))
Filipino = float(input("ENTER YOUR FILIPINO GRADE : "))

Average = (Science + Math + TLE + AP + English + ESP + Mapeh + Filipino) / 8

print("YOUR AVERAGE: " + str(Average))

if Average > 100 or Average <= 50:
    print("INVALID GRADE")
elif Average >= 98:
    print("WITH HIGHEST HONORS")
elif Average >= 95:
    print("WITH HIGH HONORS")
elif Average >= 90:
    print("WITH HONORS")
elif Average >= 75:
    print("PASSED")
else:
    print("FAILED")