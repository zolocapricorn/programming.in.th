def main(sentence):
    if sentence.upper() == sentence:
        print("All Capital Letter")
    elif sentence.lower() == sentence:
        print("All Small Letter")
    else:
        print("Mix")
main(input())
