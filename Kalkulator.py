import streamlit as st
st.write("""
# Kalkulator Restriksi
Aplikasi Untuk Menghitung Restriksi Obat Kemoterapi
""")
BB= st.number_input("Masukkan Berat Badan dalam Kilogram")
TB= st.number_input("Masukkan Tinggi Badan dalam Centimeter")
Hitung= st.button ("Hitung Restriksi")

import math as m
if Hitung :
    BSA = m.sqrt(BB*TB/3600)
    BSA_x="{:.2f}".format(BSA)
    st.write("BSA :",BSA_x)
  

    Paklitaksel=BSA*175
    Paklitaksel_x="{:.2f}".format(Paklitaksel)
    Bendamustin=BSA*100
    Bendamustin_x="{:.2f}".format(Bendamustin)
    Irinotekan_2=BSA*125
    Irinotekan_2_x="{:.2f}".format(Irinotekan_2)
    Irinotekan_3=BSA*180
    Irinotekan_3_x="{:.2f}".format(Irinotekan_3)
    rituksimab=BSA*375
    rituksimab_x="{:.2f}".format(rituksimab)
    Fluorourasil_Nasofaring=BSA*1000
    Fluorourasil_Nasofaring_x="{:.2f}".format(Fluorourasil_Nasofaring)
    Fluorourasil_Kolorektal=BSA*2800
    Fluorourasil_Kolorektal_x="{:.2f}".format(Fluorourasil_Kolorektal)
    Dosetaksel_kombinasi=BSA*75
    Dosetaksel_kombinasi_x="{:.2f}".format(Dosetaksel_kombinasi)
    Dosetaksel_Tunggal=BSA*100
    Dosetaksel_Tunggal_x="{:.2f}".format(Dosetaksel_Tunggal)
    Kapesitabin=BSA*2500
    Kapesitabin_x="{:.2f}".format(Kapesitabin)
    Epirubisin=BSA*900
    Epirubisin_x="{:.2f}".format(Epirubisin)
    Doksorubisin=BSA*500
    Doksorubisin_x="{:.2f}".format(Doksorubisin)
    st.write("Paklitaksel:",Paklitaksel_x)
    st.write("Bendamustin:",Bendamustin_x)
    st.write("Irinotekan  2 minggu:",Irinotekan_2_x)
    st.write("Irinotekan  3 minggu:",Irinotekan_3_x)
    st.write("Rituksimab:",rituksimab_x)
    st.write("Fluorourasil Nasofaring:",Fluorourasil_Nasofaring_x)
    st.write("Fluorourasil Kolorektal:",Fluorourasil_Kolorektal_x)
    st.write("Oksaliplatin:","12X")
    st.write("Doksorubisin:",Doksorubisin_x,"Untuk Seumur Hidup")
    st.write("Dosetaksel kombinasi :",Dosetaksel_kombinasi_x)
    st.write("Dosetaksel Tunggal :",Dosetaksel_Tunggal_x)
    st.write("Kapesitabin :",Kapesitabin_x)
    st.write("Epirubisin :",Epirubisin_x)
    



