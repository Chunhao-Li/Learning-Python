
import math

## Simulate flight of first stage of the Falcon 9 (FT) rocket to
## find out how high it can go

## an answer(?): 
# https://www.reddit.com/r/spacex/comments/5tklb4/falcon_9ft_first_stage_flight_analysis/

## From SpaceX web page:
takeoff_weight = 549054.0     # kg
stage1_burn_time = 162        # s
stage1_thrust_sl = 7607000.0  # N (kg m / s^2)
stage1_thrust_vac = 8227000.0 # N (kg m / s^2)

## https://space.stackexchange.com/questions/17945/falcon-9-fuel-use
# "Mass of propellant on first stage, fuel + oxidizer, is on the order
#  of 395,700kg"
stage1_fuel = 395700.0        # kg

stage1_burn_rate = stage1_fuel / stage1_burn_time  # kg / s
non_fuel_weight = takeoff_weight - stage1_fuel

gravity = 9.81  # m / s^2

def thrust(altitude, thrust_at_sea_level, thrust_in_vacuum):
    '''Calculate thrust as a function of altitude, using the given
    values for thrust at sea level and in vacuum. We assume a linear
    interpolation, and that vacuum begins at 120km (100-120km seems
    a reasonable guess; see
    https://en.wikipedia.org/wiki/Atmosphere_of_Earth).'''
    if altitude < 120000:
        f = altitude / 120000
        return (f * (thrust_in_vacuum - thrust_at_sea_level)) + thrust_at_sea_level
    else:
        return thrust_in_vacuum


# The variables we are going to track in the simulation
time = 0
altitude = 0
velocity = 0
remaining_fuel = stage1_fuel
mass = non_fuel_weight + remaining_fuel

# Set the time step to 1 second
dt = 1

while remaining_fuel >= (stage1_burn_rate * dt):
    # Calculate change in altitude, velocity and mass from the
    # current values, and update the variables.
    altitude = altitude + velocity * dt
    acceleration = (thrust(altitude, stage1_thrust_sl, stage1_thrust_vac) / mass) - gravity
    velocity = velocity + acceleration * dt
    remaining_fuel = remaining_fuel - stage1_burn_rate * dt
    mass = non_fuel_weight + remaining_fuel
    time = time + dt

    # Print some information so we can track progress
    print(time, altitude, velocity)
