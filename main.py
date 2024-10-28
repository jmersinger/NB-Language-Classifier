import joblib

cont ='Y'
while cont != 'N':
    while True:
        model_selection = input("Hello! Which model would you like to use? (1 or 2)\n1. 10-Language Model (Faster)\n2. 100-Language Model (Slower)\n")
        
        if model_selection in ['1', '2']:
            break
        else:
            print("Invalid input. Please enter 1 or 2.")

    user_input = [input("Okay! Tell me somthing, and I will tell you what language you are speaking! :)\n")]

    if model_selection == '1':
        NBvect = joblib.load('./NB/models/ten_lang_vect.joblib')
        NBmodel = joblib.load('./NB/models/ten_language_mod.joblib')
    else:
        NBvect = joblib.load('./NB/models/hund_lang_vect.joblib')
        NBmodel = joblib.load('./NB/models/hund_language_mod.joblib')


    sentence_vect = NBvect.transform(user_input)
    output = NBmodel.predict(sentence_vect)

    print("That looks like", output[0], "to me!")

    while True:
        cont = input("Continue? (Y/N): ").upper()
        
        if cont in ['Y', 'N']:
            break
        else:
            print("Invalid input. Please enter Y or N.")


