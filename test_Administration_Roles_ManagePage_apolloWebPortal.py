#               Apollo Web Portal - ADMINISTRATION ROLES

def Administration_Roles_ManagePage (driver, driver_Name, driver_Version, carrier, truckDriversList):

    from selenium import webdriver
    import time
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.support.ui import Select
    import tc_reports
    from selenium.webdriver import ActionChains
    from selenium.webdriver.support.select import Select
    import os
    import glob
    import openpyxl
    from pathlib import Path
    from pathlib import Path
    from os import path
    from datetime import datetime, timedelta
    from selenium.common.exceptions import NoSuchElementException
    import test_Report_Categories_Defects_FIELDSInterchanges_apolloWebPortal
    import test_Global_Variables_apolloWebPortal

    #               DVIR Main

    #       Fields Address
    menuRegion_MainSideBar_ManagePageAdrAsideDiv = "/html/body/app-root/app-main/div/main-side-bar/aside/div"

    button_Administration_ManagePageId = '//a[contains(@href,"#")]'
    #button_Administration_ManagePageAdr = "/html/body/app-root/app-main/div/main-side-bar/aside/div/nav/ul/li[17]/a"
    button_Administration_Roles_ManagePageAdr = '//a[contains(@href,"/roles")]'

    title_DVIR_DVIRPageAdr = "/html/body/app-root/app-main/div/div[1]/app-dvir/section[1]/div/div/div[1]/h1"


    #   Global Variables

    workbookDB = test_Global_Variables_apolloWebPortal.workbookDB_Global
    worksheetDB = test_Global_Variables_apolloWebPortal.worksheetDB_Global

    #       Variables

    Ref_DVIR_DVIRPage = "Roles"

    w = WebDriverWait(driver, 30)

    #       #######################################     DVIR Main functions    ########################################################
    #   ###############################################################################################################################
#   Page Title on TCReport
    function_Name = "Administration Function"
    tc_reports.function_Init_Page(function_Name, driver_Name)


#       Function Administration side bar button click
    menuRegion_MainSideBar_ManagePageAsideDiv = w.until(EC.presence_of_element_located((By.XPATH, menuRegion_MainSideBar_ManagePageAdrAsideDiv)))
    button_Administration_ManagePage = WebDriverWait(menuRegion_MainSideBar_ManagePageAsideDiv,10).until(EC.element_to_be_clickable((By.XPATH, button_Administration_ManagePageAdr))).click()

    input('stop')
#       Title of the right page
    title_DVIR_DVIRPage = w.until(EC.presence_of_element_located((By.XPATH, title_DVIR_DVIRPageAdr))).text
    test_Name = "DVIR page open"
    condition1 = "DVIR"
    condition2 = title_DVIR_DVIRPage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "DVIR Page - DVIR page open:"
    print_Information_Var = title_DVIR_DVIRPage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    #       Screenshot
    #tc_reports.screenshot(driver, driver_Name, test_Name)
    #print(title_DVIR_DVIRPage)
