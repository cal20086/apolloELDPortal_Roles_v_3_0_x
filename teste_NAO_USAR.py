#               apollo Web Portal - Test Control page


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service



#               Variables
driverModelTestControl = 0

contol_Reportfile = 0
test_Case_Type = "Regression"

carrier = ["QATest1"]
truckDriversList = ["All",
                    "QADriver1 (qadriver1)",
                    "QADriver2 (qadriver2)",
                    "QADriver3 (qadriver3)"]

siteAddressVar = "http://10.1.10.33:8082/Login.aspx?ReturnUrl=%2fDefault.aspx"

driverListName = ["Chrome",
                  "Opera",
                  "Edge",
                  "Firefox"
                  ]

driverListVersion = ["99.0.4896.20 (Official Build) (64-bit)", "83.0.4254.27 (64-bit)",
                     "98.0.1108.43 (Official build) (64-bit", "94.0.2 (64-bit)"
                     ]

driverDriverListVar = ["C:\\tools\chromedriver.exe",
                       "C:\\tools\operadriver.exe",
                       "C:\\tools\msedgedriver.exe",
                       "C:\\tools\geckodriver.exe"]


driverService = Service("C:\\tools\chromedriver.exe")

driver = webdriver.Chrome(service=driverService)
#driver = webdriver.Opera(executable_path= "C:\\tools\operadriver.exe")
#driver = webdriver.Edge(executable_path = "C:\\tools\msedgedriver.exe")
#driver = webdriver.Firefox(executable_path = "C:\\tools\geckodriver.exe")




driver.get(siteAddressVar)
