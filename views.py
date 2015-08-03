from django.shortcuts import get_object_or_404, render, render_to_response
from .forms import PostModelForm, EditUserModelForm, AddCategoryModelForm, addProductBycatModelForm, AddProductModleForm
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.conf import settings

#   OF PRODUCTS  #
from .models import Category, Products, Basket
from .models import User as PUser
#### for login
# views.py
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, models
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext


# Create your views here.

#   VIEWS FOR PRODUCTS  #

def index(request):
    total_list = PUser.objects.all()
    context = {'total_list': total_list}
    return render(request, 'products/index.html', context)


def user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'products/user.html', {'user': user})


def category(request):
    category_list = Category.objects.all()
    context = {'category_list': category_list}
    print context
    return render(request, 'products/categories.html', context)


def product(request):
    products_list = Products.objects.all()
    print(products_list)
    basket_count = Basket.objects.filter(auth_user=request.user).count()
    basket_items = Basket.objects.filter(auth_user=request.user)
    return render(request, 'products/products.html', {'products_list': products_list, 'user': User, 'basket_count':
        basket_count, 'basket_items': basket_items})


def adduser(request):
    if request.method == 'GET':
        form = PostModelForm()

    else:
        form = PostModelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('products:index'))
    return render(request, 'products/addUser.html', {'form': form})


def addproduct(request):
    template_name = 'products/addProduct.html'
    # user = User.objects.get(id=user_id)
    form = AddProductModleForm()

    if request.method == 'POST':
        form = AddProductModleForm(request.POST)
        if form.is_valid():
            form.save()
            # return HttpResponse('Items saved!')
            return HttpResponseRedirect('/products/product/')

    dict_items = {'form': form}
    return render(request, template_name, dict_items)


def addProduct(request, user_id):
    user = User.objects.get(pk=user_id)
    template_name = 'products/addProduct.html'
    # user = User.objects.get(id=user_id)
    form = AddProductModleForm()

    if request.method == 'POST':
        form = AddProductModleForm(request.POST)
        if form.is_valid():
            form.save()
            # return HttpResponse('Items saved!')
            return HttpResponseRedirect('/products/product/')

    dict_items = {'form': form}
    return render(request, template_name, dict_items)


def addcategory(request):
    template_name = 'products/addCategory.html'
    form = AddCategoryModelForm()
    if request.method == 'POST':
        form = AddCategoryModelForm(request.POST)
        if form.is_valid():
            form.save()
            # name = request.POST['name']
            # description = request.POST['description']
            #
            # category = Category.objects.create(name=name, description=description)
            # category.user.add(user)
            # return HttpResponseRedirect(reverse('products:viewcategory'))
            return HttpResponseRedirect('/products/categories/')
    dict_items = {'form': form, 'user': user}
    return render(request, template_name, dict_items)

    # return render(request, 'products/addCategory.html', {'form':form})


def addCategory(request, user_id):
    user = User.objects.get(pk=user_id)
    template_name = 'products/addCategory.html'
    form = AddCategoryModelForm()
    if request.method == 'POST':
        form = AddCategoryModelForm(request.POST)
        if form.is_valid():
            form.save()
            # name = request.POST['name']
            # description = request.POST['description']
            #
            # category = Category.objects.create(name=name, description=description)
            # category.user.add(user)
            # return HttpResponseRedirect(reverse('products:viewcategory'))
            return HttpResponseRedirect('/products/categories/')
    dict_items = {'form': form, 'user': user}
    return render(request, template_name, dict_items)


def edituser(request, user_id):
    user = User.objects.get(id=user_id)
    form = EditUserModelForm(instance=user)
    return render(request, 'products/editUser.html', {'form': form, 'user': user})


def edited(request):
    if request.method == 'POST':
        email = request.POST['email']
        print(email)
        user = User.objects.get(email=email)
        print(user)
        form = EditUserModelForm(request.POST, instance=user)
        print(form.is_valid())
        print(form)
        if (form.is_valid()):
            form.save()
            return HttpResponseRedirect(reverse('products:index'))
        return render(request, 'products/editUser.html', {'form': form, 'user': user})


def editproduct(request, product_id):
    product = Products.objects.get(id=product_id)
    form = AddProductModleForm(instance=product)
    if request.method == 'POST':
        form = AddProductModleForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/products/product/')
    template_name = 'products/editProduct.html'
    return render(request, template_name, {'form': form, 'product_id': product_id})


def editcategory(request, category_id):
    category = Category.objects.get(id=category_id)
    form = AddCategoryModelForm(instance=category)
    if request.method == 'POST':
        form = AddCategoryModelForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/products/categories/')

    template_name = 'products/editCategory.html'
    return render(request, template_name, {'form': form})


def viewcategory(request, user_id):
    user = User.objects.get(id=user_id)
    list_category = Category.objects.filter(user=user)
    print(list_category)
    return render(request, 'products/viewCategory.html', {'list_category': list_category, 'user': user})

def viewCategory(request, user_id):
    user = PUser.objects.get(id=user_id)
    list_category = Category.objects.filter(user=user)
    print(list_category)
    return render(request, 'products/viewCategory.html', {'list_category': list_category, 'user': user})


def viewproducts(request):
    list_products = Products.objects.all()
    print(list_products)
    basket_count = Basket.objects.filter(auth_user=request.user).count()
    basket_items = Basket.objects.filter(auth_user=request.user)
    return render(request, 'products/viewProducts.html', {'list_products': list_products, 'user': User, 'basket_count':
        basket_count, 'basket_items': basket_items})

    # return HttpResponse(list_products)


def viewProducts(request, user_id):
    print user_id
    user = PUser.objects.get(id=user_id)
    list_products = Products.objects.filter(user=user)
    print(list_products)
    return render(request, 'products/viewProducts.html', {'list_products': list_products, 'user': user})
#
# def viewProducts(request, user_name):
#     print user_name
#     user = PUser.objects.get(username=user_name)
#     list_products = Products.objects.filter(user=user)
#     print(list_products)
#     return render(request, 'products/viewProducts.html', {'list_products': list_products, 'user': user})
# return HttpResponse(list_products)


def viewproductsByCat(request, user_id, category_id):
    user = User.objects.get(id=user_id)
    category = Category.objects.get(id=category_id)

    product_list = Products.objects.filter(user=user).filter(category=category)

    return render(request, 'products/viewProductsByCategory.html', {'product_list': product_list, 'user': user,
                                                                    'category': category})


def viewproductsByCategory(request, category_id):
    category = Category.objects.get(id=category_id)
    product_list = Products.objects.filter(category=category)
    print(product_list)
    return render(request, 'products/viewProductsByCategory.html', {'product_list': product_list, 'category': category})


def addProductByCat(request, user_id, category_id):
    user = User.objects.get(id=user_id)
    category = Category.objects.get(id=category_id)

    form = addProductBycatModelForm()
    if request.method == 'POST':
        form = addProductBycatModelForm(request.POST)
        if form.is_valid():
            name = request.POST['name']
            price = request.POST['price']

            product = Products.objects.create(name=name, price=price, user=user, category=category)
            return HttpResponseRedirect(reverse('products:viewcategory', kwargs={'user_id': user.id}))
    return render(request, 'prodcuts/addProductsByCategory.html', {'form': form, 'user': user, 'category': category})


def DelProductByCat(request, user_id, category_id):
    user = User.objects.get(id=user_id)
    category = Category.objects.get(id=category_id)
    product_list = Products.objects.filter(user=user).filter(category=category)

    return render(request, 'products/deleteProductsByCategory.html',
                  {'product_list': product_list, 'user': user, 'category': category})


def delProduct(request, product_id):
    product = Products.objects.get(id=product_id)
    product.delete()
    # return HttpResponse('Product Deleted Successfully !')
    return HttpResponseRedirect('/products/product/')


def delCategory(request, category_id):
    category = Category.objects.get(id=category_id)
    category.delete()
    return HttpResponseRedirect('/products/categories/')


def delUser(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    return HttpResponseRedirect('/products/')

    # User login


@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('success/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
        'form': form
    })

    return render_to_response(
        'register.html',
        variables,
    )


def register_success(request):
    return render_to_response(
        'success.html',
    )


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required
def home(request):
    return render_to_response(
        'home.html',
        {'user': request.user}
    )


######### add to basket view is here

def addToBasket(request, product_id):
    product = Products.objects.get(id=product_id)
    print request.user, product
    test = Basket.objects.create(auth_user=request.user, product=product)
    print test
    # Basket()
    return HttpResponseRedirect(reverse('products:product'))

def delFromBasket(request, product_id):
    product = Products.objects.get(id=product_id)
    print product
    basket = Basket.objects.filter(auth_user=request.user, product=product)
    print basket
    basket.delete()
    return HttpResponseRedirect(reverse('products:product'))


############

##### for displaying the extended html content ############

def display(request):
    return render(request, 'products/display.html')
