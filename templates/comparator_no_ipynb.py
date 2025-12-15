import pandas as pd
import numpy as np

class Tables_comparator:
    def __init__(self,df_book_table01,df_book_table02):
        self.df_book_table01=df_book_table01
        self.df_book_table02=df_book_table02
             
    def comparator(df_book_table01,df_book_table02):
        num_filas_table01=int(df_book_table01.shape[0])
        num_filas_table02=int(df_book_table02.shape[0])       
        cont=0
        df_aux=pd.DataFrame()        
        list_field01=[]
        list_field02=[]
        list_field03=[]
        list_field04=[]       
        #print("df_book_table01[8,0]: ",df_book_table01.iloc[8,0]) #UnitsByDealer.csv_r.csv
        #print("df_book_table02[8,5]: ",df_book_table02.iloc[8,5]) #6MB.        
        print("\nInformación de las tablas: ")
        print("\nTabla 1:")
        print(df_book_table01.info())
        print("\nTabla 2:")
        print(df_book_table02.info())
        attribute_name_table01=input("\nDigita el atributo a comparar de la tabla 1: ")
        attribute_name_table02=input("Digita el atribito a comparar de la tabla 2: ")
        position_table01=int(df_book_table01.columns.get_loc(attribute_name_table01))
        position_table02=int(df_book_table02.columns.get_loc(attribute_name_table02))
        print("\nAtributo de la tabla1: ",position_table01)
        print("Atributo de la tabla2: ",position_table02,"\n")
        print("Trabajando...")
                          
        for i in range(0,num_filas_table01):
            for j in range(0,num_filas_table02):
                #if str(df_book_table01.iloc[i,5])==str(df_book_table02.iloc[j,3]): 
                if str(df_book_table01.iloc[i,position_table01])==str(df_book_table02.iloc[j,position_table02]):                                                                             
                    list_field01.append(df_book_table02.iloc[j,3])
                    list_field02.append(df_book_table02.iloc[j,2])
                    list_field03.append(df_book_table02.iloc[j,4])
                    list_field04.append(df_book_table02.iloc[j,1])
                    print("df_book_table01[i,position_table01]: ",df_book_table01.iloc[i,position_table01]," = ",end="")
                    print("df_book_table02[j,position_table02]: ",df_book_table02.iloc[j,position_table02])               
                    cont=cont+1
        df_aux['FIELD01']=list_field01
        df_aux['FIELD02']=list_field02
        df_aux['FIELD03']=list_field03
        df_aux['FIELD04']=list_field04
        print("Cont= ",cont)
        print(df_aux.info())
        option_exp=input("\n¿Desea generar un reporte de coincidencias en formato csv S/N?\n")
        if option_exp=="S":
            df_aux.to_csv('./reports/tables_comparator_coincident.csv')
        cont=0
        option_exp=input("¿Desea generar un reporte de diferencias en formato csv S/N?\n")        
        df_book_table02['ACTION']="Keep"
        if option_exp=="S":
            print("Trabajando...")
            for i in range(0,num_filas_table01):
                for j in range(0,num_filas_table02):
                    if str(df_book_table01.iloc[i,position_table01])==str(df_book_table02.iloc[j,position_table02]):
                        df_book_table02.iloc[j,5]=np.nan
                        print("df_book_table01[i,position_table01]: ",df_book_table01.iloc[i,position_table01]," = ",end="")
                        print("df_book_table02[j,position_table02]: ",df_book_table02.iloc[j,position_table02])               
            df_book_table02.dropna(axis=0,inplace=True)
            #print(df_book_table02)
            df_book_table02.to_csv("./reports/tables_comparator_differences.csv")

        #lista_combinada=[lista_simcard,lista_linea]