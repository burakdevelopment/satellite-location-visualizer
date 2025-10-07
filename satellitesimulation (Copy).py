import requests
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib.animation import FuncAnimation
from datetime import datetime
import tkinter as tk
from tkinter import ttk

API_KEY = "yourapikey:D"

#norad id'ler
satellites = {
    "ISS": 25544,
    "Hubble Uzay Teleskobu": 20580,
    "Tiangong Uzay İstasyonu": 48274,
    "NOAA-20": 43013,
    "GOES-16": 41753,
    "Starlink 44942": 44942,
    "GPS PRN 01": 24876,
    "Envisat": 27386
}


def get_satellite_position(norad_id):
    url = f"https://api.n2yo.com/rest/v1/satellite/positions/{norad_id}/0/0/0/1/&apiKey={API_KEY}"
    response = requests.get(url)
    data = response.json()
    pos = data['positions'][0]
    return pos['satlatitude'], pos['satlongitude']

root = tk.Tk()
root.title("Uydu Seçimi")

label = tk.Label(root, text="Takip edilecek uyduları seçin (Ctrl+Click çoklu seçim):")
label.pack()

listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, width=40, height=10)
for sat in satellites.keys():
    listbox.insert(tk.END, sat)
listbox.pack()

def start_animation():
    selected_indices = listbox.curselection()
    selected_sats = [list(satellites.values())[i] for i in selected_indices]
    selected_names = [list(satellites.keys())[i] for i in selected_indices]

    root.destroy()  

    
    fig = plt.figure(figsize=(12, 6))
    m = Basemap(projection='mill', lon_0=0)
    m.drawcoastlines()
    m.drawcountries()
    m.drawmapboundary(fill_color='aqua')
    m.fillcontinents(color='lightgreen', lake_color='aqua')
    plt.title("Seçilen Uyduların Dünya Üzerindeki Yolu - Gerçek Zamanlı Simülasyon")

    sat_positions = {name: {'lats': [], 'lons': [], 'line': m.plot([], [], marker='o', linewidth=2, markersize=5, label=name)[0]} for name in selected_names}
    plt.legend()

    def update(frame):
        for name, norad_id in zip(selected_names, selected_sats):
            lat, lon = get_satellite_position(norad_id)
            sat_positions[name]['lats'].append(lat)
            sat_positions[name]['lons'].append(lon)
            x, y = m(sat_positions[name]['lons'], sat_positions[name]['lats'])
            sat_positions[name]['line'].set_data(x, y)
        return [sat_positions[name]['line'] for name in selected_names]

    ani = FuncAnimation(fig, update, interval=5000)
    plt.show()

start_btn = tk.Button(root, text="Başlat", command=start_animation)
start_btn.pack()

root.mainloop()
