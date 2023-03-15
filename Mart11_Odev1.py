
students={}
# öğrenci ekleme
def add_student(name,surname,index):
    name_surname= name +" "+ surname
    students[name_surname]=index
    return students

add_student("Eda" ,"Toper", 1)
add_student("Derya" ,"Avcı", 2)
add_student("Efe" ,"Aydın", 3)
add_student("Ahmet","Yılmaz",4)
add_student("Mehmet", "Çelik",5)
add_student("Ayşe", "Demir",6)
add_student("Ali", "Aksoy",7)
add_student("Fatma", "Kaya",8)
add_student("Mustafa", "Er",9)
add_student("Zeynep", "Uçar",10)
print(f"öğrenci listesi: {students}")

#öğrenci silme
def remove_student(name, surname):
    name_surname= name +" "+ surname   
    if(name_surname in students):
        print(f"{students[name_surname]} nolu {name_surname} öğrenci listesinden çıkarıldı")
        del students[name_surname]
        
remove_student("Fatma", "Kaya")
print(f"öğrenci listesi: {students}")

#öğrencileri listeleme
def list_student():
    print("\nöğrenci listesi")
    for key, value in students.items():
        print(f" {value}: {key}")

list_student()

#listeden öğrenci bulma
def find_student(name_surname):
    students_iter = iter(students.items())
    while True:
        try:
            key, value = next(students_iter)
            if key == name_surname:
                print(f'{key} öğrencinin numarası: {value}')
                break
        except StopIteration:
            print(f'{name_surname} öğrenci kaydı bulunamadı.')
            break
   

find_student("Ahmet Yılmaz")
find_student("isim soyisim")

#listeden birden fazla öğrenci silme
def remove_multiple_students(*name_surname):
    for name_surname in name_surname:
        if(name_surname in students.keys()):
            remove_student(name_surname.split(" ")[0],name_surname.split(" ")[-1])

remove_multiple_students("Ayşe demir", "Mustafa Er", "Zeynep Uçar")
list_student()

#listeye birden fazla öğrenci ekleme       
def add_multiple_students(*name_surname):
    for i,name_surname in enumerate(name_surname, start=10):
        add_student(name_surname.split(" ")[0],name_surname.split(" ")[-1],i)

add_multiple_students("Ayşe demir", "Mustafa Er", "Zeynep Uçar")
list_student()


