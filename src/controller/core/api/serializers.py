from rest_framework import serializers

from core.models import Server


class ServerSerializer(serializers.ModelSerializer): # forms.ModelForm
    url         = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Server
        fields = [
            'url',
            'id',
            'hostname',
            'ipadress',
            'os',
            'timestamp',
        ]
        read_only_fields = ['id']

    # converts to JSON
    # validations for data passed

    def get_url(self, obj):
        # request
        request = self.context.get("request")
        return obj.get_api_url(request=request)

    def validate_title(self, value):
        qs = Server.objects.filter(title__iexact=value) # including instance
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("This title has already been used")
        return value