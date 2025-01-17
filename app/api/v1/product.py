# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/6/17.
  ↓↓↓ 产品接口 ↓↓↓
"""
from app.extensions.api_docs.redprint import Redprint
from app.extensions.api_docs.v1 import product as api_doc
from app.core.token_auth import auth
from app.models.product import Product
from app.dao.product import ProductDao
from app.libs.error_code import Success
from app.validators.forms import PaginateValidator, CountValidator, IDMustBePositiveIntValidator

__author__ = 'Allen7D'

api = Redprint(name='product', description='产品', api_doc=api_doc)


@api.route('/recent', methods=['GET'])
@api.doc(args=['count'])
def get_recent():
    '''最新的商品'''
    count = CountValidator().validate_for_api().count.data
    product_list = ProductDao.get_most_recent(count=count)
    return Success(product_list)


@api.route('/all/by_category', methods=['GET'])
@api.doc(args=['g.query.category_id'])
def get_all_by_category():
    '''查询某类别所有商品'''
    category_id = IDMustBePositiveIntValidator().get_data().id
    product_list = Product.query.filter_by(category_id=category_id).all_by_wrap()
    return Success(product_list)


@api.route('/list/by_category', methods=['GET'])
@api.doc(args=['g.query.page', 'g.query.size', 'g.query.category_id'], auth=True)
@auth.login_required
def get_list_by_category():
    '''查询某类别商品列表'''
    category_id = IDMustBePositiveIntValidator().get_data().id
    paginate = PaginateValidator().get_data()

    rv = ProductDao.get_list_by_category(category_id=category_id, page=paginate.page, size=paginate.size)
    return Success(rv)


@api.route('/<int:id>', methods=['GET'])
@api.doc(args=['g.path.product_id'])
def get_product(id):
    '''查询商品'''
    product = ProductDao.get_product_detail(id=id)
    return Success(product)


@api.route('', methods=['POST'])
@api.route_meta(auth='新增商品', module='商品')
@api.doc(auth=True)
@auth.group_required
def create_product():
    '''新增商品'''
    return Success(error_code=1)


@api.route('/<int:id>', methods=['PUT'])
@api.route_meta(auth='更新商品', module='商品')
@api.doc(args=['g.path.product_id'], auth=True)
@auth.group_required
def update_product(id):
    '''更新商品'''
    return Success(error_code=1)


@api.route('/<int:id>', methods=['DELETE'])
@api.route_meta(auth='删除商品', module='商品')
@api.doc(args=['g.path.product_id'], auth=True)
@auth.group_required
def delete_product(id):
    '''删除商品'''
    ProductDao.delete_product(id)
    return Success(error_code=2)
