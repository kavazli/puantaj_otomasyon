import time
import pandas as pd

import puantaj
import degiskenler

""" bu script veriler koşullar özelinde özetlenir ve ,
    gerekli yerlere mail atılmak üzere yeni bir kontrol exceli oluşturulur.."""

def kosul_1():
    df = puantaj.main()
    kosul1 = ((df["Günler"] == "Haftaiçi") & df["Giriş"].isna() & df["Çıkış"].isna() &  df["İzin Açıklama"].isna())
    df.loc[kosul1, "Notlar"] = degiskenler.açıklama_1
    liste1 = df[kosul1]
    return liste1

def kosul_2():
    df = puantaj.main()
    kosul2 = ((df["Günler"] == "Haftaiçi") & df["Giriş"].notna() & df["Çıkış"].isna())
    df.loc[kosul2, "Notlar"] = degiskenler.açıklama_2
    liste2 = df[kosul2]
    return liste2

def kosul_3():
    df = puantaj.main()
    kosul3 = ((df["Günler"] == "Haftaiçi") & df["Giriş"].isna() & df["Çıkış"].notna())
    df.loc[kosul3, "Notlar"] = degiskenler.açıklama_3
    liste3 = df[kosul3]
    return liste3


def kosul_4():
    df = puantaj.main()
    kosul4 = ((df["Günler"] == "Haftaiçi") & df["Giriş"].notna() & (df["Çıkış"] > "18:30") & (df["OFM"] == "00:00"))
    df.loc[kosul4, "Notlar"] = degiskenler.açıklama_4
    liste4 = df[kosul4]
    return liste4

def kosul_5():
    df = puantaj.main()
    kosul5 = ((df["Günler"] == "Haftaiçi") & df["Giriş"].notna() & df["Çıkış"].notna() & (df["EM"] > "00:15") & df["İzin Açıklama"].isna())
    df.loc[kosul5, "Notlar"] = degiskenler.açıklama_5
    liste5 = df[kosul5]
    return liste5

def kosul_6():
    df = puantaj.main()
    kosul6 = ((df["Günler"] == "Haftasonu") & df["Giriş"].notna() & df["Çıkış"].isna())
    df.loc[kosul6, "Notlar"] = degiskenler.açıklama_6
    liste6 = df[kosul6]
    return liste6

def kosul_7():
    df = puantaj.main()
    kosul7 = ((df["Günler"] == "Haftasonu") & df["Giriş"].isna() & df["Çıkış"].notna())
    df.loc[kosul7, "Notlar"] = degiskenler.açıklama_7
    liste7 = df[kosul7]
    return liste7

def kosul_8():
    df = puantaj.main()
    kosul8 = ((df["Günler"] == "Haftasonu") & df["Giriş"].notna() & df["Çıkış"].notna() & (df["OFM"] == "00:00"))
    df.loc[kosul8, "Notlar"] = degiskenler.açıklama_8
    liste8 = df[kosul8]
    return liste8


def özet_tablo() -> object:

    puntaj_raporu = pd.concat([kosul_1(), kosul_2(), kosul_3(), kosul_4(),
                               kosul_5(), kosul_6(), kosul_7(), kosul_8()], axis=0)

    return puntaj_raporu.to_excel("Kontrol_raporu.xlsx")






