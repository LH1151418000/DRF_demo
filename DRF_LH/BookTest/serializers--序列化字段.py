from rest_framework import serializers
from .models import *


class HeroInfoSerializer2(serializers.Serializer):
    """英雄数据序列化器"""
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female')
    )
    id = serializers.IntegerField(label='ID', read_only=True)
    hname = serializers.CharField(label='名字', max_length=20)
    hgender = serializers.ChoiceField(choices=GENDER_CHOICES, label='性别', required=False)


def validators_btitle(value):

    if 'django' not in value:
        raise serializers.ValidationError('这不是一本关于Django的书')


class BookInfoSerializer(serializers.Serializer):
    # 全局  自定义校验函数
    # btitle = serializers.CharField(validators=[validators_btitle])
    btitle = serializers.CharField()
    bpub_date = serializers.DateField()
    bread = serializers.IntegerField(required=False)
    bcomment = serializers.IntegerField(required=False)
    is_delete = serializers.BooleanField(required=False)
    image = serializers.CharField(required=False)
    # heros = serializers.PrimaryKeyRelatedField(read_only=True,many=True)
    # heros = serializers.StringRelatedField(many=True)
    # 嵌套序列化器
    # heros = HeroInfoSerializer2(many=True)

    # 类中自定义函数校验
    # def validate_btitle(self, value):
    #     if 'django' not in value:
    #         raise serializers.ValidationError('这不是一本关于Django的书')
    #     return value

    def validate(self, attrs):

        btitle = attrs.get('btitle')
        if 'django' not in btitle:
            raise serializers.ValidationError('这不是一本关于Django的书')
        return attrs

    # 新建资源
    def create(self, validated_data):
        """

        :param validated_data: 校验后的有效数据
        :return:
        """
        instance = BookInfo(
            btitle=validated_data.get('btitle'),
            bpub_date=validated_data.get('bpub_date')
        )
        instance.save()
        return instance

    # 反序列化更新
    def update(self, instance, validated_data):
        """

        :param instance:被更新的模型类对象
        :param validated_data:有效数据
        :return:
        """
        btitle = validated_data.get('btitle')
        instance.btitle = btitle
        instance.save()
        return instance


class HeroInfoSerializer(serializers.Serializer):
    """英雄数据序列化器"""
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female')
    )
    id = serializers.IntegerField(label='ID', read_only=True)
    hname = serializers.CharField(label='名字', max_length=20)
    hgender = serializers.ChoiceField(choices=GENDER_CHOICES, label='性别', required=False)
    hcomment = serializers.CharField(label='描述信息', max_length=200, required=False, allow_null=True)
    is_delete = serializers.BooleanField()

    hbook = serializers.PrimaryKeyRelatedField(
        queryset=BookInfo.objects.all()
    )
    # hbook = serializers.StringRelatedField(read_only=True)
