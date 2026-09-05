# PUBG_No_Recoil_Script
Works respectively for M416 , AUG , AKM , M249 .
This is the simplest hack you can find anywhere. This app pulls your mouse down when you shoot so your vertical recoil compansates.

This Python code will start pushing your mouse down whenyou click the left mouse button but first you need to choose your gun .Pushing the left back button on logitech gaming mouse will trigger the app and switches your gun mode between M416 , AUG , AKM , M249.
You can take this code and run it in your own device .  Your current gun is shown on the screen. F12 ends the process. You can prefer different buttons and change them in the code.

You are probibly get banned after some time.

Before running the script your in-game sensitivities must be calibrated.  

<img width="626" height="425" alt="Screenshot 2026-09-02 180530" src="https://github.com/user-attachments/assets/b1f45f6d-38d3-499f-90d0-5eef1c834b9e" />


### Recoil Per-Shot Bullet for M416

The table below lists the instantaneous angular offset per single round.

| Shot # | Vertical Pitch ($\Delta^\circ$) | Horizontal Yaw ($\pm^\circ$) | Phase Description |
| :---: | :---: | :---: | :--- |
| **1** | 0.4400° | ±0.0750° | High first-shot jump |
| **2** | 0.4650° | ±0.0820° | Recoil recovery / initial reset |
| **3** | 0.4900° | ±0.0910° | Linear ramp starts |
| **4** | 0.5150° | ±0.1000° | Early pattern formation |
| **5** | 0.5400° | ±0.1120° | Initial spray stabilization |
| **6** | 0.5650° | ±0.1250° | Horizontal sway expansion |
| **7** | 0.5900° | ±0.1380° | Steady climb interval |
| **8** | 0.6150° | ±0.1490° | Steady climb interval |
| **9** | 0.6400° | ±0.1600° | Steady climb interval |
| **10** | 0.6650° | ±0.1700° | End of primary cluster |
| **11** | 0.7200° | ±0.1850° | Phase 2 transition |
| **12** | 0.7650° | ±0.1980° | Increased vertical pull |
| **13** | 0.8100° | ±0.2100° | Mid-spray ramp |
| **14** | 0.8500° | ±0.2220° | Mid-spray ramp |
| **15** | 0.8850° | ±0.2330° | Sustained acceleration |
| **16** | 0.9200° | ±0.2440° | Sustained acceleration |
| **17** | 0.9500° | ±0.2540° | Approaching upper group |
| **18** | 0.9800° | ±0.2630° | Near 1.0° boundary |
| **19** | 1.0100° | ±0.2710° | Entering high-deviation band |
| **20** | 1.0350° | ±0.2780° | End of mid-spray phase |
| **21** | 1.0900° | ±0.2850° | Near-peak saturation |
| **22** | 1.1100° | ±0.2910° | Near-peak saturation |
| **23** | 1.1250° | ±0.2960° | Asymptotic rise |
| **24** | 1.1350° | ±0.3000° | Asymptotic rise |
| **25** | 1.1420° | ±0.3030° | Saturation approach |
| **26** | 1.1460° | ±0.3050° | Saturation approach |
| **27** | 1.1480° | ±0.3070° | Sub-threshold limit |
| **28** | 1.1490° | ±0.3080° | Sub-threshold limit |
| **29** | 1.1495° | ±0.3090° | Convergence point |
| **30–40** | 1.1500° | ±0.3100° | Hard clamp ceiling |

### Recoil Per-Shot Bullet for AUG

The table below lists the instantaneous angular offset per single round in sequence.

| Shot | Vertical Pitch | Horizontal Yaw | Phase Description |
| :---: | :---: | :---: | :--- |
| 1 | 0.4150° | ±0.0884° | First-shot climb |
| 2 | 0.4820° | ±0.1020° | Rapid acceleration begins |
| 3 | 0.5210° | ±0.1130° | Vertical acceleration growth |
| 4 | 0.5580° | ±0.1210° | Acceleration peak |
| 5 | 0.5850° | ±0.1300° | Early spray stabilization |
| 6 | 0.6020° | ±0.1410° | Horizontal sway variance widens |
| 7 | 0.6150° | ±0.1500° | Rounds 1–10 Avg Pitch: ~0.5858° (46.2%) |
| 8 | 0.6280° | ±0.1620° | Linear pitch increase |
| 9 | 0.6400° | ±0.1710° | Linear pitch increase |
| 10 | 0.6520° | ±0.1800° | End of first 10-round group |
| 11 | 0.7210° | ±0.2010° | Phase 2 climb onset |
| 12 | 0.7850° | ±0.2120° | Noticeable jump in vertical kick |
| 13 | 0.8400° | ±0.2230° | Steady climb |
| 14 | 0.8900° | ±0.2350° | Steady climb |
| 15 | 0.9320° | ±0.2460° | High climb interval |
| 16 | 0.9650° | ±0.2550° | Rounds 11–20 Avg Pitch: ~0.9497° (74.9%) |
| 17 | 0.9900° | ±0.2640° | Approaching 1.0° barrier |
| 18 | 1.0120° | ±0.2710° | High recoil threshold |
| 19 | 1.0350° | ±0.2780° | Approaching saturation |
| 20 | 1.0500° | ±0.2820° | End of mid-spray group |
| 21 | 1.1970° | ±0.2910° | Peak impulse onset |
| 22 | 1.2150° | ±0.2950° | Near maximum climb limit |
| 23 | 1.2300° | ±0.2980° | Heavy saturation |
| 24 | 1.2420° | ±0.3010° | Heavy saturation |
| 25 | 1.2510° | ±0.3030° | Rounds 21–40 Avg Pitch: ~1.1970° (94.4%) |
| 26 | 1.2580° | ±0.3050° | Asymptotic rise |
| 27 | 1.2620° | ±0.3060° | Asymptotic rise |
| 28 | 1.2650° | ±0.3070° | Asymptotic rise |
| 29 | 1.2670° | ±0.3075° | Threshold convergence |
| 30–40 | 1.2680° | ±0.3078° | Hard maximum clamp (Max Climb & Sway) |

### Recoil Per-Shot Bullet for AKM

The table below lists the instantaneous angular offset per single round in sequence.

| Shot | Vertical Pitch | Horizontal Yaw | Phase Description |
| :---: | :---: | :---: | :--- |
| 1 | 0.5800° | ±0.0950° | Heavy first-shot kick |
| 2 | 0.6200° | ±0.1100° | Rapid vertical climb |
| 3 | 0.6650° | ±0.1250° | Strong acceleration phase |
| 4 | 0.7100° | ±0.1400° | Sustained vertical impulse |
| 5 | 0.7550° | ±0.1550° | Early spray grouping |
| 6 | 0.7950° | ±0.1700° | Horizontal sway begins widening |
| 7 | 0.8350° | ±0.1850° | High torque climb |
| 8 | 0.8750° | ±0.2000° | High torque climb |
| 9 | 0.9150° | ±0.2150° | Approaching 1.0° threshold |
| 10 | 0.9500° | ±0.2300° | End of primary burst phase |
| 11 | 1.0500° | ±0.2500° | Transition to mid-spray climb |
| 12 | 1.1100° | ±0.2650° | Heavy angular jump |
| 13 | 1.1650° | ±0.2800° | High upward force |
| 14 | 1.2150° | ±0.2950° | Sustained climb interval |
| 15 | 1.2600° | ±0.3100° | Sustained climb interval |
| 16 | 1.3000° | ±0.3250° | Mid-spray ramp peak |
| 17 | 1.3350° | ±0.3400° | Pronounced horizontal spread |
| 18 | 1.3650° | ±0.3550° | High recoil threshold |
| 19 | 1.3900° | ±0.3700° | Approaching saturation phase |
| 20 | 1.4100° | ±0.3800° | End of mid-spray phase |
| 21 | 1.4600° | ±0.3950° | Peak vertical impulse onset |
| 22 | 1.4850° | ±0.4050° | Near-limit rise |
| 23 | 1.5050° | ±0.4150° | Heavy saturation |
| 24 | 1.5200° | ±0.4200° | Heavy saturation |
| 25 | 1.5300° | ±0.4250° | Upper boundary convergence |
| 26 | 1.5380° | ±0.4280° | Asymptotic saturation |
| 27 | 1.5440° | ±0.4300° | Asymptotic saturation |
| 28 | 1.5470° | ±0.4320° | Asymptotic saturation |
| 29 | 1.5490° | ±0.4330° | Limit convergence |
| 30–40 | 1.5500° | ±0.4350° | Hard clamp ceiling (Maximum Climb & Yaw) |

### Recoil Per-Shot Bullet for M249

The table below lists the instantaneous angular offset per single round in sequence (standing fire mode, standard/extended magazine profile).

| Shot | Vertical Pitch | Horizontal Yaw | Phase Description |
| :---: | :---: | :---: | :--- |
| 1 | 0.4000° | ±0.0700° | Mild initial jump |
| 2 | 0.4250° | ±0.0800° | Rapid cyclic acceleration |
| 3 | 0.4500° | ±0.0920° | Linear ramp starts |
| 4 | 0.4750° | ±0.1050° | Early pattern formation |
| 5 | 0.5000° | ±0.1180° | Stabilization window |
| 6 | 0.5250° | ±0.1320° | Gradual climb |
| 7 | 0.5500° | ±0.1470° | Gradual climb |
| 8 | 0.5750° | ±0.1600° | Sustained burst phase |
| 9 | 0.6000° | ±0.1750° | Sustained burst phase |
| 10 | 0.6250° | ±0.1900° | End of low-recoil initial cluster |
| 11 | 0.7000° | ±0.2200° | Phase 2 climb transition |
| 12 | 0.7400° | ±0.2350° | Vertical impulse increases |
| 13 | 0.7800° | ±0.2500° | Linear climb |
| 14 | 0.8150° | ±0.2650° | Linear climb |
| 15 | 0.8500° | ±0.2800° | Continuous climb |
| 16 | 0.8800° | ±0.2950° | Continuous climb |
| 17 | 0.9100° | ±0.3100° | Horizontal sway expansion |
| 18 | 0.9350° | ±0.3250° | High-rate climb band |
| 19 | 0.9600° | ±0.3400° | High-rate climb band |
| 20 | 0.9800° | ±0.3550° | End of mid-spray phase |
| 21 | 1.0500° | ±0.3750° | Upper cluster transition |
| 22 | 1.0800° | ±0.3900° | Heavy vertical drag |
| 23 | 1.1050° | ±0.4050° | Sustained LMG climb |
| 24 | 1.1250° | ±0.4180° | High sustained recoil |
| 25 | 1.1400° | ±0.4300° | Approaching primary ceiling |
| 26 | 1.1520° | ±0.4400° | Yaw instability increases |
| 27 | 1.1620° | ±0.4500° | Yaw instability increases |
| 28 | 1.1700° | ±0.4580° | Pre-clamp phase |
| 29 | 1.1760° | ±0.4650° | Pre-clamp phase |
| 30–75 | 1.1800° | ±0.4700° | Sustained fire saturation limit |
| 76–150 | 1.1800° | ±0.4850° | Hard clamp ceiling (Maximum Horizontal Dispersion) |


<img width="1280" height="800" alt="Screenshot 2026-09-05 204531" src="https://github.com/user-attachments/assets/653c56de-46fa-4411-9e6d-a6fadfac5601" />

