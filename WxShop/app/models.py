#coding:utf-8
from __future__ import unicode_literals
from datetime import datetime
import hashlib
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from markdown import markdown
import bleach
from flask import current_app, request, url_for
from flask.ext.login import UserMixin, AnonymousUserMixin
#from app.exceptions import ValidationError
from . import db, login_manager


class Permission:
    ROOT = 0x01
    ADMIN = 0x02
    SERVICE = 0x03
    SELLER = 0x04
    BUYER = 0x05


class Role(db.Model):
    __tablename__ = 'Role'
    RoleId = db.Column(db.Integer, primary_key=True)
    RoleName = db.Column(db.String(128))
    RoleValue = db.Column(db.Integer)
    @staticmethod
    def insert_roles():
        roles = {
            'root':Permission.ROOT,
            'admin':Permission.ADMIN,
            'service':Permission.SERVICE,
            'seller':Permission.SELLER,
            'BUYER':Permission.BUYER
        }
        for r in roles:
            role = Role.query.filter_by(name=r).first()
            if role is None:
                role = Role(name=r)
            role.RoleName = roles[r][0]
            role.RoleValue = roles[r][1]
            print role.RoleName,role.RoleValue
            db.session.add(role)
        db.session.commit()

class Root(db.Model):
    __tablename__ = 'Root'
    RootId = db.Column(db.Integer, primary_key=True)
    RootName = db.Column(db.String(128), unique=True)
    RootAllow = db.Column(db.Boolean, default=False, index=False)
    RoleValue = db.Column(db.Integer,default=Permission.ROOT)
#平台管理者
class Admin(db.Model):
    __tablename__ = 'Admin'
    AdminId = db.Column(db.Integer, primary_key=True)
    AdminName = db.Column(db.String(128), unique=True)
    AdminAllow = db.Column(db.Boolean, default=False, index=False)
    RoleValue = db.Column(db.Integer,default=Permission.ADMIN)

class Service(db.Model):
    __tablename__ = 'Service'
    ServiceId = db.Column(db.Integer, primary_key=True)
    ServiceName = db.Column(db.String(128), unique=True)
    Password = db.Column(db.String(128), unique=True)
    ServiceAllow = db.Column(db.Boolean, default=False, index=False)
    RoleValue = db.Column(db.Integer,default=Permission.SERVICE)
