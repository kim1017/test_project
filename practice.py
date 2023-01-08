def std_weight(height, gender):
    if gender == "men":
        return height ** 2 * 22
    else:
        return height * height * 21

height = 180
gender = "women"
weight = round(std_weight(height / 100, gender), 2)

print(f"height {height} {gender} standard weight is {weight}kg.")

