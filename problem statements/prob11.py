slots=list(map(str,input('Enter book  slots:').split()))
time_slots=input('Enter reuested  slots:')
print("slote already booked" if time_slots in slots else "slot is available")