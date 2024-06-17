# myapp/serializers.py

from rest_framework import serializers

class B2CRequestSerializer(serializers.Serializer):
    CommandID = serializers.CharField(max_length=50)
    OriginatorConversationID = serializers.CharField(max_length=50)
    ThirdPartyID = serializers.CharField(max_length=50)
    Password = serializers.CharField(max_length=100)
    ResultURL = serializers.URLField()
    Timestamp = serializers.CharField(max_length=14)
    Identifier = serializers.CharField(max_length=50)
    SecurityCredential = serializers.CharField(max_length=100)
    ShortCode = serializers.CharField(max_length=10)
    ReceiverIdentifier = serializers.CharField(max_length=50)
    Amount = serializers.CharField(max_length=10)
    Currency = serializers.CharField(max_length=3)
    ReasonType = serializers.CharField(max_length=20)
    Comment = serializers.CharField(max_length=100)
