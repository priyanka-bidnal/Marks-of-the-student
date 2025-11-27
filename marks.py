import sys
if len(sys.argv) == 6:
    n1 = float(sys.argv[1])
    n2 = float(sys.argv[2])
    n3 = float(sys.argv[3])
    n4 = float(sys.argv[4])
    n5 = float(sys.argv[5])
    print("User provided marks:")
else:
    n1 = 80
    n2 = 70
    n3 = 75
    n4 = 60
    n5 = 50
    print("No input provided — using default marks:")
avg = (n1 + n2 + n3 + n4 + n5) / 5
if avg >= 100:
    grade = 'A'
elif avg >= 80:
    grade = 'B'
elif avg >= 65:
    grade = 'C'
elif avg >= 45:
    grade = 'D'
else:
    grade = "Fail"
print("\nAverage Marks:", round(avg, 2))
print("Grade:", grade)
