import pytest
from contextlib import nullcontext as does_not_raise
from PIL import Image
from SberMegaParser import recognize_capcha
from SberMegaParser.tools.capcha.capcha import _recognizer


class FakeImageHref:
    """Fake image href object."""


class TestRecognizeCapcha:
    args = ['image_url', 'expectation']
    vals = [
        ('link/to/image.png', does_not_raise()),
        (FakeImageHref(), pytest.raises(TypeError)),
        (1, pytest.raises(TypeError)),
        (None, pytest.raises(TypeError))
    ]

    @pytest.mark.parametrize(args, vals)
    def test_recognize_capcha_exceptions(self, image_url, expectation):
        with expectation:
            recognize_capcha(image_url)


class TestRecognizer:
    args = ['image', 'result']
    vals = [
        (Image.open('./tests/tools/capcha/images/HAPK3.jpg'), 'HAPK3'),
        (Image.open('./tests/tools/capcha/images/W9H5K.jpg'), 'W9H5K'),
        (Image.open('./tests/tools/capcha/images/N8C6H.jpg'), 'N8C6H'),
        (Image.open('./tests/tools/capcha/images/SKARD.jpg'), 'SKARD'),
        (Image.open('./tests/tools/capcha/images/B4T9S.jpg'), 'B4T9S'),
        (Image.open('./tests/tools/capcha/images/BR8X6.jpg'), 'BR8X6'),
        (Image.open('./tests/tools/capcha/images/59CTR.jpg'), '59CTR'),
        (Image.open('./tests/tools/capcha/images/VETRC.jpg'), 'VETRC'),
        (Image.open('./tests/tools/capcha/images/W93BX.jpg'), 'W93BX'),
        (Image.open('./tests/tools/capcha/images/6AR8R.jpg'), '6AR8R'),
        (Image.open('./tests/tools/capcha/images/R84CH.jpg'), 'R84CH'),
        (Image.open('./tests/tools/capcha/images/9Y548.jpg'), '9Y548'),
        (Image.open('./tests/tools/capcha/images/UXP4D.jpg'), 'UXP4D'),
        (Image.open('./tests/tools/capcha/images/MCSXH.jpg'), 'MCSXH'),
        (Image.open('./tests/tools/capcha/images/X8B9A.jpg'), 'X8B9A'),
        (Image.open('./tests/tools/capcha/images/JA3V8.jpg'), 'JA3V8'),
        (Image.open('./tests/tools/capcha/images/HSB9W.jpg'), 'HSB9W'),
        (Image.open('./tests/tools/capcha/images/HWJRC.jpg'), 'HWJRC'),
        (Image.open('./tests/tools/capcha/images/AWRTB.jpg'), 'AWRTB'),
        (Image.open('./tests/tools/capcha/images/RBSKW.jpg'), 'RBSKW'),
        (Image.open('./tests/tools/capcha/images/CEPT6.jpg'), 'CEPT6'),
        (Image.open('./tests/tools/capcha/images/AUSKW.jpg'), 'AUSKW'),
        (Image.open('./tests/tools/capcha/images/RADTC.jpg'), 'RADTC'),
        (Image.open('./tests/tools/capcha/images/HY4NM.jpg'), 'HY4NM'),
        (Image.open('./tests/tools/capcha/images/DWXM5.jpg'), 'DWXM5'),
        (Image.open('./tests/tools/capcha/images/HSD5A.jpg'), 'HSD5A'),
        (Image.open('./tests/tools/capcha/images/3M56R.jpg'), '3M56R'),
        (Image.open('./tests/tools/capcha/images/HAT8M.jpg'), 'HAT8M'),
        (Image.open('./tests/tools/capcha/images/DT6JX.jpg'), 'DT6JX'),
        (Image.open('./tests/tools/capcha/images/TK58P.jpg'), 'TK58P'),
        (Image.open('./tests/tools/capcha/images/HK5B6.jpg'), 'HK5B6'),
        (Image.open('./tests/tools/capcha/images/HJ9PV.jpg'), 'HJ9PV'),
        (Image.open('./tests/tools/capcha/images/U64YW.jpg'), 'U64YW'),
        (Image.open('./tests/tools/capcha/images/URVTP.jpg'), 'URVTP'),
        (Image.open('./tests/tools/capcha/images/AWSKH.jpg'), 'AWSKH'),
        (Image.open('./tests/tools/capcha/images/TUTXJ.jpg'), 'TUTXJ'),
        (Image.open('./tests/tools/capcha/images/9M4BP.jpg'), '9M4BP'),
        (Image.open('./tests/tools/capcha/images/6H3T8.jpg'), '6H3T8'),
        (Image.open('./tests/tools/capcha/images/ADUR3.jpg'), 'ADUR3'),
        (Image.open('./tests/tools/capcha/images/JN6TS.jpg'), 'JN6TS'),
        (Image.open('./tests/tools/capcha/images/TSMS9.jpg'), 'TSMS9'),
        (Image.open('./tests/tools/capcha/images/R48EK.jpg'), 'R48EK'),
        (Image.open('./tests/tools/capcha/images/4NV3A.jpg'), '4NV3A'),
        (Image.open('./tests/tools/capcha/images/Y4VUJ.jpg'), 'Y4VUJ'),
        (Image.open('./tests/tools/capcha/images/459CT.jpg'), '459CT'),
        (Image.open('./tests/tools/capcha/images/9T4JW.jpg'), '9T4JW'),
        (Image.open('./tests/tools/capcha/images/XRVSH.jpg'), 'XRVSH'),
        (Image.open('./tests/tools/capcha/images/WB3CX.jpg'), 'WB3CX'),
        (Image.open('./tests/tools/capcha/images/D4TSH.jpg'), 'D4TSH'),
        (Image.open('./tests/tools/capcha/images/3JYP4.jpg'), '3JYP4'),
        (Image.open('./tests/tools/capcha/images/WKRH5.jpg'), 'WKRH5'),
        (Image.open('./tests/tools/capcha/images/D35UA.jpg'), 'D35UA'),
        (Image.open('./tests/tools/capcha/images/XKWDN.jpg'), 'XKWDN'),
        (Image.open('./tests/tools/capcha/images/KNYWV.jpg'), 'KNYWV'),
        (Image.open('./tests/tools/capcha/images/C46U5.jpg'), 'C46U5'),
        (Image.open('./tests/tools/capcha/images/SREMD.jpg'), 'SREMD'),
        (Image.open('./tests/tools/capcha/images/HRDX8.jpg'), 'HRDX8'),
        (Image.open('./tests/tools/capcha/images/YU4RT.jpg'), 'YU4RT'),
        (Image.open('./tests/tools/capcha/images/W9NB4.jpg'), 'W9NB4'),
        (Image.open('./tests/tools/capcha/images/MUX2S.jpg'), 'MUX2S')
    ]

    @pytest.mark.parametrize(args, vals)
    def test_recognizer_quality(self, image, result):
        assert _recognizer(image) == result
