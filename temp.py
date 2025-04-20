from pyttsx3 import speak
import datetime
now = datetime.datetime.now()
hrs = now.hour
mint = now.minute
speak('the time is'+str(hrs)+','+str(mint))