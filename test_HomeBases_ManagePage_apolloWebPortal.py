#               Apollo Web Portal - Manage - Home Bases


def carrierHomeBases_ChildMenu_ManagePage (driver, driver_Name, driver_Version):

    from selenium import webdriver
    import time
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.support.ui import Select
    from datetime import datetime
    import tc_reports
    import test_Global_Variables_apolloWebPortal
    import re
    from selenium.webdriver import ActionChains
    import test_Global_Variables_apolloWebPortal


#       Carrier details Page Address & Variables
#       Fields Address
    button_Carrier_HomeBases_ManagePageAdr = "/html/body/app-root/app-main/div/div/app-manage/section[2]/div/div[1]/div/carrier-list/div/div/div[2]/table/tbody/tr/td[3]/div/button[3]"
    title_HomeBases_HomeBases_ManagePageAdr = "/html/body/app-root/app-main/div/div[1]/app-manage/section[2]/div/div[2]/div/app-homebase-list/div/div/div[1]/h3"
    button_PlussNew_HomeBases_ManagePageAdr = "/html/body/app-root/app-main/div/div[1]/app-manage/section[2]/div/div[2]/div/app-homebase-list/div/div/div[1]/div/button"
    title_HomeBases_HomeBases_ManagePageAdr = "/html/body/app-root/app-main/div/div[1]/app-manage/section[2]/div/div[2]/div/app-homebase-list/div/div/div[1]/h3"
    title_HomeBase_HomeBase_ChildPageAdr = "/html/body/ngb-modal-window/div/div/homebase-modal-form/div[1]/h4"
    input_LocationName_HomeBase_ChildPageAdr = "/html/body/ngb-modal-window/div/div/homebase-modal-form/div[2]/form/div[1]/div[1]/input"
    input_Address_HomeBase_ChildPageAdr = "/html/body/ngb-modal-window/div/div/homebase-modal-form/div[2]/form/div[1]/div[2]/input"
    input_Latitude_HomeBase_ChildPageAdr = "/html/body/ngb-modal-window/div/div/homebase-modal-form/div[2]/form/div[1]/div[3]/input"
    input_Longitude_HomeBase_ChildPageAdr = "/html/body/ngb-modal-window/div/div/homebase-modal-form/div[2]/form/div[1]/div[4]/input"
    dropDown_TimeZone_HomeBase_ChildPageAdr = "/html/body/ngb-modal-window/div/div/homebase-modal-form/div[2]/form/div[1]/div[5]/select"
    checkBox_SetMainOffice_HomeBase_ChildPageAdr = "/html/body/ngb-modal-window/div/div/homebase-modal-form/div[2]/form/div[1]/div[6]/div/input"
    button_SAVE_HomeBase_ChildPageAdr = "/html/body/ngb-modal-window/div/div/homebase-modal-form/div[2]/form/div[2]/button[1]"
    button_CLOSE_HomeBase_ChildPageAdr = "/html/body/ngb-modal-window/div/div/homebase-modal-form/div[2]/form/div[2]/button[2]"
    button_X_HomeBase_ChildPageAdr = "/html/body/ngb-modal-window/div/div/homebase-modal-form/div[1]/button/span"
    input_Search_HomeBasesAdr = "/html/body/app-root/app-main/div/div/app-manage/section[2]/div/div[2]/div/app-homebase-list/div/div/div[2]/dx-data-grid/div/div[4]/div/div/div[3]/div/div/div/div/div[1]/input"

    indicator_Sort_Name_HomeBasesPageAdr = "/html/body/app-root/app-main/div/div[1]/app-manage/section[2]/div/div[2]/div/app-homebase-list/div/div/div[2]/dx-data-grid/div/div[5]/div[1]/table/tbody/tr/td[1]"

    text_FirstName_HomeBasesPageAdr = "/html/body/app-root/app-main/div/div[1]/app-manage/section[2]/div/div[2]/div/app-homebase-list/div/div/div[2]/dx-data-grid/div/div[6]/div[2]/table/tbody/tr[1]/td[1]"
    button_Details_Action_HomeBasePageAdr = "/html/body/app-root/app-main/div/div[1]/app-manage/section[2]/div/div[2]/div/app-homebase-list/div/div/div[2]/dx-data-grid/div/div[6]/div[1]/div/div[1]/div/table/tbody/tr[1]/td[4]/div/button[1]"
    button_Delete_Action_HomeBasePageAdr = "/html/body/app-root/app-main/div/div/app-manage/section[2]/div/div[2]/div/app-homebase-list/div/div/div[2]/dx-data-grid/div/div[6]/div[1]/div/div[1]/div/table/tbody/tr[1]/td[4]/div/button[3]"
    button_DriverAssignment_Action_HomeBasePageAdr = "/html/body/app-root/app-main/div/div/app-manage/section[2]/div/div[2]/div/app-homebase-list/div/div/div[2]/dx-data-grid/div/div[6]/div[1]/div/div[1]/div/table/tbody/tr[1]/td[4]/div/button[2]"
    checkBox_Assignment_DriverAssignmentChild_HomeBasesPageAdr = "/html/body/ngb-modal-window/div/div/app-drivers-assigned/div[2]/form/div[1]/div[2]/dx-data-grid/div/div[6]/div/table/tbody/tr[1]/td[3]/div/dx-check-box/div/span"
    button_SAVE_DriverAssignmentChild_HomeBasesPageAdr = "/html/body/ngb-modal-window/div/div/app-drivers-assigned/div[2]/form/div[2]/button[1]"
    button_CLOSE_DriverAssignmentChild_HomeBasesPageAdr = "/html/body/ngb-modal-window/div/div/app-drivers-assigned/div[2]/form/div[2]/button[2]"
    button_PageNumber_DriverAssignmentChild_HomeBasesPageAdr = "/html/body/ngb-modal-window/div/div/app-drivers-assigned/div[2]/form/div[1]/div[2]/dx-data-grid/div/div[10]/div/div[1]"
    button_DELETE_DeleteHomeBase_Popup_Adr = "/html/body/ngb-modal-window/div/div/app-confirmation-dialog/div[3]/button[1]"

    #       Variables:
    date = datetime.now()
    w = WebDriverWait(driver, 30)

    random = str(date)
    random = random[len(random) - 6:]
    random = str(random)
    """
    input_LocationName_HomeBase_ChildPageVar = "AAA Miami Dolphins Stadium "
    input_Address_HomeBase_ChildPageVar = "347 Don Shula Dr, Miami Gardens, FL 33056"
    input_Latitude_HomeBase_ChildPageVar = "25.95856"
    input_Longitude_HomeBase_ChildPageVar = "-80.23965"
    """

    input_LocationName_HomeBase_ChildPageVar = test_Global_Variables_apolloWebPortal.input_LocationName_HomeBase_ChildPage_Global
    input_Address_HomeBase_ChildPageVar = test_Global_Variables_apolloWebPortal.input_Address_HomeBase_ChildPage_Global
    input_Latitude_HomeBase_ChildPageVar = test_Global_Variables_apolloWebPortal.input_Latitude_HomeBase_ChildPage_Global
    input_Longitude_HomeBase_ChildPageVar = test_Global_Variables_apolloWebPortal.input_Longitude_HomeBase_ChildPage_Global

    date1 = str(date)
    date1 = date1[len(date1)-6:]
    input_LocationName_HomeBase_ChildPageVar = input_LocationName_HomeBase_ChildPageVar + str(date1)
    print(input_LocationName_HomeBase_ChildPageVar)

    #####################################################################################################################################
    #                                                   Home Bases Main functions                                                       #
    #####################################################################################################################################

    #####################################################################################################################################
    #                                                   Home Bases ACTIONS DETAILS Main functions                                       #
    #####################################################################################################################################

    #   Page Title on TCReport
    function_Name = "Carriers Home Bases Function"
    tc_reports.function_Init_Page(function_Name, driver_Name)

    # Home Page button
    button_Carrier_HomeBases_ManagePage = w.until(EC.element_to_be_clickable((By.XPATH, button_Carrier_HomeBases_ManagePageAdr)))
    time.sleep(0.5)
    button_Carrier_HomeBases_ManagePage.click()

    #   Home Bases Page Open test:
    title_HomeBases_HomeBases_ManagePage = w.until((EC.presence_of_element_located((By.XPATH, title_HomeBases_HomeBases_ManagePageAdr)))).text
    print(title_HomeBases_HomeBases_ManagePage)
    #       Assert Test and print if assert is fail
    test_Name = "Home Bases Page Open"
    condition1 = "Home Bases"
    condition2 = title_HomeBases_HomeBases_ManagePage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Home Bases Page Open"
    print_Information_Var = title_HomeBases_HomeBases_ManagePage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    #       Screenshot
    test_Name = "Home Bases Page"
    tc_reports.screenshot(driver, driver_Name, test_Name)

    #   + New button
    w.until(EC.element_to_be_clickable((By.XPATH, button_PlussNew_HomeBases_ManagePageAdr))).click()

    #   Home Bases ChildPage Open test:
    title_HomeBase_HomeBase_ChildPage = w.until((EC.presence_of_element_located((By.XPATH, title_HomeBase_HomeBase_ChildPageAdr)))).text
    #       Assert Test and print if assert is fail
    test_Name = "Home Bases Child Page Open"
    condition1 = "Home Base"
    condition2 = title_HomeBase_HomeBase_ChildPage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Home Base Child Page Open"
    print_Information_Var = title_HomeBase_HomeBase_ChildPage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    #       Screenshot
    test_Name = "Home Base New Child Page"
    tc_reports.screenshot(driver, driver_Name, test_Name)

    #   Location Name Home Base Child Page test:
    input_LocationName_HomeBase_ChildPage = w.until((EC.presence_of_element_located((By.XPATH, input_LocationName_HomeBase_ChildPageAdr))))
    input_LocationName_HomeBase_ChildPage.send_keys(input_LocationName_HomeBase_ChildPageVar)
    read_LocationName_HomeBase_ChildPage = input_LocationName_HomeBase_ChildPage.get_property('value')
    #       Assert Test and print if assert is fail
    test_Name = "Location Name Home Base Child Page Open"
    condition1 = input_LocationName_HomeBase_ChildPageVar
    condition2 = read_LocationName_HomeBase_ChildPage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Location Name Home Base Child Page"
    print_Information_Var = read_LocationName_HomeBase_ChildPage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)


    #   Address Home Base Child Page test:
    input_Address_HomeBase_ChildPage = w.until((EC.presence_of_element_located((By.XPATH, input_Address_HomeBase_ChildPageAdr))))
    input_Address_HomeBase_ChildPage.send_keys(input_Address_HomeBase_ChildPageVar)
    read_Address_HomeBase_ChildPage = input_Address_HomeBase_ChildPage.get_property('value')
    #       Assert Test and print if assert is fail
    test_Name = "Address Home Base Child Page Open"
    condition1 = input_Address_HomeBase_ChildPageVar
    condition2 = read_Address_HomeBase_ChildPage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Address Home Base Child Page"
    print_Information_Var = read_Address_HomeBase_ChildPage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)


    #   Latitude Home Base Child Page test:
    input_Latitude_HomeBase_ChildPage = w.until((EC.presence_of_element_located((By.XPATH, input_Latitude_HomeBase_ChildPageAdr))))
    #input_Latitude_HomeBase_ChildPage.send_keys(input_Latitude_HomeBase_ChildPageVar)
    read_Latitude_HomeBase_ChildPage = input_Latitude_HomeBase_ChildPage.get_property('value')
    #       Assert Test and print if assert is fail
    test_Name = "Latitude Home Base Child Page Open"
    condition1 = input_Latitude_HomeBase_ChildPageVar
    condition2 = read_Latitude_HomeBase_ChildPage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Latitude Home Base Child Page"
    print_Information_Var = read_Latitude_HomeBase_ChildPage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    #   Longitude Home Base Child Page test:
    input_Longitude_HomeBase_ChildPage = w.until((EC.presence_of_element_located((By.XPATH, input_Longitude_HomeBase_ChildPageAdr))))
    #input_Longitude_HomeBase_ChildPage.send_keys(input_Longitude_HomeBase_ChildPageVar)
    read_Longitude_HomeBase_ChildPage = input_Longitude_HomeBase_ChildPage.get_property('value')
    #       Assert Test and print if assert is fail
    test_Name = "Longitude Home Base Child Page Open"
    condition1 = input_Longitude_HomeBase_ChildPageVar
    condition2 = read_Longitude_HomeBase_ChildPage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Longitude"
    print_Information_Var = read_Longitude_HomeBase_ChildPage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    #       Time Zone Home Base Child Page test:
    dropDown = Select(w.until(EC.presence_of_element_located((By.XPATH, dropDown_TimeZone_HomeBase_ChildPageAdr))))
    dropDown_Import_TimeZone_HomeBase_ChildPage_List = [x.text for x in dropDown.options]
    n = 0
    while n < len(dropDown_Import_TimeZone_HomeBase_ChildPage_List):
        dropDown_TimeZone_HomeBase_ChildPage = dropDown.select_by_visible_text(dropDown_Import_TimeZone_HomeBase_ChildPage_List[n])
        # read the selected option on the dropdown
        dropDown_TimeZone_HomeBase_ChildPageRead = dropDown.first_selected_option.text
        # **************** Test and report results at TCReport  ****************************************************************************
        #       Assert Test and print if assert is fail
        test_Name = "Time Zone Home Base Child Page Open"
        last_Options_dropDown_TimeZone_HomeBase_ChildPageVar = dropDown_Import_TimeZone_HomeBase_ChildPage_List[n]
        condition1 = last_Options_dropDown_TimeZone_HomeBase_ChildPageVar
        condition2 = dropDown_TimeZone_HomeBase_ChildPageRead
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
        #       Print Assert OK
        print_Information_Fix = "Time Zone Home Base Child Page"
        print_Information_Var = dropDown_TimeZone_HomeBase_ChildPageRead
        test_Case_Type = ""
        contol_Reportfile = 1
        tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
        n = n + 1

#   Select a random time zone for each test
    n = date.strftime("%S")
    n = int(n[1])
    if n > 7:
        n = n - 3
    dropDown_Random_TimeZone_HomeBase_ChildPage = dropDown.select_by_visible_text(dropDown_Import_TimeZone_HomeBase_ChildPage_List[n])


    w.until((EC.element_to_be_clickable((By.XPATH, button_SAVE_HomeBase_ChildPageAdr)))).click()

    # Verify New Home base
    input_Search_HomeBasesVar = w.until((EC.presence_of_element_located(((By.XPATH, input_Search_HomeBasesAdr)))))
    input_Search_HomeBasesVar.send_keys(input_LocationName_HomeBase_ChildPageVar)
    time.sleep(1)
    text_FirstName_HomeBasesPageVar = w.until((EC.presence_of_element_located(((By.XPATH, text_FirstName_HomeBasesPageAdr))))).text
    print(text_FirstName_HomeBasesPageVar)
#       Assert Test and print if assert is fail
    test_Name = "Home Bases SAVED check"
    condition1 = input_LocationName_HomeBase_ChildPageVar
    condition2 = text_FirstName_HomeBasesPageVar
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Home Bases Saved check OK"
    print_Information_Var = text_FirstName_HomeBasesPageVar
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    #       Screenshot
    test_Name = "Home Bases SAVED"
    tc_reports.screenshot(driver, driver_Name, test_Name)

