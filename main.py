
#Saya Muhammad Iqbal Rynaldi mengerjakan TP3DPBO2022 untuk mata kuliah DPBO untuk keberkahan-Nya maka saya tidak melakukan kecurangan yang seperti yang telah dispesifikasikan. Aamiin    


from tkinter import *
from tkinter import ttk
import mysql.connector
from PIL import ImageTk, Image
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="db_praktikum"
)

dbcursor = mydb.cursor()

root = Tk()
root.title("Praktikum DPBO")


# Fungsi untuk mengambil data
def getMhs():
    global mydb
    global dbcursor

    dbcursor.execute("SELECT * FROM mahasiswa")
    result = dbcursor.fetchall()

    return result

def getFasilitas():
    global mydb
    global dbcursor

    dbcursor.execute("SELECT * FROM fasilitas_kampus")
    result = dbcursor.fetchall()

    return result


# Window Input Data
def inputs():
    # Hide root window
    global root
    root.withdraw()

    top = Toplevel()
    top.title("Input")
    dframe = LabelFrame(top, text="Input Data Mahasiswa", padx=10, pady=10)
    dframe.pack(padx=10, pady=10)
    # Input 1
    label1 = Label(dframe, text="Nama Mahasiswa").grid(row=0, column=0, sticky="w")
    input_nama = Entry(dframe, width=30)
    input_nama.grid(row=0, column=1, padx=20, pady=10, sticky="w")
    # Input 2
    label2 = Label(dframe, text="NIM").grid(row=1, column=0, sticky="w")
    input_nim = Entry(dframe, width=30)
    input_nim.grid(row=1, column=1, padx=20, pady=10, sticky="w")
    # Input 3
    options = ["Filsafat Meme", "Sastra Mesin", "Teknik Kedokteran", "Pendidikan Gaming"]
    input_jurusan = StringVar(root)
    input_jurusan.set(options[0])
    label4 = Label(dframe, text="Jurusan").grid(row=2, column=0, sticky="w")
    input4 = OptionMenu(dframe, input_jurusan, *options)
    input4.grid(row=2, column=1, padx=20, pady=10, sticky='w')

    # input radio jenis kelamin dan Frame
    input_jenisKelamin = StringVar(root);
    label_jenisKelamin = Label(dframe, text="Jenis Kelamin").grid(row=3, column=0, sticky="w")
    R1_jk = Radiobutton(dframe, text="Laki-Laki", variable = input_jenisKelamin, value="Laki-Laki");
    R2_jk = Radiobutton(dframe, text="Perempuan", variable = input_jenisKelamin, value="Perempuan");
    R1_jk.grid(row=3, column=1)
    R2_jk.grid(row=3, column=2)

    # input radio jenis kelamin dan Frame
    input_hobi = StringVar(root);
    label_hobi = Label(dframe, text="Hobi").grid(row=4, column=0, sticky="w")
    pilihan_hobi = ttk.Combobox(dframe, textvariable = input_hobi,state="readonly")
    pilihan_hobi['values'] = ("Berenang","Makan","Jalan-Jalan","Bermain Game","Olah Raga","Sepak Bola","Bulu Tangkis")
    pilihan_hobi.grid(row=4, column=1)
    pilihan_hobi.current(1) 
    # Button Frame
    frame2 = LabelFrame(dframe, borderwidth=0)
    frame2.grid(columnspan=2, column=0, row=10, pady=10)

    # Submit Button
    btn_submit = Button(frame2, text="Submit Data", anchor="s", command=lambda:[insertData(top, input_nama, input_nim, input_jurusan, input_jenisKelamin, input_hobi), top.withdraw()])
    btn_submit.grid(row=3, column=0, padx=10)

    # Cancel Button
    btn_cancel = Button(frame2, text="Gak jadi / Kembali", anchor="s", command=lambda:[top.destroy(), root.deiconify()])
    btn_cancel.grid(row=3, column=1, padx=10)

# Untuk memasukan data
def insertData(parent, nama, nim, jurusan, jenisKelamin, hobi):
    top = Toplevel()
    # Get data
    nama = nama.get()
    nim = nim.get()
    jurusan = jurusan.get()
    jenisKelamin = jenisKelamin.get()
    hobi = hobi.get()
    if nama != "" and nim != "" and jurusan != "" and jenisKelamin != "" and hobi != "":
        sql = "INSERT INTO `mahasiswa` (`id`, `nim`, `nama`, `jurusan`, `jenis_kelamin`, `hobi`) VALUES (NULL, %s, %s, %s, %s, %s);"
        val = (nim,nama,jurusan,jenisKelamin,hobi)
        dbcursor.execute(sql,val)
        mydb.commit();
        # Input data disini
        btn_ok = Button(top, text="Syap!, Berhasil", anchor="s", command=lambda:[top.destroy(), parent.deiconify()])
        btn_ok.pack(padx=10, pady=10)
        pass
    else:
        # Input data disini
        btn_ok = Button(top, text="Huhu!, Input Jangan Kosong", anchor="s", command=lambda:[top.destroy(), parent.deiconify()])
        btn_ok.pack(padx=10, pady=10)
        pass
  
# Window Semua Mahasiswa
def viewAll():
    global root
    root.withdraw()

    top = Toplevel()
    top.title("Semua Mahasiswa")
    frame = LabelFrame(top, borderwidth=0)
    frame.pack()
    # Cancel Button
    btn_cancel = Button(frame, text="Kembali", anchor="w", command=lambda:[top.destroy(), root.deiconify()])
    btn_cancel.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    # Head title
    head = Label(frame, text="Data Mahasiswa")
    head.grid(row=0, column=1, padx=10, pady=10, sticky="w")

    tableFrame = LabelFrame(frame)
    tableFrame.grid(row=1, column = 0, columnspan=2)

    # Get All Data
    result = getMhs()

    # Title
    title1 = Label(tableFrame, text="No.", borderwidth=1, relief="solid", width=3, padx=5).grid(row=0, column=0)
    title2 = Label(tableFrame, text="NIM", borderwidth=1, relief="solid", width=15, padx=5).grid(row=0, column=1)
    title3 = Label(tableFrame, text="Nama", borderwidth=1, relief="solid", width=20, padx=5).grid(row=0, column=2)
    title4 = Label(tableFrame, text="Jurusan", borderwidth=1, relief="solid", width=20, padx=5).grid(row=0, column=3)
    title5 = Label(tableFrame, text="Jenis Kelamin", borderwidth=1, relief="solid", width=20, padx=5).grid(row=0, column=4)
    title6 = Label(tableFrame, text="Hobi", borderwidth=1, relief="solid", width=20, padx=5).grid(row=0, column=5)

    # Print content
    i = 0
    for data in result:
        label1 = Label(tableFrame, text=str(i+1), borderwidth=1, relief="solid", height=2, width=3, padx=5).grid(row=i+1, column=0)
        label2 = Label(tableFrame, text=data[1], borderwidth=1, relief="solid", height=2, width=15, padx=5).grid(row=i+1, column=1)
        label3 = Label(tableFrame, text=data[2], borderwidth=1, relief="solid", height=2, width=20, padx=5).grid(row=i+1, column=2)
        label4 = Label(tableFrame, text=data[3], borderwidth=1, relief="solid", height=2, width=20, padx=5).grid(row=i+1, column=3)
        label5 = Label(tableFrame, text=data[4], borderwidth=1, relief="solid", height=2, width=20, padx=5).grid(row=i+1, column=4)
        label6 = Label(tableFrame, text=data[5], borderwidth=1, relief="solid", height=2, width=20, padx=5).grid(row=i+1, column=5)
        i += 1

# Dialog konfirmasi hapus semua data
def clearAll():
    top = Toplevel()
    lbl = Label(top, text="Yakin mau hapus semua data?")
    lbl.pack(padx=20, pady=20)
    btnframe = LabelFrame(top, borderwidth=0)
    btnframe.pack(padx=20, pady=20)
    # Yes
    btn_yes = Button(btnframe, text="Gass", bg="green", fg="white", command=lambda:[top.destroy(), delAll()])
    btn_yes.grid(row=0, column=0, padx=10)
    # No
    btn_no = Button(btnframe, text="Tapi boong", bg="red", fg="white", command=top.destroy)
    btn_no.grid(row=0, column=1, padx=10)

# Dialog konfirmasi keluar GUI
def exitDialog():
    global root
    root.withdraw()
    top = Toplevel()
    lbl = Label(top, text="Yakin mau keluar?")
    lbl.pack(padx=20, pady=20)
    btnframe = LabelFrame(top, borderwidth=0)
    btnframe.pack(padx=20, pady=20)
    # Yes
    btn_yes = Button(btnframe, text="Gass", bg="green", fg="white", command=lambda:[top.destroy(), root.destroy()])
    btn_yes.grid(row=0, column=0, padx=10)
    # No
    btn_no = Button(btnframe, text="Tapi boong", bg="red", fg="white", command=lambda:[top.destroy(), root.deiconify()])
    btn_no.grid(row=0, column=1, padx=10)

def delAll():
    top = Toplevel()
    # Delete data disini
    sql = "TRUNCATE `mahasiswa`"
    dbcursor.execute(sql)
    mydb.commit();
    btn_ok = Button(top, text="Zeeb", command=top.destroy)
    btn_ok.pack(pady=20)


def showImage(index = 0):
    result = getFasilitas()
    if(index == 0):
        indexMin = len(result)-1;
        indexPlus = index+1
    elif(index == len(result)-1):
        indexMin = index-1
        indexPlus = 0
    else:
        indexMin = index-1
        indexPlus = index+1

    global root
    root.withdraw()
    top = Toplevel()
    top.title("Semua Fasilitas Kampus")
    frame = LabelFrame(top, borderwidth=0)
    frame.pack()
    size = [255,255]
    img = ImageTk.PhotoImage(Image.open("images/" + result[index][2]).resize(size)) 
    # # Title
    title1 = Label(frame, image=img)
    title1.image = img
    title1.place(x=0, y=0)
    title1.grid(row=1, column=0)

    head = Label(frame, text=result[index][1])
    head.grid(row=2, column=0, padx=10, pady=10, sticky="w")
    
    framebtn = LabelFrame(frame, borderwidth=0)
    framebtn.grid(columnspan=2, column=0, row=3, pady=10)
    
    btn_cancel = Button(framebtn, text="Kembali", anchor="w", command=lambda:[top.destroy(), root.deiconify()])
    btn_cancel.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    
    btn_left = Button(framebtn, text="Left", bg="green", fg="white", command=lambda:[top.destroy(), showImage(indexMin)])
    btn_left.grid(row=0, column=1, padx=10)

    btn_right = Button(framebtn, text="Right", bg="red", fg="white", command=lambda:[top.destroy(), showImage(indexPlus)])
    btn_right.grid(row=0, column=2, padx=10)


# Title Frame
frame = LabelFrame(root, text="Praktikum DPBO", padx=10, pady=10)
frame.pack(padx=10, pady=10)

# ButtonGroup Frame
buttonGroup = LabelFrame(root, padx=10, pady=10)
buttonGroup.pack(padx=10, pady=10)

# Title
label1 = Label(frame, text="Data Mahasiswa", font=(30))
label1.pack()

# Description
label2 = Label(frame, text="Ceritanya ini database mahasiswa ngab")
label2.pack()

# Input btn
b_add = Button(buttonGroup, text="Input Data Mahasiswa", command=inputs, width=30)
b_add.grid(row=0, column=0, pady=5)

# All data btn
b_add = Button(buttonGroup, text="Semua Data Mahasiswa", command=viewAll, width=30)
b_add.grid(row=1, column=0, pady=5)

# All data fasilitas
b_add = Button(buttonGroup, text="Semua Data Fasilitas Kampus", command=showImage, width=30)
b_add.grid(row=2, column=0, pady=5)

# Clear all btn
b_clear = Button(buttonGroup, text="Hapus Semua Data Mahasiswa", command=clearAll, width=30)
b_clear.grid(row=3, column=0, pady=5)

# Exit btn
b_exit = Button(buttonGroup, text="Exit", command=exitDialog, width=30)
b_exit.grid(row=4, column=0, pady=5)

root.mainloop()