import abc

class State(abc.ABC):

    def __init__(self, name, user):

        self.doc = None

        self.user = user

        self.status = name

    @abc.abstractmethod
    def render(self):

        pass

    @abc.abstractmethod
    def publish(self):

        pass

class Draft(State):

    def __init__(self, name, user):

        super().__init__(name, user)

    def render(self):

        if(self.user.isAdmin or self.user.isAuthor):

            print("DraftState rended the document.")

        else:

            print("Error")

            self.doc.statechange(Forbidden("ForbiddenState", self.user))
    
    def publish(self):

        if(self.user.isAdmin):

            print("Admin published the document.")

            print("Document changed to PublishedState.")

            self.doc.statechange(Published("PublishedState", self.user))

    
        else:

            print("User published the document.")

            print("Document changed to ModerationState.")

            self.doc.statechange(Moderation("ModerationState", self.user))

class Moderation(State):

    def __init__(self, name, user):

        super().__init__(name, user)

    def render(self):

        pass
    
    def publish(self):

        if(self.user.isApproved):

            print("Admin approoved the document.")

            print("Document changed to PublishedState.")

            self.doc.statechange(Published("PublishedState", self.user))
    
        else:

            print("Review failed.")

            print("Document changed to DraftState.")

            self.doc.statechange(Draft("DraftState", self.user))

class Published(State):

    def __init__(self, name, user):

        super().__init__(name, user)

    def render(self):

        pass
    
    def publish(self):

        if(self.user.isExpired):

            print("Publication expired.")

            print("Document changed to DraftState.")

            self.doc.statechange(Draft("DraftState", self.user))
    
        else:

            print("Document Publishment Completed.")

class Forbidden(State):

    def __init__(self, name, user):

        super().__init__(name, user)

    def render(self):

        pass
    
    def publish(self):

        pass

class Document:

    def __init__(self, state, user):

        self.state = state

        self.state.doc = self

        self.state.user = user

        self.state.render()

        self.state.publish()

    def statechange(self, newstate):

        self.state = newstate

        self.state.doc = self

        if(newstate.status == "DraftState"):

            print("Returned to the initial DraftState.")

        self.state.render()

        self.state.publish()

class User:

    def __init__(self, isAdmin, isAuthor, isApproved, isExpired):

        self.isAdmin = isAdmin

        self.isAuthor = isAuthor

        self.isApproved = isApproved
        
        self.isExpired = isExpired

user = User(True, False, True, False)

document = Document(Draft("DraftState", user), user)