from postitoimipaikka import hae_postinumerot


def etsi_postinumerot(postitoimipaikka, postinumerot_sanakirja):
    numerot_paikalle = []

    if postitoimipaikka in postinumerot_sanakirja:
        numerot_paikalle = postinumerot_sanakirja[postitoimipaikka]
    return numerot_paikalle


def hae_aineisto():
    postinumerot = hae_postinumerot()

    toimipaikat_ja_numerot = {}

    for numero, toimipaikka in postinumerot.items():
        if toimipaikka in toimipaikat_ja_numerot:
            toimipaikat_ja_numerot[toimipaikka].append(numero)
        else:
            toimipaikat_ja_numerot[toimipaikka] = [numero]

    return toimipaikat_ja_numerot


def main():

    etsittava = input('Kirjoita postitoimipaikka: ').strip().upper()

    aineisto = hae_aineisto()
    # print(aineisto)
    # Num_list = etsi_postinnumerot(etsittava, aineisto)
    # this gives same as below but without "styling"
    # print(Num_list)

    if etsittava in aineisto:
        loydetyt = aineisto[etsittava]
        print('Postinumerot: ' + ', '.join(loydetyt))
    else:
        print('Postitoimipaikkaa ei löytynyt :(')


if __name__ == '__main__':
    main()
