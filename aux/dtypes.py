import numpy as np

cols_map = {
    "Year": {
        "name": "year",
        "py_dtype": np.int64,
        "nullable": True
    },
    "Quarter": {
        "name": "quarter",
        "py_dtype": np.int64,
        "nullable": True
    },
    "Month": {
        "name": "month",
        "py_dtype": np.int64,
        "nullable": True
    },
    "DayofMonth": {
        "name": "day_of_month",
        "py_dtype": np.int64,
        "nullable": True
    },
    "DayOfWeek": {
        "name": "day_of_week",
        "py_dtype": np.int64,
        "nullable": True
    },
    "FlightDate": {
        "name": "flight_date",
        "py_dtype": None,
        "format": "%Y-%m-%d",
        "nullable": True
    },
    "Operating_Airline ": {
        "name": "airline",
        "py_dtype": np.str,
        "nullable": True
    },
    "Tail_Number": {
        "name": "tail",
        "py_dtype": np.str,
        "nullable": True
    },
    "Flight_Number_Operating_Airline": {
        "name": "flight_number",
        "py_dtype": np.str,
        "nullable": True
    },
    "OriginCityMarketID": {
        "name": "origin_market_id",
        "py_dtype": np.int64,
        "nullable": True
    },
    "Origin": {
        "name": "origin",
        "py_dtype": np.str,
        "nullable": True
    },
    "OriginCityName": {
        "name": "origin_city_name",
        "py_dtype": np.str,
        "nullable": True
    },
    "OriginStateName": {
        "name": "origin_state_name",
        "py_dtype": np.str,
        "nullable": True
    },
    "OriginWac": {
        "name": "origin_area_code",
        "py_dtype": np.str,
        "nullable": True
    },
    "DestCityMarketID": {
        "name": "dest_market_id",
        "py_dtype": np.str,
        "nullable": True
    },
    "Dest": {
        "name": "dest",
        "py_dtype": np.str,
        "nullable": True
    },
    "DestCityName": {
        "name": "dest_city_name",
        "py_dtype": np.str,
        "nullable": True
    },
    "DestStateName": {
        "name": "dest_state_name",
        "py_dtype": np.str,
        "nullable": True
    },
    "DestWac": {
        "name": "dest_area_code",
        "py_dtype": np.str,
        "nullable": True
    },
    "CRSDepTime": {
        "name": "crs_dep_time",
        "py_dtype": np.float64,
        "nullable": True
    },
    "DepTime": {
        "name": "dep_time",
        "py_dtype": np.float64,
        "nullable": False
    },
    "DepDelay": {
        "name": "dep_delay",
        "py_dtype": np.float64,
        "nullable": True
    },
    "DepDelayMinutes": {
        "name": "dep_delay_minutes",
        "py_dtype": np.float64,
        "nullable": True
    },
    "DepDel15": {
        "name": "dep_delay_15",
        "py_dtype": np.float64,
        "nullable": True
    },
    "DepartureDelayGroups": {
        "name": "dep_delay_groups",
        "py_dtype": np.float64,
        "nullable": True
    },
    "DepTimeBlk": {
        "name": "dep_time_block",
        "py_dtype": np.str,
        "nullable": True
    },
    "TaxiOut": {
        "name": "taxi_out",
        "py_dtype": np.int64,
        "nullable": True
    },
    "WheelsOff": {
        "name": "wheels_off",
        "py_dtype": np.int64,
        "nullable": True
    },
    "WheelsOn": {
        "name": "wheels_on",
        "py_dtype": np.int64,
        "nullable": True
    },
    "TaxiIn": {
        "name": "taxi_in",
        "py_dtype": np.int64,
        "nullable": True
    },
    "CRSArrTime": {
        "name": "crs_arr_time",
        "py_dtype": np.float64,
        "nullable": True
    },
    "ArrTime": {
        "name": "arr_time",
        "py_dtype": np.float64,
        "nullable": False
    },
    "ArrDelay": {
        "name": "arr_delay",
        "py_dtype": np.int64,
        "nullable": True
    },
    "ArrDelayMinutes": {
        "name": "arr_delay_minutes",
        "py_dtype": np.int64,
        "nullable": True
    },
    "ArrDel15": {
        "name": "arr_delay_15",
        "py_dtype": np.int64,
        "nullable": True
    },
    "ArrivalDelayGroups": {
        "name": "arr_delay_groups",
        "py_dtype": np.int64,
        "nullable": True
    },
    "ArrTimeBlk": {
        "name": "arr_time_block",
        "py_dtype": np.str,
        "nullable": True
    },
    "Cancelled": {
        "name": "cancelled",
        "py_dtype": np.int64,
        "nullable": True
    },
    "CancellationCode": {
        "name": "cancellation_code",
        "py_dtype": np.int64,
        "nullable": True
    },
    "Diverted": {
        "name": "diverted",
        "py_dtype": np.int64,
        "nullable": True
    },
    "Duplicate": {
        "name": "duplicate",
        "py_dtype": np.int64,
        "nullable": True
    },
    "CRSElapsedTime": {
        "name": "crs_elapsed_time",
        "py_dtype": np.float64,
        "nullable": True
    },
    "ActualElapsedTime": {
        "name": "actual_elapsed_time",
        "py_dtype": np.float64,
        "nullable": True
    },
    "AirTime": {
        "name": "air_time",
        "py_dtype": np.float64,
        "nullable": True
    },
    "Flights": {
        "name": "flights",
        "py_dtype": np.int64,
        "nullable": True
    },
    "Distance": {
        "name": "distance",
        "py_dtype": np.int64,
        "nullable": True
    },
    "CarrierDelay": {
        "name": "carrier_delay",
        "py_dtype": np.float64,
        "nullable": True
    },
    "WeatherDelay": {
        "name": "weather_delay",
        "py_dtype": np.float64,
        "nullable": True
    },
    "NASDelay": {
        "name": "nas_delay",
        "py_dtype": np.float64,
        "nullable": True
    },
    "SecurityDelay": {
        "name": "security_delay",
        "py_dtype": np.float64,
        "nullable": True
    },
    "LateAircraftDelay": {
        "name": "late_aircraft_delay",
        "py_dtype": np.float64,
        "nullable": True
    },
    "FirstDepTime": {
        "name": "first_dep_time",
        "py_dtype": np.float64,
        "nullable": True
    },
    "TotalAddGTime": {
        "name": "total_add_gate_time",
        "py_dtype": np.float64,
        "nullable": True
    },
    "LongestAddGTime": {
        "name": "longest_add_gate_time",
        "py_dtype": np.float64,
        "nullable": True
    },
    "DivAirportLandings": {
        "name": "diverted_airport_landings",
        "py_dtype": np.float64,
        "nullable": True
    },
    "DivReachedDest": {
        "name": "diverted_reached_dest",
        "py_dtype": np.float64,
        "nullable": True
    },
    "DivActualElapsedTime": {
        "name": "diverted_actual_elapsed_time",
        "py_dtype": np.float64,
        "nullable": True
    },
    "DivDistance": {
        "name": "diverted_distance",
        "py_dtype": np.float64,
        "nullable": True
    },
    "Div1Airport": {
        "name": "diverted_airport_1",
        "py_dtype": np.str,
        "nullable": True
    },
    "Div1WheelsOn": {
        "name": "diverted_wheels_on_1",
        "py_dtype": np.float64,
        "nullable": True
    },
    "Div1TotalGTime": {
        "name": "diverted_ground_time_1",
        "py_dtype": np.float64,
        "nullable": True
    },
    "Div1LongestGTime": {
        "name": "diverted_longest_gate_time_1",
        "py_dtype": np.float64,
        "nullable": True
    },
    "Div1WheelsOff": {
        "name": "diverted_wheels_off_1",
        "py_dtype": np.float64,
        "nullable": True
    },
    "Div1WheelsOff": {
        "name": "diverted_tail_1",
        "py_dtype": np.str,
        "nullable": True
    },
    "Div2Airport": {
        "name": "diverted_airport_2",
        "py_dtype": np.str,
        "nullable": True
    },
    "Div2WheelsOn": {
        "name": "diverted_wheels_on_2",
        "py_dtype": np.float64,
        "nullable": True
    },
    "Div2TotalGTime": {
        "name": "diverted_ground_time_2",
        "py_dtype": np.float64,
        "nullable": True
    },
    "Div2LongestGTime": {
        "name": "diverted_longest_gate_time_2",
        "py_dtype": np.float64,
        "nullable": True
    },
    "Div2WheelsOff": {
        "name": "diverted_wheels_off_2",
        "py_dtype": np.float64,
        "nullable": True
    },
    "Div2WheelsOff": {
        "name": "diverted_tail_2",
        "py_dtype": np.str,
        "nullable": True
    },
    "Div3Airport": {
        "name": "diverted_airport_3",
        "py_dtype": np.str,
        "nullable": True
    },
    "Div3WheelsOn": {
        "name": "diverted_wheels_on_3",
        "py_dtype": np.float64,
        "nullable": True
    },
    "Div3TotalGTime": {
        "name": "diverted_ground_time_3",
        "py_dtype": np.float64,
        "nullable": True
    },
    "Div3LongestGTime": {
        "name": "diverted_longest_gate_time_3",
        "py_dtype": np.float64,
        "nullable": True
    },
    "Div3WheelsOff": {
        "name": "diverted_wheels_off_3",
        "py_dtype": np.float64,
        "nullable": True
    },
    "Div3WheelsOff": {
        "name": "diverted_tail_3",
        "py_dtype": np.float64,
        "nullable": True
    }
}