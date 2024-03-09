def maxtxt(text, mlen, txtlist):
    """
    Divide el texto en segmentos de longitud máxima `mlen` y los añade a `txtlist`.
    """
    if len(text) <= mlen:
        return False

    start = 0
    end = mlen

    while start < len(text):
        txtlist.append(text[start:end])
        start += mlen
        end += mlen

    return True


def maxembed(embed):
    mlen = 2000  # Asumimos que mlen es una constante definida previamente
    # Separamos el lenguaje del bloque de código
    first_line_end = embed.find('\n') + 1
    language_line = embed[:first_line_end]  # Esto incluirá algo como
    content = embed[first_line_end:-3]  # Excluimos los últimos tres caracteres

    # Calculamos el tamaño máximo de contenido ajustado para incluir los delimitadores de bloque de código
    max_content_length = mlen - len(language_line) - 3  # 3 para los caracteres


    # Segmentamos el contenido
    start = 0
    while start < len(content):
        # Determinamos el punto final del segmento actual, ajustando para evitar cortar una línea en medio
        end = start + max_content_length
        if end < len(content):
            end = content.rfind('\n', start, end) + 1
            if end == 0:  # Si no encontramos un salto de línea, simplemente usamos el corte máximo
                end = start + max_content_length

        segment = (language_line + content[start:end] + "```")
        txtlist.append(segment)
        start = end

    return True



def txtsplit(text, embeds):
    mlen = 2000
    global txtlist
    txtlist = []
    oe = 0  # Índice del final del último embed procesado

    if not embeds:
        if not maxtxt(text, mlen, txtlist):
            txtlist.append(text)
        return txtlist

    for n, embed in enumerate(embeds):
        start, end = embed["start"], embed["end"]

        # Añade el texto previo al embed si no es parte del contenido ya procesado.
        if not text[oe:start].startswith(embed["content"][0:10]):
            if not maxtxt(text[oe:start], mlen, txtlist):
                txtlist.append(text[oe:start])

        # Procesa el contenido del embed actual.
        if (end - start) > mlen:
            maxembed(embed["content"])  # Asume que esta función maneja la división correctamente.
        else:
            txtlist.append(embed["content"])

        oe = end

    # Añade cualquier texto restante después del último embed.
    if oe < len(text):
        if not maxtxt(text[oe:], mlen, txtlist):
            txtlist.append(text[oe:])

    # Eliminar entradas vacías, si las hay.
    txtlist = [item for item in txtlist if item]

    return txtlist
