#               Apollo Web Portal - Manage - Notifications


def carrierNotifications_ChildMenu_ManagePage (driver, driver_Name, driver_Version):

    from selenium import webdriver
    import time
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.support.ui import Select
    from datetime import datetime
    import tc_reports
    import re
    import test_Global_Variables_apolloWebPortal
    import openpyxl
    from pathlib import Path

#       Notifications Page Address & Variables
#       Fields Address

    # Notifications page
    button_Notifications_Carrier_ManagePageAdr = "/html/body/app-root/app-main/div/div/app-manage/section/div/div[1]/div/carrier-list/div/div/div[2]/table/tbody/tr/td[3]/div/button[5]"
    title_Notifications_Carrier_ManagePageAdr = "/html/body/app-root/app-main/div/div/app-manage/section/div/div[2]/div/notification-list/div/div/div[1]/h3"
    button_PlussNew_Notifications_ManagePageAdr = "/html/body/app-root/app-main/div/div/app-manage/section/div/div[2]/div/notification-list/div/div/div[1]/div/button"
    #input_Search_Notifications_ManagePageAdr = "/html/body/app-root/app-main/div/div/app-manage/section[2]/div/div[2]/div/notification-list/div/div/div[2]/dx-data-grid/div/div[4]/div/div/div[3]/div/div/div/div/div[1]/input"
    input_Search_Notifications_ManagePageAdr = "/html/body/app-root/app-main/div/div/app-manage/section[2]/div/div[2]/div/notification-list/div/div/div[2]/dx-data-grid/div/div[4]/div/div/div[3]/div/div/div/div/div[1]/input"
    text_1stName_Notifications_ManagePageAdr = "/html/body/app-root/app-main/div/div/app-manage/section[2]/div/div[2]/div/notification-list/div/div/div[2]/dx-data-grid/div/div[6]/div/table/tbody/tr[1]/td[1]"
    text_1stType_Notifications_ManagePageAdr = "/html/body/app-root/app-main/div/div/app-manage/section[2]/div/div[2]/div/notification-list/div/div/div[2]/dx-data-grid/div/div[6]/div/table/tbody/tr[1]/td[2]/div"
    text_1stHomeBase_Notifications_ManagePageAdr = "/html/body/app-root/app-main/div/div/app-manage/section[2]/div/div[2]/div/notification-list/div/div/div[2]/dx-data-grid/div/div[6]/div/table/tbody/tr[1]/td[3]/div"
    title_Name_Notifications_ManagePageAdr = "/html/body/app-root/app-main/div/div/app-manage/section[2]/div/div[2]/div/notification-list/div/div/div[2]/dx-data-grid/div/div[5]/div/table/tbody/tr/td[1]"
    sort_Name_Notifications_ManagePageAdr = "/html/body/app-root/app-main/div/div/app-manage/section[2]/div/div[2]/div/notification-list/div/div/div[2]/dx-data-grid/div/div[5]/div/table/tbody/tr/td[1]/div[1]/span"
    button_Delete_Notifications_ManagePageAdr = "/html/body/app-root/app-main/div/div/app-manage/section[2]/div/div[2]/div/notification-list/div/div/div[2]/dx-data-grid/div/div[6]/div/table/tbody/tr[1]/td[4]/div/button[2]"
    button_DeleteOK_Notifications_ManagePageAdr = "/html/body/ngb-modal-window/div/div/app-confirmation-dialog/div[3]/button[1]"
    button_SearchClean_Notifications_ManagePageAdr = "/html/body/app-root/app-main/div/div/app-manage/section[2]/div/div[2]/div/notification-list/div/div/div[2]/dx-data-grid/div/div[4]/div/div/div[3]/div/div/div/div/div[2]/span/span"

    #Notification page
    title_Notification_Notifications_ManagePageAdr = "/html/body/ngb-modal-window/div/div/notification-modal/div[1]"
    dropDown_HomeBase_Notification_Notifications_ManagePageAdr = "/html/body/ngb-modal-window/div/div/notification-modal/div[2]/notification-form/form/div[1]/div[1]/select"
    input_Name_Notification_Notifications_ManagePageAdr = "/html/body/ngb-modal-window/div/div/notification-modal/div[2]/notification-form/form/div[1]/div[2]/input"
    drpBox_Type_Notification_Notifications_ManagePageId = "type"
    input_Emails_Notification_Notifications_ManagePageAdr = "/html/body/ngb-modal-window/div/div/notification-modal/div[2]/notification-form/form/div[1]/div[4]/input"
    input_SearchAssets_Notification_Notifications_ManagePageAdr = "/html/body/ngb-modal-window/div/div/notification-modal/div[2]/notification-form/form/div[1]/div[4]/app-items-table/div/div/dx-data-grid/div/div[4]/div/div/div[3]/div/div/div/div/div[1]/input"
    checkBox_Assets_Notification_Notifications_ManagePageAdr = "/html/body/ngb-modal-window/div/div/notification-modal/div[2]/notification-form/form/div[1]/div[4]/app-items-table/div/div/dx-data-grid/div/div[6]/div/table/tbody/tr[1]/td[1]/div/div"
    title_List_Notification_Notifications_ManagePageAdr = "/html/body/ngb-modal-window/div/div/notification-modal/div[2]/notification-form/form/div[1]/div[5]/div/div[1]"
    checkBox_1stAsset_Notification_Notifications_ManagePageAdr = "/html/body/ngb-modal-window/div/div/notification-modal/div[2]/notification-form/form/div[1]/div[5]/app-items-table/div/div/dx-data-grid/div/div[6]/div/table/tbody/tr[1]/td[1]/div/div"
    button_SAVE_Notification_Notifications_ManagePageAdr = "/html/body/ngb-modal-window/div/div/notification-modal/div[2]/notification-form/form/div[2]/button[1]"
    button_CLOSE_Notification_Notifications_ManagePageAdr = "/html/body/ngb-modal-window/div/div/notification-modal/div[2]/notification-form/form/div[2]/button[2]"

    #       Variables:
    date = datetime.now()
    w = WebDriverWait(driver, 30)

    random = str(date)
    random = random[len(random) - 6:]
    random = str(random)

    input_Name_Notification_Notifications_ManagePageVar = "Notification Automation Test" + random
    input_Emails_Notification_Notifications_ManagePageVar = "carlos.liguori@assuredtechmatics.com"
    input_SearchAssets_Notification_Notifications_ManagePageVar = "TRUCKATEST1000001"

    # Excel DB
    #workbookDB = test_Global_Variables_apolloWebPortal.workbookDB_Global
    #worksheetDB = test_Global_Variables_apolloWebPortal.worksheetDB_Global
    workbookMANAGEDB = test_Global_Variables_apolloWebPortal.workbookMANAGEDB_Global
    worksheetMANAGEDB = test_Global_Variables_apolloWebPortal.worksheetMANAGEDB_Global
    #excel_Type_cellValue = worksheetMANAGEDB_Read['G2'].value
    #excel_ListTitle_cellValue = worksheetMANAGEDB_Read['H2'].value
    #excel_DB_line = 4
    excel_DB_line_LogicTest = 2
    excel_colum_Type = "G"
    excel_colum_ListTitle = "H"

    #####################################################################################################################################
    #                                                       NOTIFICATIONS Main functions                                                       #
    #####################################################################################################################################

    button_Notifications_Carrier_ManagePage = w.until(EC.presence_of_element_located((By.XPATH,button_Notifications_Carrier_ManagePageAdr))).click()

  #   Page Title on TCReport
    function_Name = "Carriers NOTIFICATIONS Function"
    tc_reports.function_Init_Page(function_Name, driver_Name)

    title_Notifications_Carrier_ManagePage = w.until(EC.presence_of_element_located((By.XPATH, title_Notifications_Carrier_ManagePageAdr))).text
    # print(title_Assets_Assets_ManagePage)
    #       Assert Test and print if assert is fail
    test_Name = "Notifictions Page Open"
    condition1 = "Notifications"
    condition2 = title_Notifications_Carrier_ManagePage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Notifications Page Open"
    print_Information_Var = title_Notifications_Carrier_ManagePage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type,driver_Name, driver_Version)
    #       Screenshot
    test_Name = "Notifications Page"
    tc_reports.screenshot(driver, driver_Name, test_Name)

    #****************************************************
    # Create a New Notification - Notification Child page
    #****************************************************

    time.sleep(1)
    #   + New button
    w.until(EC.element_to_be_clickable((By.XPATH, button_PlussNew_Notifications_ManagePageAdr))).click()

    #   Notification Child Page:
    title_Notification_Notifications_ManagePage = w.until((EC.presence_of_element_located((By.XPATH, title_Notification_Notifications_ManagePageAdr)))).text
    # print(title_Assets_Assets_ManagePage)
    #       Assert Test and print if assert is fail
    test_Name = "Notifiction Page Open"
    condition1 = "Notification"
    condition2 = title_Notification_Notifications_ManagePage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Notification Page Open"
    print_Information_Var = title_Notification_Notifications_ManagePage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type,
                                driver_Name, driver_Version)
    #       Screenshot
    test_Name = "Notification Page"
    tc_reports.screenshot(driver, driver_Name, test_Name)

    # Create a New Notification


    # Home Base
    dropDown = Select(w.until(EC.presence_of_element_located((By.XPATH, dropDown_HomeBase_Notification_Notifications_ManagePageAdr))))
    dropDown_HomeBase_Notification_Notifications_ManagePage_List = [x.text for x in dropDown.options]
    n = 0
    while n < len(dropDown_HomeBase_Notification_Notifications_ManagePage_List):
        dropDown_HomeBase_Notification_Notifications_ManagePage_Selected = dropDown.select_by_visible_text(dropDown_HomeBase_Notification_Notifications_ManagePage_List[n])
        dropDown_HomeBase_Notification_Notifications_ManagePage_Read = dropDown.first_selected_option.text
        # Assert
        test_Name = "Home Base -> Select x Read"
        condition1 = dropDown_HomeBase_Notification_Notifications_ManagePage_List[n]
        condition2 = dropDown_HomeBase_Notification_Notifications_ManagePage_Read
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
        n = n + 1
    #       Print Assert OK
    print_Information_Fix = "Home Base -> Select x Read"
    print_Information_Var = ""
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    dropDown_HomeBase_Notification_Notifications_ManagePage_Selected = dropDown.select_by_visible_text(dropDown_HomeBase_Notification_Notifications_ManagePage_List[0])
    dropDown_HomeBase_Notification_Notifications_ManagePage_Read = dropDown.first_selected_option.text

    # Name
    input_Name_Notification_Notifications_ManagePage = w.until((EC.presence_of_element_located((By.XPATH,input_Name_Notification_Notifications_ManagePageAdr))))
    input_Name_Notification_Notifications_ManagePage.send_keys(input_Name_Notification_Notifications_ManagePageVar)

    # Type & List Title verification
    #   Read excel

    # Read excel value not formula
    excell_pointer = Path(workbookMANAGEDB)
    workbookDB_Read = openpyxl.load_workbook(excell_pointer, data_only=True)
    worksheetDB_Read = workbookDB_Read.active

    dropDown = Select(w.until(EC.presence_of_element_located((By.ID,drpBox_Type_Notification_Notifications_ManagePageId))))
    drpBox_Type_Notification_Notifications_ManagePage_List = [x.text for x in dropDown.options]
    n = 0
    x = n + 3
    print("****************************************************************")
    while n < len(drpBox_Type_Notification_Notifications_ManagePage_List):
        dropBox_Type_Notification_Notifications_ManagePage_Selected = dropDown.select_by_visible_text(drpBox_Type_Notification_Notifications_ManagePage_List[n])
        dropBox_Type_Notification_Notifications_ManagePage_Read = dropDown.first_selected_option.text
        if dropBox_Type_Notification_Notifications_ManagePage_Read != "-- Select notification type --":
            title_List_Notification_Notifications_ManagePage = w.until(EC.presence_of_element_located((By.XPATH, title_List_Notification_Notifications_ManagePageAdr))).text
            #excel_colum_TypeVar = (str(excel_colum_Type) + str(x))
            #typeVar = worksheetDB_Read[excel_colum_TypeVar].value
            excel_colum_ListTitleVar = (str(excel_colum_ListTitle) + str(x))
            excel_listTitleVar = worksheetDB_Read[excel_colum_ListTitleVar].value
            # Assert
            test_Name = "Notification Type x List Title"
            condition1 = title_List_Notification_Notifications_ManagePage
            condition2 = excel_listTitleVar
            tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
            x = x + 1
        else:
            print("List Error")
        n = n + 1
    #       Print Assert OK
    print_Information_Fix = "Notification Type selected x List* Title"
    print_Information_Var = title_List_Notification_Notifications_ManagePage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    #Emails
    input_Emails_Notification_Notifications_ManagePage = w.until(EC.presence_of_element_located((By.XPATH,input_Emails_Notification_Notifications_ManagePageAdr)))
    input_Emails_Notification_Notifications_ManagePage.send_keys(input_Emails_Notification_Notifications_ManagePageVar)

    # Select 1st Asset on the list
    checkBox_1stAsset_Notification_Notifications_ManagePage = w.until(EC.element_to_be_clickable((By.XPATH, checkBox_1stAsset_Notification_Notifications_ManagePageAdr))).click()
    #SAVE
    w.until(EC.element_to_be_clickable((By.XPATH,button_SAVE_Notification_Notifications_ManagePageAdr))).click()

    #*************************************************************************************************************************************************
    # Back to Notifications page
    # Verifying if the notification created is correctly saved
    input_Search_Notifications_ManagePage = w.until(EC.presence_of_element_located((By.XPATH, input_Search_Notifications_ManagePageAdr)))
    input_Search_Notifications_ManagePage.send_keys(input_Name_Notification_Notifications_ManagePageVar)

    #Verifying Notifications created parameters
    time.sleep(1)

    #NAME
    text_1stName_Notifications_ManagePage = w.until(EC.presence_of_element_located((By.XPATH, text_1stName_Notifications_ManagePageAdr))).text
    #       Assert Test and print if assert is fail
    test_Name = "NAME Notifiction Created Verification"
    condition1 = input_Name_Notification_Notifications_ManagePageVar
    condition2 = text_1stName_Notifications_ManagePage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "NAME Notifiction Created Verification"
    print_Information_Var = text_1stName_Notifications_ManagePage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    #TYPE
    text_1stType_Notifications_ManagePage = w.until(EC.presence_of_element_located((By.XPATH, text_1stType_Notifications_ManagePageAdr))).text
    #       Assert Test and print if assert is fail
    test_Name = "TYPE Notifiction Created Verification"
    condition1 = dropBox_Type_Notification_Notifications_ManagePage_Read
    condition2 = text_1stType_Notifications_ManagePage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "TYPE Notifiction Created Verification"
    print_Information_Var = text_1stType_Notifications_ManagePage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)


    # Home Base
    text_1stHomeBase_Notifications_ManagePage = w.until(EC.presence_of_element_located((By.XPATH, text_1stHomeBase_Notifications_ManagePageAdr))).text
    #       Assert Test and print if assert is fail
    test_Name = "HOME BASE Notifiction Created Verification"
    condition1 = dropDown_HomeBase_Notification_Notifications_ManagePage_Read
    condition2 = text_1stHomeBase_Notifications_ManagePage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "HOME BASE Notifiction Created Verification"
    print_Information_Var = text_1stHomeBase_Notifications_ManagePage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    #       Screenshot
    test_Name = "Notification Created Verification"
    tc_reports.screenshot(driver, driver_Name, test_Name)

    # DELETE Notification
    w.until(EC.element_to_be_clickable((By.XPATH, button_Delete_Notifications_ManagePageAdr))).click()
    #       Screenshot
    test_Name = "Delete Notification"
    tc_reports.screenshot(driver, driver_Name, test_Name)
    w.until((EC.element_to_be_clickable(((By.XPATH, button_DeleteOK_Notifications_ManagePageAdr))))).click()

    w.until(EC.element_to_be_clickable((By.XPATH, button_SearchClean_Notifications_ManagePageAdr))).click()

    return()
