LEC BILL & UNIT ESTIMATOR — RUN GUIDE

Files:
- lec_bill_unit_estimator.py: Python source code
- LEC_Bill_Unit_Estimator_Presentation.pptx: 12-slide presentation
- program_execution_screenshot.png: terminal demonstration screenshot
- demo_output.txt: text output from the same test run

How to run:
1. Install Python 3.
2. Open a terminal in this folder.
3. Run: python lec_bill_unit_estimator.py
4. Enter the purchase information when prompted.
5. Enter appliance information. Press Enter at the appliance-name prompt to finish.

Sample purchase:
20 USD × 200 = 4,000 LRD
4,000 − 100 service fee = 3,900 LRD
3,900 ÷ 25 tariff = 156 kWh

The sample execution screenshot uses:
- 2 LED bulbs, 10 W each, 8 hours/day
- 1 fan, 75 W, 12 hours/day
- 1 TV, 120 W, 6 hours/day
Daily consumption = 0.16 + 0.90 + 0.72 = 1.78 kWh/day
Estimated duration = 156 ÷ 1.78 = 87.64 days



