# contact = {}
# while True:
#     choice = int(input("1.Add new contact \n 2. Search contact \n 3. Display contact \n 4. Edit contact \n 4. Exit"))
#     if choice == 1:
#         name = input("enter the contact name")
#         phone = input("enter the mobile number")
#         contact[name] = phone
#     elif choice == 2:
#         search_name = input("enter the contact name")
#         if search_name in contact:
#             print(search_name," ' s contact number is", contact[search_name])
#         else:
#             print("Name is not found in contact book")