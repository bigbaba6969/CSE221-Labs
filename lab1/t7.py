def sorting(trains, n):
    i = 0
    while i < n- 1:
        j = 0
        while j < n - i - 1:
            name1, time1, a ,b= trains[j]
            name2, time2, a ,b= trains[j + 1]           
            if (name1 == name2 and time1 < time2) or name1 > name2:
                trains[j], trains[j + 1] = trains[j + 1], trains[j]
            j+= 1
        i+= 1
 
def main():
    n = int(input())
    t= []    
    i = 0
    while i < n:
        line= input()
        parts = line.split()
        name = parts[0]
        departure = parts[-1]
        destination= parts[3]  
        train_description = " ".join(parts[1:-2]) + " " + parts[-2] + " " + parts[-1]
        t.append((name, departure, destination, train_description))
        i += 1
    
    sorting(t, n)
    i = 0
    while i < n:
        print(t[i][0] + " " + t[i][3])
        i += 1
 
train=main()