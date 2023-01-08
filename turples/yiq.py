# https://dodona.ugent.be/nl/courses/1286/series/14352/activities/2097740983

def yiq(kleur):
    y = kleur[0] * 0.299 + kleur[1] * 0.587 + kleur[2] * 0.114
    y = round(y,4)
    i = kleur[0] * 0.596 - kleur[1] * 0.274 - kleur[2] * 0.322
    i = round(i,4)
    q = kleur[0] * 0.211 - kleur[1] * 0.523 + kleur[2] * 0.312
    q = round(q, 4)
    return (y, i, q)

rgb = (82, 227, 112)

print(yiq(rgb))