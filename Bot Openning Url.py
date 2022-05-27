import webbrowser, time

url = input('Input URL : ')
durasi = 5

for i in range (5):
    webbrowser.open_new(url)
    time.sleep(durasi)


