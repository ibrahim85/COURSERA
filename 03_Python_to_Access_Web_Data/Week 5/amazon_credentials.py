#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Trenton J. McKinney
#
# Created:     26/11/2015
# Copyright:   (c) Trenton J. McKinney 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#Amazon User Credentials for tjm_python_project


def amazon_cred():
    return {"access_key_id": "AKIAJSTPKHNATA5OFVRA",
            "secret_access_key": "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"}



'''
url = "http://webservices.amazon.com/onca/xml?\
       Service=AWSECommerceService\
       &Operation=ItemLookup\
       &ResponseGroup=Large\
       &SearchIndex=All\
       &IdType=ISBN\
       &ItemId=076243631X\
       &AWSAccessKeyId=[Your_AWSAccessKeyID]\
       &AssociateTag=[Your_AssociateTag]\
       &Timestamp=[YYYY-MM-DDThh:mm:ssZ]\
       &Signature=[Request_Signature]"

'''