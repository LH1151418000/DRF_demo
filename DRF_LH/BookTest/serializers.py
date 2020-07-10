from rest_framework import serializers


class HeroInfoSerializer2(serializers.Serializer):
    """英雄数据序列化器"""
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female')
    )
    id = serializers.IntegerField(label='ID', read_only=True)
    hname = serializers.CharField(label='名字', max_length=20)
    hgender = serializers.ChoiceField(choices=GENDER_CHOICES, label='性别', required=False)


class BookInfoSerializer(serializers.Serializer):
    btitle = serializers.CharField()
    bpub_date = serializers.CharField()
    bread = serializers.IntegerField()
    bcomment = serializers.IntegerField()
    is_delete = serializers.BooleanField()
    image = serializers.CharField()
    # heros = serializers.PrimaryKeyRelatedField(read_only=True,many=True)
    # heros = serializers.StringRelatedField(many=True)
    # 嵌套序列化器
    heros = HeroInfoSerializer2(many=True)


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
    # hbook = serializers.PrimaryKeyRelatedField(read_only=True)
    hbook = serializers.StringRelatedField(read_only=True)
