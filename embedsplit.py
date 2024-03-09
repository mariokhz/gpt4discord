def emsplit(text):
    embedcounter = 0
    print(text)
    start = []
    end = []
    reseml = []
    for i in range(0, len(text)-1):
        if (text[i-2] == "`") & (text[i-1] == "`") & (text[i] == "`") :
            if embedcounter%2 == 0:
                startn = i-2
                start.append(startn)
                for j in range(i+1, len(text)):
                    if (text[j-2] == "`") & (text[j-1] == "`") & (text[j] == "`") :
                        endn = j+1
                        end.append(endn)
                        break
                reseml.append(text[startn:endn])
                print(reseml)
            embedcounter += 1

    embeds = []
    for k in range(0, len(reseml)):
        e = {"start" : start[k], "end" : end[k], "content" : reseml[k]}
        embeds.append(e)
    return embeds
