# Hardware suggestions

## Temperature and humidity
| Sensor | Library | RH accuracy (%RH)| T accuracy (C)| RH range | Temp range | Price (Depends on quantity)|
|--------|---------|------------------|---------------|----------|------------|-------|
|[TI - HDC3022-Q1](https://www.ti.com/lit/ds/symlink/hdc3022-q1.pdf?ts=1699898725445&ref_url=https%253A%252F%252Fwww.ti.com%252Fproduct%252FHDC3022-Q1%253FkeyMatch%253DHDC3022-Q1%2526tisearch%253Dsearch-everything%2526usecase%253DGPN-ALT)|    -   |±0.5               |±0.1            |0-100     |-40-125     | $3.779 (1-99) - 2.054 (1000+)|
|[TI - HDC3022 ](https://www.ti.com/lit/ds/symlink/hdc3022.pdf?ts=1702454356057&ref_url=https%253A%252F%252Fwww.ti.com%252Fproduct%252FHDC3022)|      -   |±0.5               |±0.1            |0-100     |-40-125     | $3.737 (1-99) - 1.850 (1000+)|
|[TI - HTU21D(F)](https://cdn-shop.adafruit.com/datasheets/1899_HTU21D.pdf) |    -   |±2                 |       -        |0-100     |-40-125     | $XX.XX |
|[Bosch - BME680](https://www.bosch-sensortec.com/products/environmental-sensors/gas-sensors/bme680/) | - | ±3 | ±0.5 | 0-100 | -40-85 | $10.71 (1-10) - 5.91(2500+) |


## Air quality


| Sensor | Library | CO2 | eCO2 | PM1 | PM2.5 | PM10 | VOC | TVOC | NOx | AQI | VSCs | Cost ea (100+) |
|--------|---------|-----|------|-----|-------|------|-----|------|-----|-----|------|------|
|[Sensirion - SGP41-D-R4](https://sensirion.com/media/documents/5FE8673C/61E96F50/Sensirion_Gas_Sensors_Datasheet_SGP41.pdf)| - | - | - | - | - | - | ✅ | - | ✅ |-|- | 5,31 €	 |
|[ScioSense - ENS160](https://www.mouser.com/datasheet/2/1081/SC_001224_DS_1_ENS160_Datasheet_Rev_0_95-2258311.pdf)| - | - | ✅ | - | - | - | - | ✅ | - | ✅ |- | 6,08 € |
|[Adafruit - PMSA003I](https://www.mouser.com/datasheet/2/737/4505_PMSA003I_series_data_manual_English_V2_6-2490334.pdf) | - | - | - | ✅ | ✅ | ✅ | - | - | - | - | - |*41,80 €	 |
|[Sensirion - SGP30/40](https://docs.rs-online.com/1956/A700000007055193.pdf) | - | - | ✅ | - | - | - | (✅) | ✅ | - | - | - | N/A, 5,16 € |
|[Cambridge CMOSSensors  - CCS811](https://www.sciosense.com/wp-content/uploads/documents/SC-001232-DS-3-CCS811B-Datasheet-Revision-2.pdf) | - | - | ✅ | - | - | - | - | ✅ | - | - | - | - |
|[Bosch - BME680](https://www.bosch-sensortec.com/products/environmental-sensors/gas-sensors/bme680/) | - | - | - | - | - | - | - | - | - | ✅ | - | 6,37 €	 |
|[Bosch - BME688](https://www.bosch-sensortec.com/products/environmental-sensors/gas-sensors/bme688/) | - | - | - | - | - | - | ✅ | - | - | - | ✅ | 6,85 €	 |

All prices are fetched from [Mouser](https://www.mouser.se/). The prices for individual sensors, and are for when over 100 units are purchased. The prices are fetched 2021-10-13.

Prices that start with a * are regular prices and do not change with quantity.

## Motion

| Sensor | Technology | Range of detection (m) | Sensitivity | Supply (V) | Cost eac (100+) |
|--------|------------|------------------------|-------------|------------|------|
|[Adafruit - 5578](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/5006/5578_Web.pdf)|PIR|5 m|Adjustable|2.2 - 3.7| *1,81 €	 |
|[muRata - IRA-S410ST01](https://www.murata.com/~/media/webrenewal/products/sensor/infrared/ira/ira-s410st01-e.ashx?la=en)|PIR|||2-15| 1,73 €	|
|[Zilog - ZRE200GE](https://www.zilog.com/docs/zmotion/PS0402.pdf)|PIR|||1 - 15| 0,958 € |
|[Omron - D6T](https://docs.rs-online.com/1ec1/0900766b8165dbfb.pdf)|Thermal|Viewing angle and distance will affect area of detection|Can give info about how many people| 4.5 - 5.5| *26,18 €|
|[RSPRO - Barrel-Style Proximity Sensor](https://docs.rs-online.com/c0bf/0900766b816c0809.pdf)|Ultrasonic|0-0.3||? - 20| - |
|[muRata - MA40S4S](https://www.murata.com/en-us/products/productdata/8797589340190/MASPOPSE.pdf)|Ultrasonic (TRANS)||||3,79 €	 |
|[muRata - MA40S4R](https://www.murata.com/en-us/products/productdata/8797589274654/MASPOPRE.pdf)|Ultrasonic (RCVR)|||| 3,51 €	|

All prices are fetched from [Mouser](https://www.mouser.se/). The prices for individual sensors, and are for when over 100 units are purchased. The prices are fetched 2021-10-13.

Prices that start with a * are either regular prices and do not change with quantity or for quantities less than 100 pieces.


