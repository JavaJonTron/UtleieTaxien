class Human:
    def __init__(self, age, sex, name, score, is_logged_in):#id Forslag til at hver enkelt person kan ha en ID
        self.age = age
        self.sex = sex
        self.name = name
        self.score = score
        self.is_logged_in = is_logged_in
        #self.id = id


#Forslag til at hver enkelt person kan ha en ID. Da blir det enklere MTP lagring
#1) Da kan vi starte med å laste opp alle brukere fra JSON.
#2) Vi går gjennom dummybrukerne vi skal opprette og sjekker ID,
# samsvarer ID på dummybrukerne med en bruker som er opprettet oppretter vi ikke dummybrukeren.

#
