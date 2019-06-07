from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = ('id', 'text', 'created', 'updated', )
		read_only_fields = ('id', 'active', 'created', 'updated', )
