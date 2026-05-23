name=input("Enter your name: ")
date=input("Enter the date: ")

letter="""Good morning {name}
I hope you are doing well. This is a reminder that you have an appointment on {date}.
Please let me know if you have any questions.
Best regards,"""

print(letter.replace("{name}",name).replace("{date}",date))