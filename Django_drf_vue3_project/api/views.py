from django.shortcuts import render
from rest_framework.permissions import BasePermission
from rest_framework import serializers, exceptions
from rest_framework.authentication import BaseAuthentication

from utils.viewsets import ModelViewSet

from api import models

class User(object):
    def __init__(self, name=None, role=None):
        self.name = name
        self.role = role

# 认证组件
class MineAuthentication(BaseAuthentication):
    def authenticate(self, request):
        # 读取用户请求token，校验是否合法
        token = request.query_params.get('token')
        role = request.query_params.get('role')
        if not token:
            raise exceptions.AuthenticationFailed("认证失败")

        # request.user.name
        # request.user.role
        # request.auth
        return (User("xdd", role), None)



    def authenticate_header(self, request):
        return "API"

# 权限校验
class MinePermission(BasePermission):
    def has_permission(self, request, view):
        # print("判断权限", request.user)
        # 1.当前用户所有的权限
        from django.conf import settings
        permission_dict = settings.PERMISSIONS[request.user.role]

        # 2.当前用户正在访问的url和方式
        # print(request.resolver_match.url_name, request.method)
        url_name = request.resolver_match.url_name
        method = request.method

        # 3.权限判断
        method_list = permission_dict.get(url_name)
        if not method_list:
            return False

        if method in method_list:
            return True

        return False

    def has_object_permission(self, request, view, obj):
        # 视图中 self.get_object()
        return True

class DepartSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Depart
        fields = "__all__"

class DepartView(ModelViewSet):
    queryset = models.Depart.objects.all()
    serializer_class = DepartSerializer

    authentication_classes = [MineAuthentication, ]
    permission_classes = [MinePermission, ]


