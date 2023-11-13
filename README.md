# iotlab-pilotcase-jemac
Jemac Sweden AB is a company based in Kalmar, Sweden. They provide services within development, production, and management. They work with a broad spectrum of commissions for different types of customers and have an extensive network of partners. They also offer products and services that connect you to your things. They can design, set up, and manage the implementation of your complete system including hardware, software, connectivity, cloud services, and user interface. They also develop and design user-friendly apps to control and monitor your thing from any type of device.

# Table of contents
* [iotlab-pilotcase-jemac](#iotlab-pilotcase-jemac)
* [Table of contents](#table-of-contents)
* [Values to measure](#values-to-measure)
   * [Internal Measurements:](#internal-measurements)
   * [External Measurements:](#external-measurements)
* [Hardware suggestions](#hardware-suggestions)
   * [Temperature and humidity](#temperature-and-humidity)
   * [Air quality](#air-quality)
   * [Motion](#motion)

# Values to measure
The concept of a soundproof pod comes with various potential areas of measurement, both internally and externally. These values could be temperature, humidity, multi-faceted air quality, motion, sound, light and fire detection from within, alongside external temperature and sound. All such measurements pave the way to fully understand and improve the pod's performance and efficiency, ensuring optimal user comfort and safety.

## Internal Measurements:
- Temperature
   - Ensures comfort levels for enhanced productivity.
   - Provides early warnings for equipment malfunctions or overheating.
   - Optimizes energy usage through smarter HVAC control.

- Humidity
   - Helps maintain an environment minimising respiratory discomfort or diseases.
   - Protects sensitive equipment from humidity damage.
   - Alerts to potential water leaks within the pod.

- Air Quality (High Priority)
   - Improves overall health by reducing exposure to airborne pollutants.
   - Identifies presence of harmful gases or chemical leaks.
   - Particle sensors detect allergens providing a more accommodative environment for user health.

- Motion Sensing
   - Tracks usage patterns, optimizing energy management.
   - Integrates with emergency systems for improved safety.

- Sound Levels
   - Ensures the pod remains a sound-free zone for focused tasks.
   - Detects anomalies, serving as an alert system for potential equipment issues. 

- Light Intensity
   - Delivers a mood-appropriate environment for varying activities.
   - Reduces eye strain and associated health issues.
   - Optimizes light-based energy consumption.

- Fire Detection
   - Satisfies safety compliance and insurance requirements.
   - Meke sure that person inside pod hears outside fire alarm

## External Measurements:
- Ambient Sound
   - Assesses the pod's soundproofing effectiveness.
   - Alerts to external disruptions or hazards.
   - Provides insights to improve design and materials for better noise isolation.

- Ambient Temperature
   - Regulates internal control systems for a consistent indoor climate.
   - Helps swiftly detect and adapt to outdoor climate changes.
   - Contributes in energy optimization while minimizing wastage.


# Hardware suggestions

## Temperature and humidity
| Sensor | Library | RH accuracy (%RH)| T accuracy (C)| RH range | temp range |Release year|
|--------|---------|------------------|---------------|----------|------------|------------|
|HDC3022-Q1|       |0.5               |0.1            |0-100     |-40-125     |            |
|HDC3022 |         |0.5               |0.1            |0-100     |-40-125     |            |
|HTU21D(F) |       |2                 |               |0-100     |-40-125     |            |

## Air quality

- **CO2**: Measuring Carbon dioxide can be a way to detect if someone is in the pod, as well as a way to know if further ventilation is needed

- **eCO2**:
eCO2: Stands for equivalent Carbon Dioxide, used in measurements for indoor air quality applications, and based primarily on the sensing of VOCs (Volatile Organic Compounds).

- **PM**: A common way to measure particles is to count them by size. PM2.5 and PM 10 are terms used to describe fine particles in the air we breathe. They refer to atmospheric particulate matter (PM) that have a diameter of less than 2.5 micrometers and 10 micrometers, respectively.  Measuring particles can be a way to monitor over all air quality, but also a way to indicate if someone smokes in the pod.

- **VOC**: Volatile Organic compound is a group of chemicals that evaporate easily at room temperature. They are produced by many household products such as paints, aerosols, and cleaners, as well as industrial processes. High levels of VOCs can have harmful effects on health and also contribute to air pollution.
There are air quality sensors available that offer a combination of ways to measure air Quality


- **TVOC**: Total Volatile Organic Compounds refer to the total concentration of multiple airborne VOCs present in the environment at a given time.

- **NOx**: It's the collective term for nitric oxide (NO) and nitrogen dioxide (NO2). They are harmful gases released by burning fuels and can cause respiratory problems and contribute to the formation of smog and acid rain.

- **AQI**: Air Quality Index is a standard scale for reporting and forecasting about air quality. It helps people understand when to reduce outdoor activities if the air quality is unhealthy.

- **VSCs**: Volatile Sulfur Compounds, a category of compounds with a low boiling point, often responsible for unpleasant odors. They can also impact air quality, especially indoors.


| Sensor | Library | CO2 | eCO2 | PM1 | PM2.5 | PM10 | VOC | TVOC | NOx | AQI | VSCs |
|-|-|-|-|-|-|-|-|-|-|-|-|
|[Sensirion - SGP41-D-R4](https://sensirion.com/media/documents/5FE8673C/61E96F50/Sensirion_Gas_Sensors_Datasheet_SGP41.pdf)| - | - | - | - | - | - | ✅ | - | ✅ |-|- | 
|[ScioSense - ENS160](https://www.mouser.com/datasheet/2/1081/SC_001224_DS_1_ENS160_Datasheet_Rev_0_95-2258311.pdf)| - | - | ✅ | - | - | - | - | ✅ | - | ✅ |- | 
|[Adafruit - PMSA003I](https://www.mouser.com/datasheet/2/737/4505_PMSA003I_series_data_manual_English_V2_6-2490334.pdf) | - | - | - | ✅ | ✅ | ✅ | - | - | - | - | - | 
|[Sensirion - SGP30/40](https://docs.rs-online.com/1956/A700000007055193.pdf) | - | - | ✅ | - | - | - | (✅) | ✅ | - | - | - | 
|[Cambridge CMOSSensors  - CCS811](https://www.sciosense.com/wp-content/uploads/documents/SC-001232-DS-3-CCS811B-Datasheet-Revision-2.pdf) | - | - | ✅ | - | - | - | - | ✅ | - | - | - | 
|[Bosch - BME680](https://www.bosch-sensortec.com/products/environmental-sensors/gas-sensors/bme680/) | - | - | - | - | - | - | ✅ | - | - | - | - | 
|[Bosch - BME688](https://www.bosch-sensortec.com/products/environmental-sensors/gas-sensors/bme688/) | - | - | - | - | - | - | ✅ | - | - | - | ✅ | 

## Motion

**Passive Infrared (PIR) Sensors:** These sensors detect body heat, and are commonly used in home security systems. They are passive because they don't emit energy; they simply detect it. Can have false triggers in the form of other heat sources.

**Thermal:** Both the pyroelectric sensor (Often used in PIR) and non-contact MEMS thermal sensor can detect even the slightest amount of radiant energy from objects such as infrared radiation and convert them into temperature readings. However, unlike pyroelectric sensor that relies on motion detection, non-contact MEMS thermal sensor is able to detect the presence of stationary humans (or objects).

**Ultrasonic Sensors:**  These sensors emit ultrasonic waves, and then measure the reflection off a moving object. They are commonly used in automated doors, light switches, or parking sensors in cars.



|Sensor|Technology| Range of detection |Sensitivity|Supply Voltage|
|-|-|-|-|-|
|[Adafruit - 4871](https://www.digikey.se/sv/products/detail/adafruit-industries-llc/4871/13922055?utm_adgroup=&utm_source=google&utm_medium=cpc&utm_campaign=PMAX%20Shopping_Product_High%20Performers&utm_term=&productid=13922055&utm_content=&utm_id=go_cmp-19549529751_adg-_ad-__dev-c_ext-_prd-13922055_sig-Cj0KCQiAr8eqBhD3ARIsAIe-buO9Et8qW-ORiGeWR51faV9cbxzlUNJU7_sIyuduhqKkcgEZOPw_wikaAhTKEALw_wcB&gad_source=1&gclid=Cj0KCQiAr8eqBhD3ARIsAIe-buO9Et8qW-ORiGeWR51faV9cbxzlUNJU7_sIyuduhqKkcgEZOPw_wikaAhTKEALw_wcB)|PIR|7 m|Adjustable|3 - 12|
|[Adafruit - 5578](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/5006/5578_Web.pdf)|PIR|5 m|Adjustable|2.2 - 3.7|
|[Omron - D6T](https://docs.rs-online.com/1ec1/0900766b8165dbfb.pdf)|Thermal|Viewing angle and distance will affect area of detection|Can give info about how many people| 4.5 - 5.5|









| Value to be Measured | Suggested Sensor | Peripheral |
|----------------------|------------------|------------|
| Internal Temperature |                  |            |
| Humidity             |                  |            |
| Air Quality          |                  |            |
| Motion               |                  |            |
| Internal Sound       |                  |            |
| Light Intensity      |                  |            |
| Fire Detection       |                  |            |
| External Sound       |                  |            |
| External Temperature |                  |            |
