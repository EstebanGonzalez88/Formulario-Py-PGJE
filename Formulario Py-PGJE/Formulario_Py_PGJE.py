## 2NLIDTS-EstebanGonzalez-03python
## Formulario de registro PY

## Almacenamiento en TXT
import tkinter as tk
from tkinter import messagebox

## Definicion de funciones
def Limpiar_campos():
    txtNombre.delete(0, tk.END)
    txtApellidos.delete(0, tk.END)
    txtEdad.delete(0, tk.END)
    txtEstatura.delete(0, tk.END)
    txtTelefono.delete(0, tk.END)
    var_genero.set(0)
    
def borrar_fun():
    Limpiar_campos
    
def guardar_valores():
    #Obtener valores desde los Entrys
    nombres = txtNombre.get()
    apellidos = txtApellidos.get()
    edad = txtEdad.get()
    estatura = txtEstatura.get()
    telefono = txtTelefono.get()
    #obtener el genero de los RadioButtons
    genero= ""
    if var_genero.get()==1:
        genero = "Hombre"
    elif var_genero.get()==2:
        genero = "Mujer"
        
    ## Generar la cadena de Caracteres 
    datos = "Nombres: " + nombres + "\n" + "Apellidos: " +  apellidos + "\n" + "Edad: "+ edad + "anos\n" + "\n" + "Estatura: " + estatura + "\n" + "Telefono: " + telefono + "\n" + "Genero: "+ genero + "\n"

    ## Guardar los datos en el archivo TXT
    with open ("abcdef.txt", "a") as archivo:
        archivo.write(datos+ "\n\n")

    ## Mostrar Mensaje de confirmacion
    messagebox.showinfo("Informacion", "Datos Guardados Con Exito: \n\n" + datos)
    txtNombre.delete(0, tk.END)
    txtApellidos.delete(0, tk.END)
    txtEdad.delete(0, tk.END)
    txtEstatura.delete(0, tk.END)
    txtTelefono.delete(0, tk.END)
    var_genero.set(0)

## Creación de Ventana 
ventana = tk.Tk()
ventana.geometry("500x480")
ventana.title("Formulario De Esteban")

## Crear variable para RadioButton
var_genero = tk.IntVar()

## Creación de etiquetas y campos de entrada
lblNombre = tk.Label(ventana, text = "Nombres: ")
lblNombre.pack()
txtNombre = tk.Entry()
txtNombre.pack()
lblApellidos = tk.Label(ventana, text= "Apellidos: ")
lblApellidos.pack()
txtApellidos = tk.Entry()
txtApellidos.pack()
lblTelefono = tk.Label(ventana, text = "Telefono: ")
lblTelefono.pack()
txtTelefono = tk.Entry()
txtTelefono.pack()
lblEdad = tk.Label(ventana, text= "Edad: ")
lblEdad.pack()
txtEdad = tk.Entry() 
txtEdad.pack()
lblEstatura = tk.Label(ventana, text= "Estatura: ")
lblEstatura.pack()
txtEstatura = tk.Entry()
txtEstatura.pack()
lblGenero = tk.Label(ventana, text= "Genero: ")
lblGenero.pack()

rbtHombre = tk.Radiobutton(ventana, text= "Hombre", variable=var_genero, value=1)
rbtHombre.pack()
rbtMujer = tk.Radiobutton(ventana, text= "Muejer", variable=var_genero, value=2)
rbtMujer.pack()

## Creación de Botones
btnBorrar = tk.Button(ventana, text = "Borrar valores", command=borrar_fun)
btnBorrar.pack()
btnGuardar = tk.Button(ventana, text= "Guardar valores", command=guardar_valores)
btnGuardar.pack()
## Ejecución de Ventana
ventana.mainloop()
