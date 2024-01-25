def character_checker(sentence):
    if sentence.upper() == sentence:
        print("All Capital Letter")
    elif sentence.lower() == sentence:
        print("All Small Letter")
    else:
        print("Mix")
character_checker(input())

