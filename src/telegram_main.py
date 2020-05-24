class telegram:
    def __init__(self,client,col):
        self.client = client
        self.col = col
        pass

    # async def insert_user_from_group(self,group_id,limit):
    #     count = 0
    #     try:
    #         async for user in self.client.iter_participants(group_id,limit=limit,aggressive=True):
    #             print(user.id)
    #             if not hasattr(user,'email'):
    #                user.email = None
    #             if db.insert_user_to_db(self.col,user):
    #                 count+=1
    #             pass
    #     except Exception as e:
    #         print("Exception in fetching users from group:",group_id ,"session name:", self.client.session.filename)
    #     print(count,"- unique users are inserted from group")


                
