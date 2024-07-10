from contextlib import nullcontext as does_not_raise
import pytest
import cv2
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
        (cv2.imread('./tests/tools/capcha/images/O4X3Y5.png'), 'O4X3Y5'),
        (cv2.imread('./tests/tools/capcha/images/3CE9C8.png'), '3CE9C8'),
        (cv2.imread('./tests/tools/capcha/images/6CCACC.png'), '6CCACC'),
        (cv2.imread('./tests/tools/capcha/images/C50264.png'), 'C50264'),
        (cv2.imread('./tests/tools/capcha/images/CB2PEC.png'), 'CB2PEC'),
        (cv2.imread('./tests/tools/capcha/images/MBESXY.png'), 'MBESXY'),
        (cv2.imread('./tests/tools/capcha/images/KTOKYM.png'), 'KTOKYM'),
        (cv2.imread('./tests/tools/capcha/images/393APY.png'), '393APY'),
        (cv2.imread('./tests/tools/capcha/images/KAPEMO.png'), 'KAPEMO'),
        (cv2.imread('./tests/tools/capcha/images/KCP1MA.png'), 'KCP1MA'),
        (cv2.imread('./tests/tools/capcha/images/OEK3C5.png'), 'OEK3C5'),
        (cv2.imread('./tests/tools/capcha/images/TAB18K.png'), 'TAB18K'),
        (cv2.imread('./tests/tools/capcha/images/6X9043.png'), '6X9043'),
        (cv2.imread('./tests/tools/capcha/images/KMATCH.png'), 'KMATCH'),
        (cv2.imread('./tests/tools/capcha/images/586EAK.png'), '586EAK'),
        (cv2.imread('./tests/tools/capcha/images/MAPO16.png'), 'MAPO16'),
        (cv2.imread('./tests/tools/capcha/images/HAPCK5.png'), 'HAPCK5'),
        (cv2.imread('./tests/tools/capcha/images/BPBC46.png'), 'BPBC46'),
        (cv2.imread('./tests/tools/capcha/images/KO1TK6.png'), 'KO1TK6'),
        (cv2.imread('./tests/tools/capcha/images/KPXHXH.png'), 'KPXHXH'),
        (cv2.imread('./tests/tools/capcha/images/3619KY.png'), '3619KY'),
        (cv2.imread('./tests/tools/capcha/images/2CEMEA.png'), '2CEMEA'),
        (cv2.imread('./tests/tools/capcha/images/PBT2MK.png'), 'PBT2MK'),
        (cv2.imread('./tests/tools/capcha/images/PHCTYC.png'), 'PHCTYC'),
        (cv2.imread('./tests/tools/capcha/images/KOXCY2.png'), 'KOXCY2'),
        (cv2.imread('./tests/tools/capcha/images/P4OOOA.png'), 'P4OOOA'),
        (cv2.imread('./tests/tools/capcha/images/BAKBHT.png'), 'BAKBHT'),
        (cv2.imread('./tests/tools/capcha/images/632383.png'), '632383'),
        (cv2.imread('./tests/tools/capcha/images/3CXB4A.png'), '3CXB4A'),
        (cv2.imread('./tests/tools/capcha/images/PYAMP2.png'), 'PYAMP2'),
        (cv2.imread('./tests/tools/capcha/images/8KP365.png'), '8KP365'),
        (cv2.imread('./tests/tools/capcha/images/BPOKAM.png'), 'BPOKAM'),
        (cv2.imread('./tests/tools/capcha/images/OPOAK5.png'), 'OPOAK5'),
        (cv2.imread('./tests/tools/capcha/images/2ME3XE.png'), '2ME3XE'),
        (cv2.imread('./tests/tools/capcha/images/CC2HKX.png'), 'CC2HKX'),
        (cv2.imread('./tests/tools/capcha/images/OBY13M.png'), 'OBY13M'),
        (cv2.imread('./tests/tools/capcha/images/KT1351.png'), 'KT1351'),
        (cv2.imread('./tests/tools/capcha/images/ECKP2X.png'), 'ECKP2X'),
        (cv2.imread('./tests/tools/capcha/images/A2TYAK.png'), 'A2TYAK'),
        (cv2.imread('./tests/tools/capcha/images/MOACHA.png'), 'MOACHA'),
        (cv2.imread('./tests/tools/capcha/images/2622YM.png'), '2622YM'),
        (cv2.imread('./tests/tools/capcha/images/KOE3OK.png'), 'KOE3OK'),
        (cv2.imread('./tests/tools/capcha/images/K422YX.png'), 'K422YX'),
        (cv2.imread('./tests/tools/capcha/images/EA8BTC.png'), 'EA8BTC'),
        (cv2.imread('./tests/tools/capcha/images/CKKEYX.png'), 'CKKEYX'),
        (cv2.imread('./tests/tools/capcha/images/BXOHEE.png'), 'BXOHEE'),
        (cv2.imread('./tests/tools/capcha/images/P34CA6.png'), 'P34CA6'),
        (cv2.imread('./tests/tools/capcha/images/KHKCBO.png'), 'KHKCBO'),
        (cv2.imread('./tests/tools/capcha/images/6C458C.png'), '6C458C'),
        (cv2.imread('./tests/tools/capcha/images/TAEA6B.png'), 'TAEA6B'),
        (cv2.imread('./tests/tools/capcha/images/80C522.png'), '80C522'),
        (cv2.imread('./tests/tools/capcha/images/BTPK8C.png'), 'BTPK8C'),
        (cv2.imread('./tests/tools/capcha/images/COMH43.png'), 'COMH43'),
        (cv2.imread('./tests/tools/capcha/images/OBB4KX.png'), 'OBB4KX'),
        (cv2.imread('./tests/tools/capcha/images/PKABPK.png'), 'PKABPK'),
        (cv2.imread('./tests/tools/capcha/images/CCX5K3.png'), 'CCX5K3'),
        (cv2.imread('./tests/tools/capcha/images/76353.png'), '76353'),
        (cv2.imread('./tests/tools/capcha/images/OKCEOO.png'), 'OKCEOO'),
        (cv2.imread('./tests/tools/capcha/images/TCAXCP.png'), 'TCAXCP'),
        (cv2.imread('./tests/tools/capcha/images/K2CTBK.png'), 'K2CTBK'),
        (cv2.imread('./tests/tools/capcha/images/PMCXEC.png'), 'PMCXEC'),
        (cv2.imread('./tests/tools/capcha/images/KKHMAY.png'), 'KKHMAY'),
        (cv2.imread('./tests/tools/capcha/images/AHMMHY.png'), 'AHMMHY'),
        (cv2.imread('./tests/tools/capcha/images/HAEYOY.png'), 'HAEYOY'),
        (cv2.imread('./tests/tools/capcha/images/4856ME.png'), '4856ME'),
        (cv2.imread('./tests/tools/capcha/images/HMBBMA.png'), 'HMBBMA'),
        (cv2.imread('./tests/tools/capcha/images/388108.png'), '388108'),
        (cv2.imread('./tests/tools/capcha/images/50T52A.png'), '50T52A'),
        (cv2.imread('./tests/tools/capcha/images/CYOK8X.png'), 'CYOK8X'),
        (cv2.imread('./tests/tools/capcha/images/BEAOYC.png'), 'BEAOYC'),
        (cv2.imread('./tests/tools/capcha/images/820046.png'), '820046'),
        (cv2.imread('./tests/tools/capcha/images/222041.png'), '222041'),
        (cv2.imread('./tests/tools/capcha/images/5PP3AE.png'), '5PP3AE'),
        (cv2.imread('./tests/tools/capcha/images/AOYTB3.png'), 'AOYTB3'),
        (cv2.imread('./tests/tools/capcha/images/4OKK3C.png'), '4OKK3C'),
        (cv2.imread('./tests/tools/capcha/images/OCKBAC.png'), 'OCKBAC'),
        (cv2.imread('./tests/tools/capcha/images/OXHAPY.png'), 'OXHAPY'),
        (cv2.imread('./tests/tools/capcha/images/CXPYEY.png'), 'CXPYEY'),
        (cv2.imread('./tests/tools/capcha/images/335HPK.png'), '335HPK'),
        (cv2.imread('./tests/tools/capcha/images/P8CY8H.png'), 'P8CY8H'),
        (cv2.imread('./tests/tools/capcha/images/863153.png'), '863153'),
        (cv2.imread('./tests/tools/capcha/images/BKEYK6.png'), 'BKEYK6'),
        (cv2.imread('./tests/tools/capcha/images/KAOPEY.png'), 'KAOPEY'),
        (cv2.imread('./tests/tools/capcha/images/2K2XOX.png'), '2K2XOX'),
        (cv2.imread('./tests/tools/capcha/images/KBOKCX.png'), 'KBOKCX'),
        (cv2.imread('./tests/tools/capcha/images/25257.png'), '25257'),
        (cv2.imread('./tests/tools/capcha/images/ACHOTM.png'), 'ACHOTM'),
        (cv2.imread('./tests/tools/capcha/images/KEKOBT.png'), 'KEKOBT'),
        (cv2.imread('./tests/tools/capcha/images/CHOYKB.png'), 'CHOYKB'),
        (cv2.imread('./tests/tools/capcha/images/103M83.png'), '103M83'),
        (cv2.imread('./tests/tools/capcha/images/PKB2AC.png'), 'PKB2AC'),
        (cv2.imread('./tests/tools/capcha/images/E2POPM.png'), 'E2POPM'),
        (cv2.imread('./tests/tools/capcha/images/PXKHAP.png'), 'PXKHAP'),
        (cv2.imread('./tests/tools/capcha/images/6PYAPU.png'), '6PYAPU'),
        (cv2.imread('./tests/tools/capcha/images/EKXXAY.png'), 'EKXXAY'),
        (cv2.imread('./tests/tools/capcha/images/MXYYBK.png'), 'MXYYBK'),
        (cv2.imread('./tests/tools/capcha/images/PKKMAY.png'), 'PKKMAY'),
        (cv2.imread('./tests/tools/capcha/images/PTMCCK.png'), 'PTMCCK'),
        (cv2.imread('./tests/tools/capcha/images/HTEACY.png'), 'HTEACY'),
        (cv2.imread('./tests/tools/capcha/images/4HE63Y.png'), '4HE63Y'),
        (cv2.imread('./tests/tools/capcha/images/MH2CTB.png'), 'MH2CTB'),
        (cv2.imread('./tests/tools/capcha/images/4658Y3.png'), '4658Y3'),
        (cv2.imread('./tests/tools/capcha/images/CCO31K.png'), 'CCO31K'),
        (cv2.imread('./tests/tools/capcha/images/PCBHPK.png'), 'PCBHPK'),
        (cv2.imread('./tests/tools/capcha/images/39TUPC.png'), '39TUPC'),
        (cv2.imread('./tests/tools/capcha/images/845290.png'), '845290'),
        (cv2.imread('./tests/tools/capcha/images/3X5HEP.png'), '3X5HEP'),
        (cv2.imread('./tests/tools/capcha/images/PP8C66.png'), 'PP8C66'),
        (cv2.imread('./tests/tools/capcha/images/TKK448.png'), 'TKK448'),
        (cv2.imread('./tests/tools/capcha/images/KO52YK.png'), 'KO52YK'),
        (cv2.imread('./tests/tools/capcha/images/CEP3XO.png'), 'CEP3XO'),
        (cv2.imread('./tests/tools/capcha/images/CAXAOP.png'), 'CAXAOP'),
        (cv2.imread('./tests/tools/capcha/images/EOX2CP.png'), 'EOX2CP'),
        (cv2.imread('./tests/tools/capcha/images/B2HOM2.png'), 'B2HOM2'),
        (cv2.imread('./tests/tools/capcha/images/OPCAOE.png'), 'OPCAOE'),
        (cv2.imread('./tests/tools/capcha/images/MKCKA5.png'), 'MKCKA5'),
        (cv2.imread('./tests/tools/capcha/images/234848.png'), '234848'),
        (cv2.imread('./tests/tools/capcha/images/236050.png'), '236050'),
        (cv2.imread('./tests/tools/capcha/images/062C66.png'), '062C66'),
        (cv2.imread('./tests/tools/capcha/images/2EXY23.png'), '2EXY23'),
        (cv2.imread('./tests/tools/capcha/images/52447.png'), '52447')
    ]

    @pytest.mark.parametrize(args, vals)
    def test_recognizer_quality(self, image, result):
        assert _recognizer(image) == result
