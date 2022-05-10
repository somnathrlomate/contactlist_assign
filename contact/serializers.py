from rest_framework import serializers
from contact.models import Contact, Group


class ContactSerializer(serializers.ModelSerializer):
	# PrimaryKeyRelatedField

    contact = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
	        model = Contact
            fields = (
		    	'pk',
		    	'name',
		    	'phone_num',
		    	'address',
                )


class GroupSerializer(serializers.ModelSerializer):
	# PrimaryKeyRelatedField
        group = serializers.PrimaryKeyRelatedField(queryset=Contact.objects.all(),many=False)

        class Meta:
	    	model = Group
            fields = (
			    'pk',
			    'name',
			    'contref',
			    )
