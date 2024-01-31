import time
import pandas as pd

from degiskenler import *


""" bu script de excel ve csv üzerinden veriler aktarılır,
    veriler filtreleme için düzenlenir ve son açamaya getirilir.."""

def vardiyalar(): # Vardiyaları excelden alıp liste döndürür
    data = pd.read_excel(vardiya_excel, sheet_name=excel_sayfa)
    liste = [ i  for i in data["Vardiya Açıklama"]]
    return liste

def csv_transfer(): # csv dosyasını alıp dataframe döndürür
    data = pd.read_csv(puantaj, sep=";")
    transfer = pd.DataFrame(data=data)
    return transfer

def dataframe_düzenleme(): # dataframe üzerinde düzenlemeler yapar ve güncel dataframe i döndürür
    data = csv_transfer()
    df1 = pd.DataFrame(data=data)
    df1["Günler"] = ""
    df1["Notlar"] = ""
    df = df1.dropna(subset=["AltFirma"])
    return df

def vardiya_kontrol(): # dataframe üzerinde mesai çaklamalarına göre günler sütununa yeni değerler döndürür
    vardiya_liste = vardiyalar()
    df = dataframe_düzenleme()

    mesai_açıklama = [i for i in df["Mesai Açıklama"]]
    vardiya_aktarım = [i for i in vardiya_liste]
    liste3 = []
    for i in range(len(mesai_açıklama)):
        eşleşme_var = False
        for x in range(len(vardiya_aktarım)):
            if mesai_açıklama[i] == vardiya_aktarım[x]:
                liste3.append("Haftasonu")
                eşleşme_var = True
                break
        if not eşleşme_var:
            liste3.append("Haftaiçi")
    return liste3


def main():

    df = dataframe_düzenleme()
    df["Günler"] = vardiya_kontrol()

    return df




