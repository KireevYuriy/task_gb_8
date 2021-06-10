import re

mail = 'abc_D.f123g@gmail.com'
# mail = 'someone@geekbrainsru'
# mail = '@gmail.com'
# mail = '1@.ru'


def email_parse(email_address):

    email_dict = {}
    re_name = re.compile(r'^[\w/.-]+[^@]')
    re_domain = re.compile(r'@[^@]+\.[^@]+')
    name = re_name.findall(mail)
    domain = re_domain.findall(mail)
    if name != [] and domain != []:
        for val_first, val_second in zip(name, domain):
            email_dict['username'] = val_first
            email_dict['domain'] = val_second[1:]
    else:
        raise ValueError(f'Некорректное значение email: {email_address}')
    return email_dict


print(email_parse(mail))
