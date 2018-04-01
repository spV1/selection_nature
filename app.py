import spacy

async def process_text(data, models):
    doc = models(data)

    list_ent = []
    for ent in doc.ents:
        # print(ent.text, ent.label_, ent.start_char, ent.end_char)
        list_ent.append(dict(map(lambda *args: args, ['text', 'type', 'start', 'end'],
                                 [ent.text, ent.label_, ent.start_char, ent.end_char])))
    dict_ent = {'entities': list_ent}
    # print(dict_ent)
    return dict_ent
