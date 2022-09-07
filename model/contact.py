from sys import maxsize


class Contact:
    def __init__(self, firstname = None, middlename = None, lastname = None, nickname = None, title = None, company = None, address = None, home_phone = None, cell_phone = None,
                 work_phone = None, fax = None, email_1 = None, email_2 = None, email_3 = None, homepage = None, day = None, month = None, year = None, a_day = None,
                 a_month = None, a_year = None, address2 = None, secondary_phone = None, notes = None, id = None, all_phones = None, all_mails = None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home_phone = home_phone
        self.cell_phone = cell_phone
        self.work_phone = work_phone
        self.fax = fax
        self.email_1 = email_1
        self.email_2 = email_2
        self.email_3 = email_3
        self.homepage = homepage
        self.day = day
        self.month = month
        self.year = year
        self.a_day = a_day
        self.a_month = a_month
        self.a_year = a_year
        self.address2 = address2
        self.secondary_phone = secondary_phone
        self.notes = notes
        self.id = id
        self.all_phones = all_phones
        self.all_mails = all_mails

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.lastname, self.firstname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and \
               (self.lastname is None or other.lastname is None or self.lastname == other.lastname) and \
               (self.firstname is None or other.firstname is None or self.firstname == other.firstname)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize


