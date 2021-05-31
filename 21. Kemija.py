def main(code, count, result):
    while count != len(code):
        if code[count] in ["a", "e", "i", "o", "u"]:
            result.append(code[count])
            count += 3
        else:
            result.append(code[count])
            count += 1
    print(*result, sep="")
main(input(), 0, [])