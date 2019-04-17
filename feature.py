def feature3(args1, args2, diction = None):
        dictionary = dict(zip(args1, args2))
        if isinstance(diction, dict):
            dictionary={**dictionary,**diction}
        return dictionary
