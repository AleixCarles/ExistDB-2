import Tkinter as tk
from Tkconstants import END

from eulexistdb import db

EXISTDB_SERVER_USER = 'admin'
EXISTDB_SERVER_PASSWORD = ''
EXISTDB_SERVER_URL = "http://localhost:8080/exist"
EXISTDB_ROOT_COLLECTION = "/mp03uf6"
db = db.ExistDB(server_url=EXISTDB_SERVER_URL, username='admin', password='')
window = tk.Tk()
window.title('AleixC')


def insereixNode():
    try:
        lbl_principal.delete('0.0', END)
        query = """update insert\n
  <treballador>
    <departament>{0}</departament>
    <dni>{1}</dni>
    <nom>{2}</nom>
    <cognom>{3}</cognom>
    <telefon>{4}</telefon>
    <mail>{5}</mail>
    <sou>{6}</sou>
  </treballador>
 into //personal""".format(ent_departament.get(), ent_dni.get(), ent_nom.get(), ent_cognom.get(), ent_telefon.get(),
                           ent_mail.get(), ent_sou.get())
        db.executeQuery(query)
        print query
    except (Exception) as error:
        lbl_principal.insert('0.0', "T'has equivocat amb algun parametre")


def eliminarNode():
    try:
        lbl_principal.delete('0.0', END)
        query = """update delete //treballador[dni='{0}']""".format(ent_dni.get())
        db.executeQuery(query)
        print query
    except (Exception) as error:
        lbl_principal.insert('0.0', "T'has equivocat amb algun parametre")


def modificarNode():
    try:
        lbl_principal.delete('0.0', END)
        query = """update replace //treballador[dni='{1}']\n
         with <treballador>
            <departament>{0}</departament>
            <dni>{1}</dni>
            <nom>{2}</nom>
            <cognom>{3}</cognom>
            <telefon>{4}</telefon>
            <mail>{5}</mail>
            <sou>{6}</sou>
          </treballador>""".format(ent_departament.get(), ent_dni.get(), ent_nom.get(), ent_cognom.get(),
                                   ent_telefon.get(),
                                   ent_mail.get(), ent_sou.get())
        db.executeQuery(query)
        print query
    except (Exception) as error:
        lbl_principal.insert('0.0', "T'has equivocat amb algun parametre")


def mostrarNodeUn():
    try:
        lbl_principal.delete('0.0', END)
        query = """/personal/treballador[dni='{0}']""".format(ent_dni.get())
        res = db.executeQuery(query)
        hits = db.getHits(res)
        text = ""
        for i in range(hits):
            text += str(db.retrieve(res, i)) + "\n"
        lbl_principal.insert('0.0', text)
        print(text)
    except (Exception) as error:
        lbl_principal.insert('0.0', "T'has equivocat amb la busqueda")


def mostrarNodeTots():
    try:
        lbl_principal.delete('0.0', END)
        query = """/personal/treballador"""
        res = db.executeQuery(query)
        hits = db.getHits(res)
        text = ""
        for i in range(hits):
            text += str(db.retrieve(res, i)) + "\n"
        lbl_principal.insert('0.0', text)
        print(text)
    except (Exception) as error:
        lbl_principal.insert('0.0', "T'has equivocat amb la busqueda")

def assginarSou():
    try:
        lbl_principal.delete('0.0', END)
        query = """update value /personal/treballador[departament='{0}']/sou
with '{6}'""".format(ent_departament.get(), ent_dni.get(), ent_nom.get(), ent_cognom.get(),
                                   ent_telefon.get(),
                                   ent_mail.get(), ent_sou.get())
        db.executeQuery(query)
        print query
    except (Exception) as error:
        lbl_principal.insert('0.0', "T'has equivocat amb algun parametre")
def augmentarSou():
    try:
        lbl_principal.delete('0.0', END)
        query = """/personal/treballador[departament='{0}']/sou/text()""".format(ent_departament.get())
        db.executeQuery(query)
        query="""update value SUM(/personal/treballador[departament='{0}']/sou'{6}') """.format(ent_departament.get(), ent_dni.get(), ent_nom.get(), ent_cognom.get(),
                                   ent_telefon.get(),
                                   ent_mail.get(), ent_sou.get())
        res = db.executeQuery(query)
        hits = db.getHits(res)
        text = ""
        for i in range(hits):
            text += str(db.retrieve(res, i)) + "\n"
            texti=int(text)
            text=str(texti)
        lbl_principal.insert('0.0', text)
        print(text)
    except (Exception) as error:
        lbl_principal.insert('0.0', "T'has equivocat amb algun parametre")

# Labels
lbl_principal = tk.Text(master=window )
lbl_departament = tk.Label(master=window, text="Departament", )
lbl_dni = tk.Label(master=window, text="DNI", )
lbl_nom = tk.Label(master=window, text="Nom", )
lbl_cognom = tk.Label(master=window, text="Cognom", )
lbl_telefon = tk.Label(master=window, text="Telefon", )
lbl_mail = tk.Label(master=window, text="Mail", )
lbl_sou = tk.Label(master=window, text="Sou", )

# Entrys
ent_departament = tk.Entry(master=window, width="80")
ent_dni = tk.Entry(master=window, width="80")
ent_nom = tk.Entry(master=window, width="80", )
ent_cognom = tk.Entry(master=window, width="80")
ent_telefon = tk.Entry(master=window, width="80")
ent_mail = tk.Entry(master=window, width="80")
ent_sou = tk.Entry(master=window, width="80")
# Botons
btn_insertar = tk.Button(master=window, text="Insertar", command=insereixNode,width="15")
btn_eliminar = tk.Button(master=window, text="Eliminar", command=eliminarNode,width="15")
btn_modificar = tk.Button(master=window, text="Modificar", command=modificarNode,width="15")
btn_mostrar = tk.Button(master=window, text="Mostrar 1", command=mostrarNodeUn,width="15")
btn_llistar_tot = tk.Button(master=window, text="Mostrar tot", command=mostrarNodeTots,width="15")
btn_assigna_sou = tk.Button(master=window, text="Assignar sou", command=assginarSou,width="15")
btn_augmentar_sou = tk.Button(master=window, text="Augnmentar sou", command=augmentarSou,width="15")

# Enters i labels
lbl_departament.grid(row=0, column=0)
ent_departament.grid(row=0, column=1)

lbl_dni.grid(row=1, column=0)
ent_dni.grid(row=1, column=1)

lbl_nom.grid(row=2, column=0)
ent_nom.grid(row=2, column=1)

lbl_cognom.grid(row=3, column=0)
ent_cognom.grid(row=3, column=1)

lbl_telefon.grid(row=4, column=0)
ent_telefon.grid(row=4, column=1)

lbl_mail.grid(row=5, column=0)
ent_mail.grid(row=5, column=1)

lbl_sou.grid(row=6, column=0)
ent_sou.grid(row=6, column=1)

# Botons
btn_insertar.grid(row=0, column=2, sticky="W")
btn_eliminar.grid(row=1, column=2, sticky="W")
btn_modificar.grid(row=2, column=2, sticky="W")
btn_mostrar.grid(row=3, column=2, sticky="W")
btn_llistar_tot.grid(row=4, column=2, sticky="W")
btn_assigna_sou.grid(row=5, column=2, sticky="W")
btn_augmentar_sou.grid(row=6, column=2, sticky="W")

# Label principal
lbl_principal.grid(row=7, column=1, sticky="W")

window.mainloop()
