fileName = "0.wdc.txt"
outputFile = "kpIndex.csv"

with open(outputFile, "w") as output:
    for i in range(2016, 2024):
        with open(fileName.replace("0", str(i)), "r") as data:
            for line in data:
                if "#" in line:
                    continue
                year = "20" + line[0:2]
                month = line[2:4].strip().zfill(2)
                day = line[4:6].strip().zfill(2)

                for x in range(0, 8):
                    kp = round(int(line[(12 + 2 * x) : (12 + 2 * x + 2)]) / 10, 1)
                    hour = f"{3*x}".zfill(2) + ":00:00"
                    output.write(f"{year}-{month}-{day} {hour}; {kp}\n")
