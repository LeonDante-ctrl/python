class User:
    '''
    generates new instance for user
    '''

    user_list = [] #empty list

    def __init__(self,user_name, password):
        self.user_name = user_name
        self.password = password

    def save_use(self):
        '''
        save_use method saves saves a new user objects to user_list
        '''
        User.user_list.append(self)
