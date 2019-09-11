class Contact:
    def __init__(self, name, e_mail):
        self.name = name
        self.e_mail = e_mail
    def print_contact(self):
        print("name:", self.name)
        print("e_mail:", self.e_mail)

def show_contact(contact_list):
    for i in contact_list:
        i.print_contact()

def contact_add():
    name = input("name: ")
    e_mail = input("e_mail:")
    contact = Contact(name, e_mail)
    return contact

def delete_contact(contact_list, name):
    for i, contact in enumerate(contact_list):
        if contact.name == name:
            del contact_list[i]

def write_contact(contact_list):
    f = open("contact.txt", "wt", encoding="utf-8")
    for i in contact_list:
        f.write(i.name + '\n')
        f.write(i.e_mail + '\n')
    f.close()

def show_menu():
    print("1.연락처 추가")
    print("2.연락처 출력")
    print("3.연락처 삭제")
    print("4.종료")
    menu = input("메뉴선택: ")
    menu = int(menu)
    return menu

def main():
    contact_list = []
    while True:
        menu = show_menu()
        if menu == 1:
            contact = contact_add()
            contact_list.append(contact)
        elif menu == 2:
            show_contact(contact_list)
        elif menu == 3:
            name = input("name: ")
            delete_contact(contact_list, name)
        elif menu == 4:
            write_contact(contact_list)
            break
        else:
            print("잘못 입력하셨습니다.다시 입력하세요")

if __name__ == '__main__':
    main()


