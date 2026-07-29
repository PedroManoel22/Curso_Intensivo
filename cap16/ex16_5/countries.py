from pygal_maps_world.i18n import COUNTRIES

codes = []
for country_code in sorted(COUNTRIES.keys()):
    codes.append(country_code)
    print(f"{country_code}: {COUNTRIES[country_code]}")
