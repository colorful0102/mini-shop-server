# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2019/6/27.
  ↓↓↓ 管理员接口 ↓↓↓
"""
from app.extensions.api_docs.redprint import Redprint
from app.core.token_auth import auth
from app.models.user import User as UserModel
from app.dao.user import UserDao
from app.libs.error_code import Success
from app.validators.forms import PaginateValidator, ResetPasswordValidator, UpdateAdminValidator

__author__ = 'Allen7D'

api = Redprint(name='user', description='用户管理', api_doc=None, alias='cms_user')


@api.route('/list', methods=['GET'])
@api.route_meta(auth='查询用户列表', module='用户')
@api.doc(args=['g.query.page', 'g.query.size'], auth=True)
@auth.group_required
def get_user_list():
    '''查询用户列表(分页)'''
    page_validator = PaginateValidator().get_data()
    rv = UserDao.get_user_list(page_validator.page, page_validator.size)
    return Success(rv)


@api.route('/<int:uid>', methods=['GET'])
@api.route_meta(auth='查询用户详情', module='用户')
@api.doc(args=['g.path.uid+'], auth=True)
@auth.group_required
def get_user(uid):
    '''查询用户信息'''
    user = UserModel.query.filter_by(id=uid).first_or_404()
    return Success(user)


@api.route('/<int:uid>/group', methods=['PUT'])
@api.route_meta(auth='更新用户分组', module='用户')
@api.doc(args=['g.path.uid+', 'g.body.group_id'], auth=True)
@auth.group_required
def update_user(uid):
    '''更新用户分组'''
    group_id = UpdateAdminValidator().get_data('group_id')
    UserDao.change_group(uid, group_id)
    return Success(error_code=1)


@api.route('/<int:uid>', methods=['DELETE'])
@api.route_meta(auth='删除用户', module='用户')
@api.doc(args=['g.path.uid+'], auth=True)
@auth.group_required
def delete_user(uid):
    '''删除用户'''
    UserDao.delete_user(uid)
    return Success(error_code=2)


@api.route('/<int:uid>/password', methods=['PUT'])
@api.route_meta(auth='更改用户密码', module='用户')
@api.doc(args=['g.path.uid+', 'g.body.new_password', 'g.body.confirm_password'], auth=True)
@auth.group_required
def reset_password(uid):
    '''更改用户密码'''
    new_password = ResetPasswordValidator().nt_data.new_password
    UserDao.reset_password(uid=uid, password=new_password)
    return Success(error_code=1, msg='密码修改成功')