from postinumerot import etsi_postinumerot
from postinumerot import hae_aineisto

aineisto = hae_aineisto()


def test_if_postiTmp_doesnt_exist():
    postiTmp = 'HUIJARI'
    assert postiTmp not in aineisto


def test_postitoimipaikka_has_only_one():
    postiTmp = 'LUUSNIEMI'
    result_nums = etsi_postinumerot(postiTmp, aineisto)
    assert len(result_nums) == 1


def test_postoimipaikka_has_many():
    postiTmp = 'VANTAA'
    result_nums = etsi_postinumerot(postiTmp, aineisto)
    assert len(result_nums) > 1


def test_etsi_postinumerot_keravalle():
    postiTmp = 'KERAVA'
    target_list = ['04230', '04200', '04261',
                   '04260', '04220', '04201', '04251', '04250']
    i = etsi_postinumerot(postiTmp, aineisto)

    assert i == target_list
