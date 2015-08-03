from django.test import TestCase, Client
from .models import User, Products, Category
from .forms import PostModelForm, AddCategoryModelForm, AddProductModleForm, addProductBycatModelForm, EditUserModelForm
from django.http import HttpResponse, HttpResponseRedirect
from .views import *


# Create your tests here.

class CategorymodelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='baahubali', email='king@maahishmati.com')
        # print('\nHere is the output : ', self.user)

    def test_cat(self):
        self.assertEquals(Category.objects.count(), 0)
        cat = Category.objects.create(name='SAGAR')
        cat.user.add(self.user)
        self.assertEquals(self.user, cat.user.all()[0])

        self.assertEquals('SAGAR', cat.cat_name())
        # print(cat)
        # print(cat.user.all())
        # print(cat.id)


class FormsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='saagar', email='sagar@maahishmathi.com')
        self.emp = {}

    #     self.di = {'username': 'rak', 'email': 'rak@rak.com'}

    def test_PostModelForm(self):
        di = {'username': 'rak', 'email': 'rak@rak.com'}
        post = PostModelForm(di)
        self.assertEquals(post.is_valid(), True)

    def test_AddCategoryModelForm(self):
        # print(self.user)
        di = {'name': 'Rak1', 'description': 'Desc1', 'user': [self.user.id]}
        cats = AddCategoryModelForm(di)
        # print(cats.errors)
        self.assertEquals(cats.is_valid(), True)

    def test_invalid(self):
        cats = AddCategoryModelForm(self.emp)
        self.assertEquals(cats.is_valid(), False)


class test_FormFieldsRequired(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(username='Devasena', email='wife2baahubali@maahishmathi.com')

    #   TESTING ADD CATEGORY WITH EMPTY FIELDS  #

    def test_addCategoryWithEmptyField(self):
        data = {}
        response = self.client.post('/addcategory/', data=data)
        self.assertFormError(response, 'form', 'name', 'This field is required.')

    #   TESTING ADD CATEGORY WITH INVALID DATA    #

    def test_addCategoryWithInvalidData(self):
        data = {'name': 'lion', 'description': '', 'user': []}
        response = self.client.post('/addcategory/', data=data)
        self.assertFormError(response, 'form', 'name',
                             'First letter should be a capital and it must contain a number in it !')
        self.assertIn('name', response.content)


class ViewsTest(TestCase):
    def setUp(self):
        self.client = Client()

        self.user1 = {'username': 'kattappa', 'email': 'slave2king@maahishmathi.com'}
        self.user2 = {'username': 'avanthika', 'email': 'lover_shivudu@maahishmathi.com'}

    def test_simple(self):
        self.assertEquals(User.objects.count(), 0)
        response = self.client.get('/adduser/', follow=True)
        response1 = self.client.post('/adduser/', self.user1, follow=True)

        print 'Views Test >>>>'
        print(response.status_code)
        print(response1.status_code)

        # print(response1.content)
        print 'test Simple response status code : ', response1.status_code
        print 'redirect chain : ', response1.redirect_chain
        self.assertEquals(response.status_code, 200)

        self.assertEquals(User.objects.count(), 1)
        print(User.objects.all())
        # self.assertEquals(response.status_code, 302)
        print 'Ends Views Test here >>>>>>'

    # INDEX TEST #

    def test_index(self):
        response = self.client.get('/products/', follow=True)

        print '\nIndex test : ******', response.status_code, '\n index test ends here ****\n'

    #   USER TEST    #

    def test_user(self):
        response = self.client.get('/products/', follow=True)
        print '\nUser Test: *******', response.status_code, '\n user test ends here *******\n'

    #   CATEGORY TEST   #

    def test_category(self):
        response = self.client.get('/categories/', follow=True)
        print '\nCategory Test: *****', response.status_code, '\n Category test ends here ****** \n'

    #   PRODUCT TEST    #

    def test_product(self):
        response = self.client.get('/product/', follow=True)
        print '\nProduct Test: *****', response.status_code, '\n Product test ends here ******\n'

    #   ADD USER TEST    #

    def test_addUser(self):
        user = {'username': 'shivagami.queen', 'mail': 'mother_baahu_balla@maahishmathi.com'}
        response = self.client.post('/adduser/', user, follow=True)
        print '\nAdd user test : *******'
        print response.status_code
        print User.objects.all()
        print 'redirect chain of add user : ', response.redirect_chain, '\nAdd user test ends here *******\n'

    #   EDIT USER TEST  #

    def test_editUser(self):
        user = User.objects.create(username='K Kattappa', email='slave2king@maahishmathi.com')
        # data = {'username': 'kattappa', 'email': 'slave2king@maahishmathi.com'}
        user_id = str(user.id)

        response = self.client.post('/edituser/' + user_id + '/', follow=True)
        # response2 = self.client.get('/edited/')
        print '\nEdit user test *******'
        print response.status_code
        print 'redirect chain of edit user : ', response.redirect_chain

        self.assertEquals(response.status_code, 200)
        self.assertEquals(User.objects.count(), 1)
        print 'Edit user test ends here *******\n'

    #   DELETE USER TEST    #

    def test_delUser(self):
        user = User.objects.create(username='K Kattappa', email='slave2king@maahishmathi.com')
        user_id = str(user.id)
        cou = User.objects.count()
        print '\nDelete user test *******'
        print 'Before deleting user count:', cou
        response = self.client.post('/delUser/' + user_id + '/', follow=True)

        print response.status_code
        print 'redirect chain of Delete user : ', response.redirect_chain

        self.assertEquals(response.status_code, 200)
        self.assertEquals(User.objects.count(), 0)
        print 'After deleting the user, count :', User.objects.count()
        print 'Delete user test ends here *******\n'

    #   VIEW PRODUCTS BY USER TEST#

    def test_viewProducts(self):
        user = User.objects.create(username='Devasena', email='wife2baahubali@maahishmathi.com')
        name = 'Movie2015'
        description = 'Latest movies'
        category = Category.objects.create(name=name, description=description)
        category.user.add(user)
        user_id = str(user.id)
        pname = 'Baahubali : The Conclusion'
        price = 100
        pdescription = 'Going to be wonderful'
        pcategory = Category.objects.all()[0]
        product = Products.objects.create(name=pname, price=price, description=pdescription, user=user,
                                          category=pcategory)

        cou = category.user.count()

        response = self.client.post('/viewcategory/' + user_id + '/')

        print '\n\n----------- View Products by user --------'
        print 'Product creting -------', product
        print response.status_code
        self.assertEquals(response.status_code, 200)
        self.assertEquals(category.user.count(), 1)
        print '----------- view Products by user ends here ---------\n\n'

    #   VIEW CATEGORY BY USER TEST#

    def test_viewCategory(self):
        user = User.objects.create(username='Devasena', email='wife2baahubali@maahishmathi.com')
        name = 'Movie2015'
        description = 'Latest movies'
        category = Category.objects.create(name=name, description=description)
        category.user.add(user)
        user_id = str(user.id)
        cou = category.user.count()
        response = self.client.post('/viewcategory/' + user_id + '/')

        print '----------- View Category by user --------'
        print response.status_code
        self.assertEquals(response.status_code, 200)
        self.assertEquals(category.user.count(), 1)
        print '----------- view category ends here ---------'

    #   ADD CATEGORY TEST #

    def test_addCategory(self):
        user1 = User.objects.create(username='kattappa', email='slave2king@maahishmathi.com')
        user2 = User.objects.create(username='avanthika', email='lover_shivudu@maahishmathi.com')
        name = 'Movie2015'
        description = 'Latest movies'
        data = {'name': name, 'description': description, 'user': [user1.id, user2.id]}

        print '\n\n------------ Add category test ----------'

        response = self.client.post('/addcategory/', data=data, follow=True)
        print "Add Category : ", response.status_code
        category_list = Category.objects.all()
        print 'category_list', category_list
        users_count = category_list[0].user.count()
        print users_count
        self.assertEquals(response.status_code, 200)
        self.assertEquals(users_count, 2)

    #   ADD PRODUCT TEST    #

    def test_addProduct(self):
        user = User.objects.create(username='Devasena', email='wife2baahubali@maahishmathi.com')
        name = 'Movie2015'
        description = 'Latest movies'
        category = Category.objects.create(name=name, description=description)
        category.user.add(user)
        user_id = str(user.id)
        pname = 'Baahubali : The Conclusion'
        price = 100
        pdescription = 'Going to be wonderful'
        pcategory = Category.objects.all()[0]
        product = {'name': pname, 'price': price, 'description': pdescription, 'user': user.id,
                   "category": category.id}

        cou = category.user.count()
        response = self.client.post('/addproduct/', data=product, follow=True)
        print '\n\n -------- add product test ---------'

        print 'add product ', response.status_code
        print product
        print Products.objects.count()
        print '--------- add product test ends here -------- \n'

    #   EDIT CATEGORY TEST  #

    def test_editCategory(self):
        user1 = User.objects.create(username='kattappa', email='slave2king@maahishmathi.com')
        user2 = User.objects.create(username='avanthika', email='lover_shivudu@maahishmathi.com')
        name = 'Movie2015'
        description = 'Latest movies'
        category = Category.objects.create(name=name, description=description)
        category.user.add(user1, user2)
        category_id = str(category.id)

        print '\n\n------------ Edit category test ----------'

        response = self.client.get('/editcategory/' + category_id + '/')
        print "Edit Category response : ", response.status_code

        self.assertEquals(response.status_code, 200)
        print '------------ Edit category test ends here ---------\n\n'

    #   EDIT PRODUCT TEST  #

    def test_editProduct(self):
        user1 = User.objects.create(username='kattappa', email='slave2king@maahishmathi.com')
        user2 = User.objects.create(username='avanthika', email='lover_shivudu@maahishmathi.com')
        name = 'Movie2015'
        description = 'Latest movies'
        category = Category.objects.create(name=name, description=description)
        category.user.add(user1, user2)

        pname = 'Baahubali : The Conclusion'
        price = 100
        pdescription = 'Going to be wonderful'

        product = Products.objects.create(name=pname, price=price, description=pdescription, user=user1,
                                          category=category)
        product_id = str(product.id)

        print '\n\n------------ Edit product test ----------'

        response = self.client.post('/editproduct/' + product_id + '/')
        print "Edit Category response : ", response.status_code

        self.assertEquals(response.status_code, 200)
        print '------------ Edit product test ends here ---------\n\n'
