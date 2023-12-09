def read_input_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        seeds = list(map(int, lines[0].split()[1:]))
        
        seed_to_soil_map = [list(map(int, line.split())) for line in lines[3:5]]
        soil_to_fertilizer_map = [list(map(int, line.split())) for line in lines[7:10]]
        fertilizer_to_water_map = [list(map(int, line.split())) for line in lines[12:16]]
        water_to_light_map = [list(map(int, line.split())) for line in lines[18:20]]
        light_to_temperature_map = [list(map(int, line.split())) for line in lines[22:25]]
        temperature_to_humidity_map = [list(map(int, line.split())) for line in lines[27:29]]
        humidity_to_location_map = [list(map(int, line.split())) for line in lines[31:33]]

        maps = {
            "seed_to_soil": seed_to_soil_map,
            "soil_to_fertilizer": soil_to_fertilizer_map,
            "fertilizer_to_water": fertilizer_to_water_map,
            "water_to_light": water_to_light_map,
            "light_to_temperature": light_to_temperature_map,
            "temperature_to_humidity": temperature_to_humidity_map,
            "humidity_to_location": humidity_to_location_map
        }

        return seeds, maps

file_path = "test.txt"  # Replace with the actual path to your file
seeds, maps = read_input_file(file_path)

print("Seeds:", seeds)
print("Maps:")
for key, value in maps.items():
    print(key + ":", value)
