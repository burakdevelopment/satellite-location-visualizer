import datetime
import requests
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib.animation import FuncAnimation
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from skyfield.api import load, EarthSatellite, Topos



satellites = {
    "ISS": 25544,
    "Hubble Uzay Teleskobu": 20580,
    "Tiangong Uzay İstasyonu": 48274,
    "NOAA-20": 43013,
    "GOES-16": 41753,  
    "Starlink 44942": 44942,
    "GPS PRN 01": 24876,
    "Envisat": 27386  #buraya farklı satelittle lar ve kodlarını girebilirsiniz
}

ts = load.timescale()
eph = load('de421.bsp') #bu apisiz location tahmini için cihaza inecek olan data'dır bunun sayesinde hesaplamalar ve konum tahmini yapılır

def fetch_and_create_satellites(sat_dict):
    print("TLE verileri CelesTrak'ten çekiliyor...")
    satellite_objects = {}
    session = requests.Session()
    
    for name, norad_id in sat_dict.items():
        try:
            url = f"https://celestrak.org/NORAD/elements/gp.php?CATNR={norad_id}&FORMAT=tle"
            response = session.get(url)
            response.raise_for_status()
            
            tle_data = response.text.splitlines()
            
            if len(tle_data) >= 2:
                line1 = tle_data[-2]
                line2 = tle_data[-1]
                
                sat = EarthSatellite(line1, line2, name, ts)
                satellite_objects[name] = sat
                print(f"  + {name} (NORAD {norad_id}) TLE başarıyla yüklendi.")
            else:
                print(f"  - {name} (NORAD {norad_id}) için TLE verisi alınamadı. Atlanıyor.")
                
        except requests.exceptions.RequestException as e:
            print(f"  - {name} (NORAD {norad_id}) yüklenirken hata: {e}. Atlanıyor.")
        except Exception as e:
            print(f"  - {name} işlenirken beklenmedik hata: {e}. Atlanıyor.")
            
    print("TLE yüklemesi tamamlandı!")
    return satellite_objects

root = tk.Tk()
root.title("Uydu Seçimi (SGP4 Modeli)")

label = tk.Label(root, text="Takip edilecek uyduları seçin (Ctrl+Click çoklu seçim):")
label.pack(pady=10)

listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, width=50, height=len(satellites))
for sat in satellites.keys():
    listbox.insert(tk.END, sat)
listbox.pack(padx=10, pady=5)

def start_animation():
    selected_indices = listbox.curselection()
    if not selected_indices:
        messagebox.showwarning("Uyarı", "Lütfen en az bir uydu seçin.")
        return
        
    selected_names = [list(satellites.keys())[i] for i in selected_indices]
    selected_sat_ids = {name: satellites[name] for name in selected_names}
    
    try:
        satellite_objects = fetch_and_create_satellites(selected_sat_ids)
    except Exception as e:
        messagebox.showerror("Hata", f"TLE verileri çekilemedi: {e}")
        return

    if not satellite_objects:
        messagebox.showerror("Hata", "Seçilen uydular için TLE verisi bulunamadı. Program kapatılıyor")
        root.destroy()
        return

    available_sat_names = list(satellite_objects.keys())

    root.destroy()  

    
    fig = plt.figure(figsize=(15, 8))
    m = Basemap(projection='mill', lon_0=0)
    m.drawcoastlines(linewidth=0.5)
    m.drawcountries(linewidth=0.5)
    m.drawmapboundary(fill_color='#a0c3d1') 
    m.fillcontinents(color='#4c703a', lake_color='#a0c3d1') 
    
    m.drawparallels(range(-90, 91, 30), labels=[1,0,0,0], fontsize=10, color='gray')
    m.drawmeridians(range(-180, 181, 60), labels=[0,0,0,1], fontsize=10, color='gray')

    plt.title(f"Seçilen Uyduların Gerçek Zamanlı Yörünge İzi (SGP4 Modeli) - {datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}")

    sat_positions = {name: {'lats': [], 'lons': [], 'line': m.plot([], [], marker='o', linewidth=1, markersize=4, label=name)[0]} for name in available_sat_names}
    sat_points = {name: m.plot([], [], marker='o', markersize=8, color=sat_positions[name]['line'].get_color(), markeredgecolor='white')[0] for name in available_sat_names}
    
    plt.legend(loc='lower left')

    def update(frame):
        t = ts.now()
        
        lines_to_update = []
        
        for name in available_sat_names:
            sat = satellite_objects[name]
            
            
            geocentric = sat.at(t)
            
            subpoint = geocentric.subpoint()
            lat = subpoint.latitude.degrees
            lon = subpoint.longitude.degrees
            
            sat_positions[name]['lats'].append(lat)
            sat_positions[name]['lons'].append(lon)
            
            x, y = m(sat_positions[name]['lons'], sat_positions[name]['lats'])
            
            sat_positions[name]['line'].set_data(x, y)
            
            x_point, y_point = m(lon, lat)
            sat_points[name].set_data([x_point], [y_point])

            lines_to_update.append(sat_positions[name]['line'])
            lines_to_update.append(sat_points[name])
            
        return lines_to_update

    ani = FuncAnimation(fig, update, interval=5000, blit=True)
    plt.show()

start_btn = tk.Button(root, text="Simülasyonu Başlat", command=start_animation, font=("Helvetica", 12), bg="#4CAF50", fg="white")
start_btn.pack(pady=10, fill=tk.X, padx=10)

root.mainloop()
