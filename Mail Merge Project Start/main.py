
# r defines that the string is a raw string and not consider the baclashes as escape sequences
letter_file = open(r".\Input\Letters\starting_letter.txt", mode="r+")
names_file = open(r".\Input\Names\invited_names.txt", mode = "r+")

letter = letter_file.read()

lines = names_file.readlines()

for names in lines:
    file_names = names.strip()
    file_path = f".\Output\ReadyToSend\letter_to_{file_names}.txt"
    named_file = open(file_path, mode="w")
    # rectified_content = f"Dear {file_names},\nYou are invited to my birthday this Saturday.\nHope you can make it!\nAngela"
    rectified_content = letter.replace("[name]", file_names)
    named_file.write(rectified_content)
    named_file.close()


names_file.close()
letter_file.close()
