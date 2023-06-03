import streamlit as st
from streamlit_option_menu import option_menu
import math
import pandas as pd
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

page_bg_img ="""
<style>
[data-testid="stAppViewContainer"]{
background-image : url("https://www.banjarsmartdigital.com/blog/wp-content/webp-express/webp-images/uploads/2021/09/background-putih-abstrak-1024x480.jpg.webp");
background-size : cover;
}

[data-testid="stSidebar"]{
background-image: url("https://wallpaperaccess.com/full/3087165.jpg");
background-size: cover;

</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)
with st.sidebar :
    selected = option_menu ("Pilih Jenis Rangkaian dengan Konfigurasi Common Emitter",
    ["Home",
    "Rangkaian Fixed Bias",
    "Rangkaian Voltage Divider Bias",
    "Rangkaian Source-Follower (Common-Drain)",],
    default_index=0)

if(selected == "Home") :
    st.header(":blue[Kalkulator Perhitungan Rangkaian FET Analisis AC model re (Zi, Av dan Zo)]")
    st.subheader(":blue[By abdul Rahman (11-2021-D:023)]:orange[ dari ITENAS Program Studi Teknik Elektro]")
    st.write(":blue[Program ini dibuat untuk memenuhi Tugas Besar Elektronika Analog\nDosen Pengampu : Ir. Rustamaji M.T]")
    st.image("ITENAS.jpeg", width=500)

if(selected == "Rangkaian Fixed Bias") :
    st.title(":green[_Contoh Rangkaian Fixed Bias Konfigurasi Common Source_]")
    st.image("FET FIXED.jpg", width = 500)
    st.title(":green[_Rangkaian Ekivalen model re Fixed Bias Konfigurasi Common Source_]")
    st.image("FET EKIVALEN.jpg", width = 500)
    st.subheader(":green[_Perhitungan Analisis AC model re dan Simulasi Sinyal Output_]")

    a=st.number_input(":green[Masukkan Nilai VDD (Volt)]",0)
    b=st.number_input(":green[Masukkan Nilai VGSQ (Volt)]",0.00)
    c=st.number_input(":green[Masukkan Nilai Vp (Volt) ]",0)
    g=st.number_input(":green[Masukkan nilai IDSS (mA)]",0)
    f=st.number_input(":green[Masukkan Nilai RD (Ω)]",0)
    h=st.number_input(":green[Masukkan nilai RG (Ω)]",0)
    i=st.number_input(":green[Masukkan nilai gos (µS)]")
    d=st.number_input(":green[Masukkan nilai Kapasitor Coupling1 (µF)]",0)
    e=st.number_input(":green[Masukkan nilai Kapasitor Coupling2 (µF)]",0)
    m=st.number_input(":green[Masukkan Nilai Tegangan Input (volt) =]",0.00)
    perhitungan = st.button(":red[_Analisis AC dan Sinyal Output_]")

    if perhitungan :
        gmo=round((2*((g)*(10**-3))/c),8)
        gm=round(gmo*(1-(b/c)),8)
        rd=round(1/(i*(10**-6)),8)
        zi=h
        zo=round((f*rd)/(f+rd),8)
        av=round(-gm*(zo),2)
        vo=av*m

        st.write(":green[ANALISIS AC]")
        st.success(f":green[Nilai  gmo = {gmo} S]")
        st.success(f":green[Nilai gm = {gm} S]")
        st.success(f":green[Nilai rd = {rd} Ω]")
        st.success(f":green[Nilai Zi = {zi} Ω]")
        st.success(f":green[Nilai Zo = {zo} Ω]")
        st.success(f":green[Nilai Av = {av} Kali]")
        st.success(f":green[Nilai Vo = {vo} Volt]")
        
        def sinusoidal():
            t = np.linspace(-0.05, 0.05, 1000)
            phase_shift = 180  # Phase shift in degrees
            
            # Calculate the sinusoidal signals
            hasil_Vi = m * np.sin(2 * np.pi * 50 * t + np.deg2rad(phase_shift))
            hasil_Vo = -1 * av * m * np.sin(2 * np.pi * 50 * t )

            hasil_Vo[hasil_Vo > a ]= a
            hasil_Vo[hasil_Vo < -a] = -a

            if perhitungan:
                fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))
                ax1.plot(t, hasil_Vi)
                ax1.set_xlabel('Waktu (s)')
                ax1.set_ylabel('Amplitudo (V)')
                ax1.set_title('Sinyal Vi')
                ax1.grid(True)

                ax2.plot(t, hasil_Vo)
                ax2.set_xlabel('Waktu (s)')
                ax2.set_ylabel('Amplitudo (V)')
                ax2.set_title('Sinyal Vo')
                ax2.grid(True)

                plt.xlim(-0.05, 0.05)
                plt.tight_layout()
                st.pyplot(fig)

        sinusoidal()


    
if(selected == "Rangkaian Voltage Divider Bias") :
    st.title(":blue[_Contoh Rangkaian Voltage Divider Bias Konfigurasi Common Source_]")
    st.image("FET DIV.jpg", width = 500)
    st.title(":blue[_Rangkaian Ekivalen model re Voltage Divider Bias Konfigurasi Common Source_]")
    st.image("FET DIV EKIV.jpg", width = 500)
    st.subheader(":blue[_Perhitungan Analisis AC model re dan Simulasi Sinyal Output_]")

    a=st.number_input(":blue[Masukkan Nilai VDD (Volt)]",0)
    b=st.number_input(":blue[Masukkan Nilai VGSQ (Volt)]",0.00)
    c=st.number_input(":blue[Masukkan Nilai Vp (Volt) ]",0)
    d=st.number_input(":blue[Masukkan nilai IDSS (mA) ]",0)
    e=st.number_input(":blue[Masukkan Nilai RD (Ω)]",0)
    f=st.number_input(":blue[Masukkan Nilai R1 (Ω)]",0)
    g=st.number_input(":blue[Masukkan Nilai R2 (Ω)]",0)
    h=st.number_input(":blue[Masukkan Nilai RS (Ω)]",0)
    l=st.number_input(":blue[Masukkan Nilai gos (µS)]")
    i=st.number_input(":blue[Masukkan Nilai Kapasitor Coupling1 (µF)]",0)
    j=st.number_input(":blue[Masukkan Nilai Kapasitor Coupling2 (µF)]",0)
    k=st.number_input(":blue[Masukkan Nilai Kapasitor Cs (µF)]",0)
    m=st.number_input(":blue[Masukkan Nilai Tegangan Input (volt) =]",0.00)
    perhitungan=st.button(":red[_Analisis AC dan Simulasi Sinyal Output_]")

    if perhitungan :
        gmo=round((2*(d*(10**-3))/c),8)
        gm=round(gmo*(1-(b/-c)),8)
        rd=round(1/(l*(10**-6)),8)
        zi=round((f*g)/(f+g),5)
        zo=round((rd*e)/(rd+e),8)
        av=round((-gm*e),2)
        vo=av*m

        st.write(":green[ANALISIS AC]")
        st.success(f":blue[Nilai  gmo = {gmo} S]")
        st.success(f":blue[Nilai gm = {gm} S]")
        st.success(f":blue[Nilai rd = {rd} Ω]")
        st.success(f":blue[Nilai Zi = {zi} Ω]")
        st.success(f":blue[Nilai Zo = {zo} Ω]")
        st.success(f":blue[Nilai Av = {av} Kali]")
        st.success(f":blue[Nilai Vo = {vo} Volt]")
        def sinusoidal():
            t = np.linspace(-0.05, 0.05, 1000)
            phase_shift = 180  # Phase shift in degrees
            
            # Calculate the sinusoidal signals
            hasil_Vi =  m * np.sin(2 * np.pi * 50 * t + np.deg2rad(phase_shift))
            hasil_Vo = -1 * av * m * np.sin(2 * np.pi * 50 * t )

            hasil_Vo[hasil_Vo > a ]= a
            hasil_Vo[hasil_Vo < -a] = -a

            if perhitungan:
                fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))
                ax1.plot(t, hasil_Vi)
                ax1.set_xlabel('Waktu (s)')
                ax1.set_ylabel('Amplitudo (V)')
                ax1.set_title('Sinyal Vi')
                ax1.grid(True)

                ax2.plot(t, hasil_Vo)
                ax2.set_xlabel('Waktu (s)')
                ax2.set_ylabel('Amplitudo (V)')
                ax2.set_title('Sinyal Vo')
                ax2.grid(True)

                plt.xlim(-0.05, 0.05)
                plt.tight_layout()
                st.pyplot(fig)

        sinusoidal()

if(selected == "Rangkaian Source-Follower (Common-Drain)") :
    st.title(":red[_Contoh Rangkaian Fixed Bias Konfigurasi Common Source_]")
    st.image("SOURCE.jpg", width = 500)
    st.title(":red[_Rangkaian Ekivalen model re Fixed Bias Konfigurasi Common Source_]")
    st.image("SOURCE EKIV.jpg", width = 500)
    st.subheader(":red[_Perhitungan Analisis AC model re dan Simulasi Sinyal Output_]")
    
    a=st.number_input(":red[Masukkan Nilai VDD (Volt)]",0)
    b=st.number_input(":red[Masukkan Nilai VGSQ (Volt)]",0.00)
    c=st.number_input(":red[Masukkan Nilai Vp (Volt) ]",0)
    g=st.number_input(":red[Masukkan nilai IDSS (mA)]",0)
    f=st.number_input(":red[Masukkan Nilai RS (Ω)]",0)
    h=st.number_input(":red[Masukkan nilai RG (Ω)]",0)
    i=st.number_input(":red[Masukkan nilai gos (µS)]")
    d=st.number_input(":red[Masukkan nilai Kapasitor Coupling1 (µF)]",0)
    e=st.number_input(":red[Masukkan nilai Kapasitor Coupling2 (µF)]",0)
    m=st.number_input(":red[Masukkan Nilai Tegangan Input (volt) =]",0.00)
    perhitungan = st.button(":red[_Analisis AC dan Sinyal Output_]")

    if perhitungan :
        gmo=round((2*((g)*(10**-3))/c),8)
        gm=round(gmo*(1-(b/c)),8)
        rd=round(1/(i*(10**-6)),8)
        zi=h
        p=(f*rd)/(f+rd)
        zo=round((p*(1/gm))/(p+(1/gm)),8)
        av1=gm*p
        av=round(av1/(1+(av1)),2)
        vo=av*m

        st.write(":green[ANALISIS AC]")
        st.success(f":red[Nilai  gmo = {gmo} S]")
        st.success(f":red[Nilai gm = {gm} S]")
        st.success(f":red[Nilai rd = {rd} Ω]")
        st.success(f":red[Nilai Zi = {zi} Ω]")
        st.success(f":red[Nilai Zo = {zo} Ω]")
        st.success(f":red[Nilai Av = {av} Kali]")
        st.success(f":red[Nilai Vo = {vo} Volt]")
        
        def sinusoidal():
            t = np.linspace(-0.05, 0.05, 1000)
            phase_shift = 180  # Phase shift in degrees
            
            # Calculate the sinusoidal signals
            hasil_Vi = m * np.sin(2 * np.pi * 50 * t + np.deg2rad(phase_shift))
            hasil_Vo = -1 * av * m * np.sin(2 * np.pi * 50 * t )

            hasil_Vo[hasil_Vo > a ]= a
            hasil_Vo[hasil_Vo < -a] = -a

            if perhitungan:
                fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))
                ax1.plot(t, hasil_Vi)
                ax1.set_xlabel('Waktu (s)')
                ax1.set_ylabel('Amplitudo (V)')
                ax1.set_title('Sinyal Vi')
                ax1.grid(True)

                ax2.plot(t, hasil_Vo)
                ax2.set_xlabel('Waktu (s)')
                ax2.set_ylabel('Amplitudo (V)')
                ax2.set_title('Sinyal Vo')
                ax2.grid(True)

                plt.xlim(-0.05, 0.05)
                plt.tight_layout()
                st.pyplot(fig)

        sinusoidal()

