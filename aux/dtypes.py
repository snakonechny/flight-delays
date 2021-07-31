import numpy as np

# KNOWN SIDE EFFECT/DONE BY DESIGN - if 'py_dtype' is None, the column type in the dataframe won't be recast
new_cols = {
    "Year": {
        "name": "year",
        "py_dtype": np.int64
    },
    "Quarter": {
        "name": "quarter",
        "py_dtype": np.int64
    },
    "Month": {
        "name": "month",
        "py_dtype": np.int64
    },
    "DayofMonth": {
        "name": "day_of_month",
        "py_dtype": np.int64
    },
    "DayOfWeek": {
        "name": "day_of_week",
        "py_dtype": np.int64
    },
    "FlightDate": {
        "name": "flight_date",
        "py_dtype": None
    },
    "Operating_Airline ": {
        "name": "airline",
        "py_dtype": np.str
    },
    "Tail_Number": {
        "name": "tail",
        "py_dtype": np.str
    },
    "Flight_Number_Operating_Airline": {
        "name": "flight_number",
        "py_dtype": np.str
    },
    "OriginCityMarketID": {
        "name": "origin_market_id",
        "py_dtype": np.str
    },
    "Origin": {
        "name": "origin",
        "py_dtype": np.str
    },
    "OriginCityName": {
        "name": "origin_city_name",
        "py_dtype": np.str
    },
    "OriginStateName": {
        "name": "origin_state_name",
        "py_dtype": np.str
    },
    "OriginWac": {
        "name": "origin_area_code",
        "py_dtype": np.str
    },
    "DestCityMarketID": {
        "name": "dest_market_id",
        "py_dtype": np.str
    },
    "Dest": {
        "name": "dest",
        "py_dtype": np.str
    },
    "DestCityName": {
        "name": "dest_city_name",
        "py_dtype": np.str
    },
    "DestStateName": {
        "name": "dest_state_name",
        "py_dtype": np.str
    },
    "DestWac": {
        "name": "dest_area_code",
        "py_dtype": np.str
    },
    "CRSDepTime": {
        "name": "crs_dep_time",
        "py_dtype": None
    },
    "DepTime": {
        "name": "dep_time",
        "py_dtype": None
    },
    "DepDelay": {
        "name": "dep_delay",
        "py_dtype": None
    },
    "DepDelayMinutes": {
        "name": "dep_delay_minutes",
        "py_dtype": None
    },
    "DepDel15": {
        "name": "dep_delay_15",
        "py_dtype": None
    },
    "DepartureDelayGroups": {
        "name": "dep_delay_groups",
        "py_dtype": None
    },
    "DepTimeBlk": {
        "name": "dep_time_block",
        "py_dtype": np.str
    },
    "TaxiOut": {
        "name": "taxi_out",
        "py_dtype": None
    },
    "WheelsOff": {
        "name": "wheels_off",
        "py_dtype": None
    },
    "WheelsOn": {
        "name": "wheels_on",
        "py_dtype": None
    },
    "TaxiIn": {
        "name": "taxi_in",
        "py_dtype": None
    },
    "CRSArrTime": {
        "name": "crs_arr_time",
        "py_dtype": None
    },
    "ArrTime": {
        "name": "arr_time",
        "py_dtype": None
    },
    "ArrDelay": {
        "name": "arr_delay",
        "py_dtype": None
    },
    "ArrDelayMinutes": {
        "name": "arr_delay_minutes",
        "py_dtype": None
    },
    "ArrDel15": {
        "name": "arr_delay_15",
        "py_dtype": None
    },
    "ArrivalDelayGroups": {
        "name": "arr_delay_groups",
        "py_dtype": None
    },
    "ArrTimeBlk": {
        "name": "arr_time_block",
        "py_dtype": np.str
    },
    "Cancelled": {
        "name": "cancelled",
        "py_dtype": np.int64
    },
    "CancellationCode": {
        "name": "cancellation_code",
        "py_dtype": np.str
    },
    "Diverted": {
        "name": "diverted",
        "py_dtype": np.int64
    },
    "Duplicate": {
        "name": "duplicate",
        "py_dtype": np.str
    },
    "CRSElapsedTime": {
        "name": "crs_elapsed_time",
        "py_dtype": None
    },
    "ActualElapsedTime": {
        "name": "actual_elapsed_time",
        "py_dtype": None
    },
    "AirTime": {
        "name": "air_time",
        "py_dtype": None
    },
    "Flights": {
        "name": "flights",
        "py_dtype": None
    },
    "Distance": {
        "name": "distance",
        "py_dtype": None
    },
    "CarrierDelay": {
        "name": "carrier_delay",
        "py_dtype": None
    },
    "WeatherDelay": {
        "name": "weather_delay",
        "py_dtype": None
    },
    "NASDelay": {
        "name": "nas_delay",
        "py_dtype": None
    },
    "SecurityDelay": {
        "name": "security_delay",
        "py_dtype": None
    },
    "LateAircraftDelay": {
        "name": "late_aircraft_delay",
        "py_dtype": None
    },
    "FirstDepTime": {
        "name": "first_dep_time",
        "py_dtype": None
    },
    "TotalAddGTime": {
        "name": "total_add_gate_time",
        "py_dtype": None
    },
    "LongestAddGTime": {
        "name": "longest_add_gate_time",
        "py_dtype": None
    },
    "DivAirportLandings": {
        "name": "diverted_airport_landings",
        "py_dtype": None
    },
    "DivReachedDest": {
        "name": "diverted_reached_dest",
        "py_dtype": None
    },
    "DivActualElapsedTime": {
        "name": "diverted_actual_elapsed_time",
        "py_dtype": None
    },
    "DivDistance": {
        "name": "diverted_distance",
        "py_dtype": None
    },
    "Div1Airport": {
        "name": "diverted_airport_1",
        "py_dtype": np.str
    },
    "Div1WheelsOn": {
        "name": "diverted_wheels_on_1",
        "py_dtype": None
    },
    "Div1TotalGTime": {
        "name": "diverted_ground_time_1",
        "py_dtype": None
    },
    "Div1LongestGTime": {
        "name": "diverted_longest_gate_time_1",
        "py_dtype": None
    },
    "Div1WheelsOff": {
        "name": "diverted_wheels_off_1",
        "py_dtype": None
    },
    "Div2Airport": {
        "name": "diverted_airport_2",
        "py_dtype": np.str
    },
    "Div2WheelsOn": {
        "name": "diverted_wheels_on_2",
        "py_dtype": None
    },
    "Div2TotalGTime": {
        "name": "diverted_ground_time_2",
        "py_dtype": None
    },
    "Div2LongestGTime": {
        "name": "diverted_longest_gate_time_2",
        "py_dtype": None
    },
    "Div2WheelsOff": {
        "name": "diverted_wheels_off_2",
        "py_dtype": None
    },
    "Div3Airport": {
        "name": "diverted_airport_3",
        "py_dtype": np.str
    },
    "Div3WheelsOn": {
        "name": "diverted_wheels_on_3",
        "py_dtype": None
    },
    "Div3TotalGTime": {
        "name": "diverted_ground_time_3",
        "py_dtype": None
    },
    "Div3LongestGTime": {
        "name": "diverted_longest_gate_time_3",
        "py_dtype": None
    },
    "Div3WheelsOff": {
        "name": "diverted_wheels_off_3",
        "py_dtype": None
    }
}