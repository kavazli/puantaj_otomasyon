########### Kuşullar ###################################################################################

# kosul_1 = Haftaiçi / Giriş yok / Çıkış Yok / İzin açıklaması yok /                           => Personelin izin bilgisi eksik
# kosul_2 = Haftaiçi / Giriş var / Çıkış Yok /                                                 => Personelin çıkış bilgisi eksik
# kosul_3 = Haftaiçi / Giriş yok / Çıkış var /                                                 => Personelin giriş bilgisi eksik
# kosul_4 = Haftaiçi / Giriş var / Çıkış saat 18:30 sonrası / OFM yok /                        => Personelin OFM bilgisi yok
# kosul_5 = Haftaiçi / Giriş var / Çıkış var / EM de eksik saat var / İzin Açıklaması Yok /    => Personelin eksik saat bilgisi yok
# kosul_6 = Haftasonu / Giriş var / çıkış yok /                                                => Personelin çıkış bilgisi eksik
# kosul_7 = Haftasonu / Giriş yok / Çıkış var /                                                => Personelin giriş bilgisi eksik
# kosul_8 = Haftasonu / Giriş var / Çıkış var / OFM yok /                                      => Personelin OFM bilgisi yok


vardiya_excel = "kod_düzen.xlsx"
excel_sayfa = "Vardiya2"
puantaj = "download.csv"
#path = "C:/Users/gokhan.kaya/OneDrive - Aster Textile/Desktop/BELGELERİM/PycharmProjects/mainProject/"
#rapor_adı = "Kontrol_raporu.xlsx"

açıklama_1 = "Personelin izin bilgisi eksik"
açıklama_2 = "Personelin çıkış bilgisi eksik"
açıklama_3 = "Personelin giriş bilgisi eksik"
açıklama_4 = "Personelin OFM bilgisi yok"
açıklama_5 = "Personelin eksik saat bilgisi yok"
açıklama_6 = "Personelin çıkış bilgisi eksik"
açıklama_7 = "vPersonelin giriş bilgisi eksik"
açıklama_8 = "Personelin OFM bilgisi yok"

gönderilenler = ["gokhan.kaya@astertextile.com",
                 "ayten.guler@astertextile.com",
                 "ferhat.sen@astertextile.com",
                 "serife.yaprak@astertextile.com",
                 "aysenur.cakir@astertextile.com",
                 "ahmet.deniz@astertextile.com",
                 "ahmet.balta@astertextile.com",
                 "burcu.seymen@astertextile.com",
                 "hande.yazici@astertextile.com",]