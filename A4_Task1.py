try:
    b=".venv/sample.txt"
    file=open(b,"r")
    a=(file.readlines())
    for i in range (len(a)):
        print(a[i],end="")
    file.close()
except FileNotFoundError:
    print("This File",b,"Not Found")
finally:
    print("\nFile reading attempt complete.")



