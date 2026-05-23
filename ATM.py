user_information = {"Name" : "Jay",
                    "Mobile Number" : "",
                    "ATM PIN" : "6600",
                    "Balance" : 47238,
                    "Transaction History" : []
                    }
print("Please insert your ATM Card")
remaining_attempts = 3
while remaining_attempts > 0:
    user_pin = input("Please Enter Your ATM pin: ")
    if len(user_pin) == 4:
        if user_pin in user_information["ATM PIN"]:
            pass
        else:
            remaining_attempts -= 1
            if remaining_attempts > 0:
                print(f" Invalid Pin entered and you have {remaining_attempts} attempts remaining ")
            else:
                print("Your ATM card is blocked")
