# lass-json
lass-json convert online [LASS] mqtt data to json format

### Prerequisite 

```sh
$ pip install paho-mqtt
$ pip install simplejson
```

### Usage

```sh
$ python lass-json.py > output.json 
NOTICE: Connected
NOTICE: Wait 15 seconds to gather MQTT data
NOTICE: 1
NOTICE: 2
NOTICE: 3
NOTICE: 4
NOTICE: 5
NOTICE: 6
NOTICE: 7
NOTICE: 8
NOTICE: 9
NOTICE: 10
NOTICE: 11
NOTICE: 12
NOTICE: 13
NOTICE: 14
NOTICE: 15
NOTICE: Disconnected
```

### output.json

> [
>     {
>         "app": "PM25",
>         "date": "2015-12-13",
>         "device": "LinkItONE",
>         "device_id": "FT1_001",
>         "fmt_opt": "0",
>         "gps_alt": "9",
>         "gps_fix": "1",
>         "gps_lat": "25.023968",
>         "gps_lon": "121.368831",
>         "gps_num": "14",
>         "s_0": "6527.00",
>         "s_1": "100.00",
>         "s_2": "1.00",
>         "s_3": "0.00",
>         "s_4": "1.00",
>         "s_d0": "28.00",
>         "s_d1": "30.00",
>         "s_h0": "56.60",
>         "s_t0": "27.20",
>         "tick": "390080346",
>         "time": "00:55:09",
>         "ver_app": "0.7.13",
>         "ver_format": "3"
>     },
>     {
>         "app": "PM25",
>         "date": "2015-12-13",
>         "device": "LinkItONE",
>         "device_id": "FT1_010",
>         "fmt_opt": "0",
>         "gps_alt": "-1",
>         "gps_fix": "1",
>         "gps_lat": "22.396057",
>         "gps_lon": "120.182182",
>         "gps_num": "5",
>         "s_0": "797.00",
>         "s_1": "100.00",
>         "s_2": "1.00",
>         "s_3": "0.00",
>         "s_4": "1.00",
>         "s_d0": "48.00",
>         "s_d1": "66.00",
>         "s_h0": "62.90",
>         "s_t0": "25.60",
>         "tick": "47634149",
>         "time": "00:55:13",
>         "ver_app": "0.7.13",
>         "ver_format": "3"
>     },
>     {
>         "app": "PM25",
>         "date": "2015-12-13",
>         "device": "LinkItONE",
>         "device_id": "FT1_035",
>         "fmt_opt": "0",
>         "gps_alt": "7",
>         "gps_fix": "1",
>         "gps_lat": "24.353590",
>         "gps_lon": "120.523095",
>         "gps_num": "14",
>         "s_0": "2209.00",
>         "s_1": "100.00",
>         "s_2": "1.00",
>         "s_3": "0.00",
>         "s_4": "1.00",
>         "s_d0": "20.00",
>         "s_d1": "27.00",
>         "s_h0": "87.00",
>         "s_t0": "20.80",
>         "tick": "133499525",
>         "time": "00:55:14",
>         "ver_app": "0.7.13",
>         "ver_format": "3"
>     },
>     {
>         "app": "PM25",
>         "date": "2015-12-13",
>         "device": "LinkItONE",
>         "device_id": "FT1_005",
>         "fmt_opt": "0",
>         "gps_alt": "-",
>         "gps_fix": "1",
>         "gps_lat": "23.508875",
>         "gps_lon": "120.171809",
>         "gps_num": "15",
>         "s_0": "2990.00",
>         "s_1": "100.00",
>         "s_2": "1.00",
>         "s_3": "0.00",
>         "s_d0": "40.00",
>         "s_d1": "55.00",
>         "s_h0": "97.60",
>         "s_t0": "21.20",
>         "tick": "29919301",
>         "time": "00:55:14",
>         "ver_app": "0.7.8",
>         "ver_format": "3"
>     },
>     {
>         "app": "PM25",
>         "date": "2015-12-13",
>         "device": "LinkItONE",
>         "device_id": "FT1_040",
>         "fmt_opt": "0",
>         "gps_alt": "3",
>         "gps_fix": "1",
>         "gps_lat": "25.046063",
>         "gps_lon": "121.292816",
>         "gps_num": "7",
>         "s_0": "2247.00",
>         "s_1": "100.00",
>         "s_2": "1.00",
>         "s_3": "0.00",
>         "s_4": "1.00",
>         "s_d0": "31.00",
>         "s_d1": "47.00",
>         "s_h0": "83.20",
>         "s_t0": "22.70",
>         "tick": "134289457",
>         "time": "00:55:20",
>         "ver_app": "0.7.13",
>         "ver_format": "3"
>     },
>     {
>         "app": "PM25",
>         "date": "2015-12-11",
>         "device": "LinkItONE",
>         "device_id": "FT1_044",
>         "fmt_opt": "0",
>         "gps_alt": "459",
>         "gps_fix": "0",
>         "gps_lat": "25.019861",
>         "gps_lon": "121.271122",
>         "gps_num": "0",
>         "s_0": "2707.00",
>         "s_1": "100.00",
>         "s_2": "1.00",
>         "s_3": "6.82",
>         "s_4": "8.00",
>         "s_d0": "30.00",
>         "s_d1": "35.00",
>         "s_h0": "35.00",
>         "s_t0": "33.90",
>         "tick": "175635041",
>         "time": "17:01:02",
>         "ver_app": "0.7.13",
>         "ver_format": "3"
>     },
>     {
>         "app": "PM25",
>         "date": "2015-12-13",
>         "device": "LinkItONE",
>         "device_id": "FT1_004",
>         "fmt_opt": "0",
>         "gps_alt": "2",
>         "gps_fix": "1",
>         "gps_lat": "23.284064",
>         "gps_lon": "120.275804",
>         "gps_num": "15",
>         "s_0": "19530.00",
>         "s_1": "100.00",
>         "s_2": "1.00",
>         "s_3": "0.00",
>         "s_4": "12.00",
>         "s_d0": "55.00",
>         "s_d1": "71.00",
>         "s_h0": "60.50",
>         "s_t0": "24.20",
>         "tick": "1167983479",
>         "time": "00:55:24",
>         "ver_app": "0.7.13",
>         "ver_format": "3"
>     },
>     {
>         "app": "PM25",
>         "date": "2015-12-13",
>         "device": "LinkItONE",
>         "device_id": "FT1_005",
>         "fmt_opt": "0",
>         "gps_alt": "-",
>         "gps_fix": "1",
>         "gps_lat": "23.508875",
>         "gps_lon": "120.171809",
>         "gps_num": "15",
>         "s_0": "2991.00",
>         "s_1": "100.00",
>         "s_2": "1.00",
>         "s_3": "0.00",
>         "s_d0": "40.00",
>         "s_d1": "53.00",
>         "s_h0": "97.20",
>         "s_t0": "21.20",
>         "tick": "29929294",
>         "time": "00:55:24",
>         "ver_app": "0.7.8",
>         "ver_format": "3"
>     }
> ]

   [LASS]: <https://lass.hackpad.com/>

