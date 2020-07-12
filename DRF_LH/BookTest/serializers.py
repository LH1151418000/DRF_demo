"""
DRF模型类序列化器
    自动从模型类中把字段映射到序列化器中，自动设置约束条件
    重写create和update方法
"""

from rest_framework import serializers
from .models import *


class BookInfoModelSerializer(serializers.ModelSerializer):

    heros = serializers.StringRelatedField(many=True, required=False)

    # 手动定义字段，会覆盖自动映射对字段
    btitle = serializers.CharField(min_length=2, max_length=20, required=True)

    class Meta:
        model = BookInfo
        # fields = '__all__'  # 映射所有字段
        fields = ['btitle', 'bpub_date', 'bread', 'heros']  # 映射指定字段
        # exclude = ['image']  # 映射除此字段

        # 对模型类序列化器自动构建对约束条件进行修订
        extra_kwargs = {
            'bread': {'min_value': 0},
            # 'heros': {'required': False}
            # 'required': True
        }

        # 批量设置字段read_only = True
        # read_only_fields = ['id', 'bread']


class HeroInfoModelSerializer(serializers.ModelSerializer):

    # 关联对象对主键隐藏字段不会被自动映射
    # book_id = serializers.IntegerField()

    class Meta:

        model = HeroInfo
        fields = '__all__'
