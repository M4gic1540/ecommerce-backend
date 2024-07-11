from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'password', 'email', 'nombre', 'apellido', 'is_active', 'is_staff']
        extra_kwargs = {
            'password': {'write_only': True},  # Para que la contraseña no se muestre en las respuestas API
        }

    def create(self, validated_data):
        usuario = Usuario.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            nombre=validated_data['nombre'],
            apellido=validated_data['apellido'],
            is_active=validated_data.get('is_active', True),
            is_staff=validated_data.get('is_staff', False),
        )
        usuario.set_password(validated_data['password'])  # Configura la contraseña cifrada
        usuario.save()
        return usuario

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.apellido = validated_data.get('apellido', instance.apellido)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.is_staff = validated_data.get('is_staff', instance.is_staff)

        if 'password' in validated_data:
            instance.set_password(validated_data['password'])  # Configura la nueva contraseña cifrada
        
        instance.save()
        return instance
