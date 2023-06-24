def save_to_file(file_name, jobs):
    file = open(f"{file_name}.csv","w")
    file.write("Position,Company,Location,URL\n")

    num =0
    for job in jobs:
        num = num+1
        if num == 50 :
            break
        file.write(
            f"{job['position']},{job['company']},{job['location']},{job['link']}\n")
    file.close()