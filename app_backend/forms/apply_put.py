#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: apply_put.py
@time: 2017/4/13 下午9:31
"""


from flask_wtf import FlaskForm as Form
from wtforms import StringField, PasswordField, BooleanField, DateField, DateTimeField
from wtforms.validators import DataRequired, Length, NumberRange, EqualTo, Email, ValidationError, IPAddress
from app_backend.api.user_auth import get_user_auth_row
from app_backend.forms import SelectBS
from app_api.maps import type_apply_list


class ApplyPutSearchForm(Form):
    """
    投资申请搜索表单
    """
    apply_put_id = StringField('Apply Put Id')
    user_id = StringField('User Id')
    type_apply = SelectBS('Type Apply', default='', choices=type_apply_list)
    money_apply = StringField('Type Apply')
    status_apply = StringField('Type Apply')
    status_order = StringField('Status Order')
    status_delete = StringField('Status Delete')
    start_time = StringField('Start Time')
    end_time = StringField('End Time')