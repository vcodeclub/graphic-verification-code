# -*- coding: utf-8 -*-

import gvcode


class TestGraphicVerificationCodeCommands(object):

    def test_generate(self):
        im, vcode = gvcode.generate()
        assert len(vcode) == 4

    def test_base64(self):
        b64str, vcode = gvcode.base64()
        assert len(vcode) == 4
