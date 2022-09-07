from random import randrange
import re


def test_info_on_home_page(app):
    index = randrange(app.contact.count())
    contact_info_from_home_page = app.contact.get_contact_list()[index]
    contact_info_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_info_from_home_page.all_phones == \
           app.contact.merge_info_like_on_home_page(contact_info_from_edit_page, 'phone')
    assert contact_info_from_home_page.all_mails == \
           app.contact.merge_info_like_on_home_page(contact_info_from_edit_page, 'mail')
    assert contact_info_from_home_page.address == contact_info_from_edit_page.address
    assert contact_info_from_home_page.firstname == contact_info_from_edit_page.firstname
    assert contact_info_from_home_page.lastname == contact_info_from_edit_page.lastname


# def clear(s):
#     return re.sub("[() -]", "", s)
#
#
# def merge_info_like_on_home_page(contact, info_type):
#
#     if info_type == 'mail':
#         return "\n".join(filter(lambda x: x != "",
#                                 map(lambda x: clear(x),
#                                     filter(lambda x: x is not None,
#                                            [contact.email_1, contact.email_2, contact.email_3]))))
#
#     return "\n".join(filter(lambda x: x != "",
#                 map(lambda x: clear(x),
#                     filter(lambda x: x is not None,
#                            [contact.home_phone, contact.cell_phone, contact.work_phone, contact.secondary_phone]))))


