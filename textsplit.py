def txtsplit(text, embeds):
    txtlist = []
    counter = 0
    mlen = 2000
    start = 0
    end = mlen
    if embeds == []:
        if len(text) > mlen:
            c = 0
            l = []
            d = int(len(text)/mlen)
            r = len(text)%mlen
            for i in range(0, d):
                txtlist.append(text[start:end])
                start += mlen
                end += mlen

            if r != 0:
                txtlist.append(text[end:])

        else:
            txtlist = [text]
        return txtlist

    for n in range(0, len(embeds)):
        start = embeds[n]["start"]
        end = embeds[n]["end"]
        if n == 0:
            oe = 0
        txtlist.append(text[oe:start-1])
        txtlist.append(embeds[n]["content"])
        print(txtlist)
        oe = end
        counter += 1
    if end < len(text)-1:
        txtlist.append(text[end:])
    return txtlist
