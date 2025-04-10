try:
    file=open(".venv/sample.txt","r")
    a=(file.readlines())
    for i in range (len(a)):
        print(a[i],end="")
    file.close()
except FileNotFoundError:
    print("Correct the file")
finally:
    print("\nFile reading attempt complete.")



