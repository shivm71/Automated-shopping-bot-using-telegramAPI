from datetime import datetime

class telegram:
    def __init__(self,client,col):
        self.client = client
        self.col = col
        pass


    def insert_user_to_db(self,user): 
        try:
            date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            # gender = requests.get("https://api.genderize.io/?name={}".format(user.first_name)).json()
            # user.first_name
            x = self.col.insert_one(
            {   
                "telegram_id":user.id,
                "telegram_username":user.username,
                "userinfo":{
                            "firstname":user.first_name,
                            "lastname":user.last_name,
                            "email":user.email,
                            "gender":"",
                            "age":"",
                            "mobile_no":user.phone,
                            "pref_cat":[]
                            },
                "created":date,
                "updated":date,
                "access_hash":user.access_hash,
                "invite_status":False,
                "membership_status":False,
            })
            return True
        except Exception as e:
            print('Not able to insert into mongo, Exception:',e)
            return False


    async def insert_user_from_group(self,group_id,limit):
        count = 0
        try:  
            async for user in self.client.iter_participants(group_id,limit=limit,aggressive=True):
                if self.insert_user_to_db(user):
                    count+=1
                pass        
        except:
            print(group_id)
            errorgroup = await self.client.get_entity(group_id)  
            print(errorgroup.stringify()) 
        print(count,"- unique users are inserted from group")                        


                
