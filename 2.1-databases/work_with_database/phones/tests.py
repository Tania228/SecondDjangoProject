from django.test import TestCase
from .models import Phone


class PhoneTest(TestCase):

    def setUp(self):
        # создаем объект модели
        self.phone = Phone.objects.create(
                             id=10,
                             name="iPhone 11",
                             image='https://avatars.mds.yandex.net/get-mpic/364668/img_id5636027222104023144.jpeg/orig',
                             price=40000,
                             release_date='2020-09-20',
                             lte_exists=True,
                             slug='iphone-11')

    def test_phone_creation(self):
        # Проверяем, что объект создан и имеет правильные значения
        self.assertEqual(self.phone.id, 10)
        self.assertEqual(self.phone.name, "iPhone 11")
        self.assertEqual(self.phone.image,
                         'https://avatars.mds.yandex.net/get-mpic/364668/img_id5636027222104023144.jpeg/orig')
        self.assertEqual(self.phone.price, 40000)
        self.assertEqual(self.phone.release_date, '2020-09-20')
        self.assertTrue(self.phone.lte_exists)
        self.assertEqual(self.phone.slug, 'iphone-11')