from matplotlib import pyplot as plt
import fastf1
import fastf1.plotting

fastf1.plotting.setup_mpl()

session = fastf1.get_session(2022, 'Belgiun', 'Q')

session.load()
fast_max = session.laps.pick_driver('VER').pick_fastest()
max_car_data = fast_max.get_car_data()
t = max_car_data['Time']
vCar = max_car_data['Speed']

fig, ax = plt.subplots()
ax.plot(t, vCar, label='Fast')
ax.set_xlabel('Time')
ax.set_ylabel('Speed [Km/h]')
ax.set_title('Verstappen - Fastest Lap')
ax.legend()
plt.show()