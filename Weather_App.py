from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk  # For image handling
import requests

def data_get():
    city = city_name.get()
    try:
        # Fetch weather data
        data = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=07e021957a8dae19ba4ccd2be561bc1a").json()
        
        # Update weather information labels
        wc_label.config(text=data["weather"][0]["main"])
        wd_label.config(text=data["weather"][0]["description"])
        temp_label.config(text=f"{round(data['main']['temp'] - 273.15, 1)}°C")
        min_temp_label.config(text=f"Min: {round(data['main']['temp_min'] - 273.15, 1)}°C")
        max_temp_label.config(text=f"Max: {round(data['main']['temp_max'] - 273.15, 1)}°C")

        # Dynamically update the weather image
        weather_condition = data["weather"][0]["main"].lower()
        if "cloud" in weather_condition:
            weather_icon = Image.open("C:\\Users\\gurpr\\OneDrive\\Desktop\\cloud_icon.png")
        elif "rain" in weather_condition:
            weather_icon = Image.open("C:\\Users\\gurpr\\OneDrive\\Desktop\\rain_icon.webp")
        else:
            weather_icon = Image.open("C:\\Users\\gurpr\\OneDrive\\Desktop\\sun_icon.jpg")  # Default icon for sunny/clear

        # Resize the image and update the label
        weather_icon = weather_icon.resize((100, 100), Image.Resampling.LANCZOS)
        weather_image = ImageTk.PhotoImage(weather_icon)
        weather_image_label.config(image=weather_image)
        weather_image_label.image = weather_image  # Keep a reference to avoid garbage collection

    except KeyError:
        # Handle invalid city or API errors
        wc_label.config(text="N/A")
        wd_label.config(text="Invalid City")
        temp_label.config(text="N/A")
        min_temp_label.config(text="N/A")
        max_temp_label.config(text="N/A")
        weather_image_label.config(image="")  # Clear the image if error

# Create main window
window = Tk()
window.title("SkyCast: Your Personal Weather Guide")
window.geometry("500x500")

# Adding the background image
bg_image = Image.open("C:\\Users\\gurpr\\OneDrive\\Desktop\\bg.webp")  # Use your uploaded image
bg_image = bg_image.resize((500, 700), Image.Resampling.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = Label(window, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Title Label
title_label = Label(window, text="SkyCast", font=("Arial", 24, "bold"), bg="#ffffff", fg="#000")
title_label.place(x=150, y=20, width=200, height=50)

# City Entry
city_name = StringVar()
city_label = Label(window, text="Enter City:", font=("Arial", 12, "bold"), bg="#ffffff", fg="#000")
city_label.place(x=50, y=90)
city_entry = ttk.Entry(window, textvariable=city_name, font=("Arial", 12))
city_entry.place(x=150, y=90, width=200)

# Search Button
search_button = Button(window, text="Get Weather", font=("Arial", 12, "bold"), bg="#007BFF", fg="white", command=data_get)
search_button.place(x=370, y=85, width=100, height=30)

# Weather Information Section
weather_frame = Frame(window, bg="#E6F7FF", bd=2, relief="groove")  # Frame with a light blue background and border
weather_frame.place(x=50, y=150, width=400, height=300)

# Add a background image to the weather frame (optional)
weather_frame_bg_image = Image.open("C:\\Users\\gurpr\\OneDrive\\Desktop\\weather_frame_bg.webp")
weather_frame_bg_image = weather_frame_bg_image.resize((400, 300), Image.Resampling.LANCZOS)
weather_frame_bg_photo = ImageTk.PhotoImage(weather_frame_bg_image)
weather_frame_bg_label = Label(weather_frame, image=weather_frame_bg_photo)
weather_frame_bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Add weather labels
temp_label = Label(weather_frame, text="Temperature", font=("Arial", 20, "bold"), bg="#E6F7FF", fg="#000")
temp_label.place(x=100, y=20, width=200)

wc_label = Label(weather_frame, text="N/A", font=("Arial", 14, "bold"), bg="#E6F7FF", fg="#000")
wc_label.place(x=50, y=70, width=300)

wd_label = Label(weather_frame, text="N/A", font=("Arial", 12), bg="#E6F7FF", fg="#000")
wd_label.place(x=50, y=110, width=300)

min_temp_label = Label(weather_frame, text="Min: N/A", font=("Arial", 12), bg="#E6F7FF", fg="#000")
min_temp_label.place(x=50, y=160, width=150)

max_temp_label = Label(weather_frame, text="Max: N/A", font=("Arial", 12), bg="#E6F7FF", fg="#000")
max_temp_label.place(x=200, y=160, width=150)

# Weather Icon Label (dynamic image display within the weather frame)
weather_image_label = Label(weather_frame, bg="#E6F7FF")
weather_image_label.place(x=150, y=200, width=100, height=100)

# Footer
footer_label = Label(window, text="Powered by OpenWeather API", font=("Arial", 10), bg="#ADD8E6", fg="#000")
footer_label.place(x=150, y=650, width=200)

# Run the application
window.mainloop()
