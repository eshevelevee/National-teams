import datetime as DT
import re


class Player:
    def __init__(self, fullname, dob):
        self.fullname = fullname
        self.dob = DT.datetime.strptime(dob, '%Y%m%d').date()

    def __repr__(self) -> object:
        return "<{}, {}>".format(self.fullname, self.dob)

    def add_transfermarkt_link(self, transfermarkt_link):
        self.transfermarkt_link = transfermarkt_link
        self.transfermarkt_id = re.search(r"\d+", self.transfermarkt_link).group(0)

    def add_instat_link(self, instat_link):
        self.instat_link = instat_link
        self.instat_id = re.search(r"\d+", self.instat_link).group(0)

