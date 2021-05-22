import csv
def write_into_csv(info_list):
    with open('student_info.csv','a',newline='') as csv_file:
        writer=csv.writer(csv_file)
        if csv_file.tell()==0:
            writer.writerow(["Name","Age","contactNo.","Email_Id"])
        writer.writerow(info_list)
if __name__=='__main__':
    condition=True
    student_no=1
    while condition:
        student_info=input(f"Enter details of student#{student_no} in the following format (Name Age ContactNo. Email_Id): ")
        student_info_list=student_info.split(' ')
        print(f"The Entered information is-\nName:{student_info_list[0]}\nAge:{student_info_list[1]}\nContact_No.:{student_info_list[2]}\nEmail_Id:{student_info_list[3]}")
        choice_check=input("is entered information is correct{yes/no}?: ")
        if choice_check=="yes":
            write_into_csv(student_info_list)
            condition_check=input("enter yes/no if you want to add details of other student: ")
            if condition_check=="yes":
                condition=True
                student_no+=1
            else:
                condition=False
        elif choice_check=="no":
            print("Re-enter the details correctly:")
