import unittest

from coupons.utils import _create_background_image, _generate_barcode_image

class TestHelperFuncs(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_create_background_image_size(self):
        try:
            width, height = 640, 480
            img = _create_background_image(width, height)
            self.assertEqual(img.size[0], width)
            self.assertEqual(img.size[1], height)
        except Exception as e:
            self.fail(e)

    def test_generate_barcode_image(self):
        try:
            barcode = _generate_barcode_image('567890')
            img = barcode.render()
            self.assertEqual(img.size[0], 360)
            self.assertEqual(img.size[1], 280)
        except Exception as e:
            self.fail(e)


if __name__ == '__main__':
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestHelperFuncs)
    unittest.TextTestRunner().run(suite)
