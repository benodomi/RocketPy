from rocketpy import Environment, Rocket, SolidMotor, Flight, FlightSoftware
import datetime
import time

env = Environment(
    latitude=32.990254,
    longitude=-106.974998,
    elevation=1400,
)

tomorrow = datetime.date.today() + datetime.timedelta(days=1)

# env.set_date(
#   (tomorrow.year, tomorrow.month, tomorrow.day, 12), timezone="America/Denver"
# ) # Tomorrow's date in year, month, day, hour UTC format

# env.set_atmospheric_model(type='Forecast', file='GFS')

Pro75M1670 = SolidMotor(
    thrust_source='data/motors/Cesaroni_M1670.eng',
    dry_mass=1.815,
    dry_inertia=(0.125, 0.125, 0.002),
    center_of_dry_mass_position=0.317,
    grains_center_of_mass_position=0.397,
    burn_time=3.9,
    grain_number=5,
    grain_separation=0.005,
    grain_density=1815,
    grain_outer_radius=0.033,
    grain_initial_inner_radius=0.015,
    grain_initial_height=0.12,
    nozzle_radius=0.033,
    throat_radius=0.011,
    interpolation_method="linear",
    nozzle_position=0,
    coordinate_system_orientation="nozzle_to_combustion_chamber",
)

calisto = Rocket(
    radius=0.0635,
    mass=14.426,  # without motor
    inertia=(6.321, 6.321, 0.034),
    power_off_drag="data/calisto/powerOffDragCurve.csv",
    power_on_drag="data/calisto/powerOnDragCurve.csv",
    center_of_mass_without_motor=0,
    coordinate_system_orientation="tail_to_nose",
)

buttons = calisto.set_rail_buttons(
    upper_button_position=0.0818,
    lower_button_position=-0.6182,
    angular_position=45,
)

calisto.add_motor(Pro75M1670, position=-1.255)

nose = calisto.add_nose(
    length=0.55829, kind="vonKarman", position=1.278
)

fins = calisto.add_trapezoidal_fins(
    n=4,
    root_chord=0.120,
    tip_chord=0.040,
    span=0.100,
    sweep_length=None,
    cant_angle=0,
    position=-1.04956,
)

tail = calisto.add_tail(
    top_radius=0.0635, bottom_radius=0.0435, length=0.060, position=-1.194656
)

def my_fun(a,b,c):
    print("Kokot")
    


main = calisto.add_parachute(
    name="main",
    cd_s=10.0,
    trigger=800,  # ejection altitude in meters
    sampling_rate=100,
    lag=1.5,
    noise=(0, 8.3, 0.5),
)

drogue = calisto.add_parachute(
    name="drogue",
    cd_s=1.0,
    trigger="apogee",  # ejection at apogee
    sampling_rate=100,
    lag=1.5,
    noise=(0, 8.3, 0.5),
)

flight_soft = FlightSoftware(sampling_period= 0.01, real_time= True)

'''
For HIL/SIL/MIL simulation: 
    max_time_step <= sampling_period of FSW,
    time_overshoot=False
'''
test_flight = Flight(
  rocket=calisto, flight_software= flight_soft, environment=env, rail_length=5.2, inclination=85, heading=0, min_time_step= 0, max_time_step= 0.01, time_overshoot=False
)


test_flight.all_info()
