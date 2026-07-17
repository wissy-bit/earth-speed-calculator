import math

# ==========================================
# CONSTANTS (Using SI Units)
# ==========================================
G = 6.67430e-11  # Gravitational constant in m^3 kg^-1 s^-2
M_sun = 1.989e30 # Mass of the Sun in kg
r_orbit = 1.496e11 # Average distance from Earth to Sun (1 AU) in meters
r_earth = 6.371e6  # Radius of the Earth in meters

# ==========================================
# PART 1: Earth's Orbital Speed (Translation)
# ==========================================
def calculate_orbital_speed(mass_sun, orbital_radius):
    """
    Calculates the orbital speed of a planet using Kepler's/Newton's laws.
    Formula: v = sqrt((G * M) / r)
    """
    v = math.sqrt((G * mass_sun) / orbital_radius)
    return v

# ==========================================
# PART 2: Earth's Rotational Speed
# ==========================================
def calculate_rotational_speed(latitude_degrees):
    """
    Calculates Earth's rotational speed at a specific latitude.
    Formula: v_rot = (2 * pi * R_earth * cos(theta)) / T_sidereal
    """
    # Convert latitude to radians
    theta = math.radians(latitude_degrees)
    
    # Sidereal day in seconds (time for Earth to complete one full 360-degree rotation)
    t_sidereal = 86164.09
    
    # Calculate linear velocity due to rotation
    v_rot = (2 * math.pi * r_earth * math.cos(theta)) / t_sidereal
    return v_rot

# ==========================================
# PART 3: Vector & Advanced Math Operations
# ==========================================
def vector_orbital_velocity(time_in_seconds, period=365.25*24*3600):
    """
    Calculates Earth's x and y velocity components relative to the Sun assuming circular orbit.
    """
    angular_velocity = (2 * math.pi) / period # omega
    v_x = -calculate_orbital_speed(M_sun, r_orbit) * math.sin(angular_velocity * time_in_seconds)
    v_y = calculate_orbital_speed(M_sun, r_orbit) * math.cos(angular_velocity * time_in_seconds)
    return v_x, v_y

# ==========================================
# MAIN EXECUTION & OUTPUT
# ==========================================
def main():
    print("=== Earth Speed Calculator (Physics/AddMath Model) ===\n")
    
    # 1. Orbital Speed
    orbital_speed_mps = calculate_orbital_speed(M_sun, r_orbit)
    orbital_speed_kmps = orbital_speed_mps / 1000
    orbital_speed_kmph = orbital_speed_kmps * 3600
    
    print("1. Earth's Orbital Speed (Moving around the Sun):")
    print(f"   - Velocity: {orbital_speed_kmps:.2f} km/s")
    print(f"   - Velocity: {orbital_speed_kmph:,.2f} km/h\n")
    
    # 2. Rotational Speed (Example with a specific location)
    # Bandar Seri Jempol, Negeri Sembilan, Malaysia is approximately 2.8°N
    my_latitude = 2.8 
    rotational_speed_mps = calculate_rotational_speed(my_latitude)
    rotational_speed_kmph = rotational_speed_mps * 3.6
    
    print(f"2. Earth's Rotational Speed at Latitude {my_latitude}°N:")
    print(f"   - Velocity: {rotational_speed_mps:.2f} m/s")
    print(f"   - Velocity: {rotational_speed_kmph:.2f} km/h\n")
    
    # 3. Vector Demonstration (At Time = 0 Days)
    vx, vy = vector_orbital_velocity(0)
    print("3. Orbital Velocity Components (at time t=0):")
    print(f"   - v_x: {vx:.2f} m/s")
    print(f"   - v_y: {vy:.2f} m/s")

if __name__ == "__main__":
    main()
