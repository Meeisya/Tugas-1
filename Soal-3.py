print ("program menentukan kelulusan")
print ('============================')
nilai_ujian_teori=input("masukkan nilai ujian teori")
nilai_ujian_praktek=input("masukkan nilai ujian praktek")
if (nilai_ujian_teori == 70 and nilai_ujian_praktek == 70):
    print("Selamat, Anda Lulus Ujian");
elif(nilai_ujian_teori == 70 and nilai_ujian_praktek < 70):
    print("Anda harus mengulang Ujian Praktek"); 
elif(nilai_ujian_teori < 70 and nilai_ujian_praktek == 70):
    print("Anda harus mengulang ujian teori");
elif(nilai_ujian_praktek < 70):
    print("Anda harus mengulang ujian teori dan praktek");
elif(nilai_ujian_teori < 70):
    print("Anda harus mengulan ujian teori dan praktek"); 
                    