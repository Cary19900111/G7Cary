# from django.test import TestCase
# from .service.mail import mailcode
# # Create your tests here.
# class MailTestCase(TestCase):
#     # def testmail(self):
#     #     c = mailcode("ffffff")
#     #     self.assertEqual(c,'ffffff')
#     def test1(self):
#         c = mailcode("fsjflks")
#         self.assertEqual(c,'fsjflks')

from models import stock_basic,stock_daily,stock_ban

if __name__=="__main__":
    obj = stock_daily.objects.get(code=code).order_by(id)[:1]
    print(obj)

