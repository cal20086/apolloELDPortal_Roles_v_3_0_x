#               apollo Web Portal - Test Control page


from selenium import webdriver
import os
import test_Global_Variables_apolloWebPortal
import time
from datetime import datetime

import test_LoginPage_apolloWebPortal
import test_HomePage_apolloWebPortal
import test_ManagePage_apolloWebPortal
import test_CarrierDetails_ManagePage_apolloWebPortal
import test_CarrierDrivers_ManagePage_apolloWebPortal
import test_HomeBases_ManagePage_apolloWebPortal
import test_Notifications_ManagePage_apolloWebPortal
import test_Assets_ManagePage_apolloWebPortal
import test_DVIR_ManagePage_apolloWebPortal
import test_DVIR_WorkOrder_ManagePage_apolloWebPortal
import test_WorkOrder_ManagePage_apolloWebPortal
import test_WorkOrder_Flow_apolloWebPortal
import test_Report_Categories_Defects_FIELDSInterchanges_apolloWebPortal
import test_Enhanced_IFTAPage_apolloWebPortal
import test_Administration_Roles_ManagePage_apolloWebPortal
import test_Hierarchy_User_Access_ManagePage_apolloWebPortal
import test_Global_Variables_apolloWebPortal
import tc_reports

#from selenium.webdriver.edge.service import Service
#from selenium.webdriver.firefox.service import Service
#from selenium.webdriver.safari.service import Service


#               Open driver & Explicit:

#               Global Variables
global testCaseCounter_Global
#testCaseCounter_Global = 0


#               Variables
driverModelTestControl = 0

contol_Reportfile = 0
test_Case_Type = "Regression"

carrier = ["QATest1"]
truckDriversList = ["All",
                    "QADriver1 (qadriver1)",
                    "QADriver2 (qadriver2)",
                    "QADriver3 (qadriver3)"]

# Site Development
#siteAddressVar = "http://10.1.10.33:8082/Login.aspx?ReturnUrl=%2fDefault.aspx"
# Site Development - Mirror alive
siteAddressVar = "http://10.1.10.33/Login.aspx?ReturnUrl=%2fDefault.aspx"


driverListName = ["Chrome",
                  "Firefox",
                  "Edge",
                  "Opera"
                  ]

driverListVersion = ["99.0.4896.20 (Official Build) (64-bit)", "83.0.4254.27 (64-bit)",
                     "98.0.1108.43 (Official build) (64-bit", "94.0.2 (64-bit)"
                     ]

driverDriverListVar = ["C:\\tools\chromedriver.exe",
                       "C:\\tools\geckodriver.exe",
                       "C:\\tools\msedgedriver.exe",
                       "C:\\tools\operadriver.exe"]




user_ApolloWebPortalListVar = ["qauser1",
                               "qauser2",
                               "qauser3",
                               "qauser4",
                               "qauser5"]

password_ApolloWebPortalListVar = ["qauser1",
                                   "qauser2",
                                   "qauser3",
                                   "qauser4",
                                   "qauser5"]


carrier = ["QATest1"]
truckDriversList = ["QADriver1 (qadriver1)",
                    "QADriver2 (qadriver2)",
                    "QADriver3 (qadriver3)",
                    "All"]
reportFolder_Path_QAReports = "C:/apollo QA Reports/apollo Web Portal/"


driver_UserName_Var = "Test (sdsd1)"
client_Name_Var = "Carrier Test"
client_Adress_Var = "11111 NE 11st Doral 33150"
defect_Vehicle_List_Var = ("Refrigeration Unit", "Part 1. Air Brake System", "(b) air loss rate exceeds prescribed limit", "Part 19. Steering", "(b) steering wheel lash(free - play) exceeds prescribed limitd")
workOrder_CreatedBy_Var = "carlos.liguori@assuredtechmatics.com"
workOrder_Contacts_Var = ("vendor@vendor.com")




#####################################################################################################################################
#                                                        Main functions                                                             #
#####################################################################################################################################

dateInit = datetime.now()
# Delete all previous reports files
for f in os.listdir(reportFolder_Path_QAReports):
    os.remove(os.path.join(reportFolder_Path_QAReports, f))


while driverModelTestControl < 1:

    if driverModelTestControl == 0:
        from selenium.webdriver.chrome.service import Service
        driver = webdriver.Chrome(service=Service(driverDriverListVar[driverModelTestControl]))
    if driverModelTestControl == 1:
        from selenium.webdriver.firefox.service import Service
        driver = webdriver.Firefox(service=Service(driverDriverListVar[driverModelTestControl]))
    if driverModelTestControl == 2:
        from selenium.webdriver.edge.service import Service
        driver = webdriver.Edge(service=Service(driverDriverListVar[driverModelTestControl]))
    if driverModelTestControl == 3:
        from selenium.webdriver.opera.service import Service
        driver = webdriver.Opera(service=Service(driverDriverListVar[driverModelTestControl]))
    if driverModelTestControl > 3:
        breack(1)

    dateInitbyDriver = datetime.now()
    driver_Name = driverListName[driverModelTestControl]
    driver_Version = driverListVersion[driverModelTestControl]
    user_ApolloWebPortalVar = user_ApolloWebPortalListVar[driverModelTestControl]
    password_ApolloWebPortalVar = password_ApolloWebPortalListVar[driverModelTestControl]

    print(driverModelTestControl)
    print(driver_Name)

# Call Functions:


    test_Global_Variables_apolloWebPortal.global_Variables()
    test_LoginPage_apolloWebPortal.login_apolloWebPortal(contol_Reportfile, driver, driver_Name, driver_Version, user_ApolloWebPortalVar, password_ApolloWebPortalVar, siteAddressVar, test_Case_Type)
    test_HomePage_apolloWebPortal.homePage(driver, driver_Name, driver_Version)
    test_ManagePage_apolloWebPortal.managePage(driver, driver_Name, driver_Version)


#    test_CarrierDetails_ManagePage_apolloWebPortal.carrierDetail_ChildMenu_ManagePage(driver, driver_Name, driver_Version, carrier, truckDriversList, driver_UserName_Var, client_Name_Var, client_Adress_Var)
#    test_CarrierDrivers_ManagePage_apolloWebPortal.carrierDrivers_ChildMenu_ManagePage(driver, driver_Name, driver_Version)
#    test_HomeBases_ManagePage_apolloWebPortal.carrierHomeBases_ChildMenu_ManagePage (driver, driver_Name, driver_Version)
    test_Assets_ManagePage_apolloWebPortal.carrierAssets_ChildMenu_ManagePage(driver, driver_Name, driver_Version)
#    test_Notifications_ManagePage_apolloWebPortal.carrierNotifications_ChildMenu_ManagePage (driver, driver_Name, driver_Version)
#    test_DVIR_ManagePage_apolloWebPortal.DVIR_ManagePage(driver, driver_Name, driver_Version, carrier, truckDriversList)
#    test_DVIR_WorkOrder_ManagePage_apolloWebPortal.DVIR_WorkOrder_ManagePage(driver, driver_Name, driver_Version, carrier, truckDriversList, driver_UserName_Var, client_Name_Var, client_Adress_Var, defect_Vehicle_List_Var, workOrder_CreatedBy_Var, workOrder_Contacts_Var)
#    test_WorkOrder_ManagePage_apolloWebPortal.WorkOrder_ManagePage (driver, driver_Name, driver_Version, carrier, truckDriversList, driver_UserName_Var, client_Name_Var, client_Adress_Var, defect_Vehicle_List_Var, workOrder_CreatedBy_Var, workOrder_Contacts_Var)
#    test_WorkOrder_Flow_apolloWebPortal.WorkOrder_Flow_ManagePage (driverModelTestControl, driver, driver_Name, driver_Version, carrier, truckDriversList, driver_UserName_Var, client_Name_Var, client_Adress_Var, defect_Vehicle_List_Var, workOrder_CreatedBy_Var, workOrder_Contacts_Var)
#    test_Enhanced_IFTAPage_apolloWebPortal.EnhancedIFTA_ManagePage (driver, driver_Name, driver_Version, carrier, truckDriversList)
#    test_Administration_Roles_ManagePage_apolloWebPortal.Administration_Roles_ManagePage(driver, driver_Name, driver_Version, carrier, truckDriversList)
#    test_Hierarchy_User_Access_ManagePage_apolloWebPortal.Hierarchy_User_Access_MenuPage (driver, driver_Name, driver_Version, carrier, truckDriversList)

    #driver.close()

    #def datebyDriver_Calc():
    #    dateEnd = datetime.now()
    #    datebyDriver = dateEnd - dateInitbyDriver
    #    return datebyDriver

    dateEnd = datetime.now()
    datebyDriver = dateEnd - dateInitbyDriver
    test_Execution_Time_By_Driver_Global = datebyDriver

    print()
    print(f"{driver_Name} - Test executing time TOTAL = {datebyDriver}")

    tc_reports.summaryPerformance_by_Driver(driver, driver_Name, datebyDriver)


    #       Print Preformance Summary
    #tc_reports.summaryPerformance_by_Driver(driver, driver_Name)


    driverModelTestControl = driverModelTestControl + 1
