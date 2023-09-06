#               Apollo Web Portal - HIERARCHY USERS

def Hierarchy_User_Access_MenuPage (driver, driver_Name, driver_Version, carrier, truckDriversList):
    from selenium.webdriver import ActionChains
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.wait import WebDriverWait
    import tc_reports
    import time

    #       Carrier details Page Address & Variables
    #       Fields Address

    title_ManagePageAdr = "/html/body/app-root/app-main/div/div/breadcrumb/section/div/div/div/h1"
    title_UserType_ManagePageAdr = "/html/body/app-root/app-main/div/main-header/nav/div[2]/div[2]/span"

    #Common Buttons - All Users type (14):
    button_Manage_ManagePageAdr = '//a[contains(@href,"/manage")]'
    button_LogBooks_ManagePageAdr = '//a[contains(@href,"/logbooks")]'
    button_UnidentifiedLogs_ManagePageAdr = '//a[contains(@href,"/unidentifiedlogs")]'
    button_LogEdits_ManagePageAdr = '//a[contains(@href,"/logedits")]'
    button_Dashboards_ManagePageId = "dashboard"
    button_Violations_ManagePageAdr = '//a[contains(@href,"/violations")]'
    button_DVIR_ManagePageAdr = '//a[contains(@href,"/dvir")]'
    button_WorkOrder_ManagePageAdr = '//a[contains(@href,"/workorder")]'
    button_EnhancedIFTA_ManagePageAdr = '//a[contains(@href,"/enhancedifta")]'
    button_DriverRecords_ManagePageAdr = '//a[contains(@href,"/driverrecords")]'
    button_FMCSARecords_ManagePageAdr = '//a[contains(@href,"/fmcsarecords")]'
    button_Shipments_ManagePageAdr = '//a[contains(@href,"/shipments")]'
    button_EngineDiagnostic_ManagePageAdr = '//a[contains(@href,"/enginediagnostic")]'
    button_DriverDutyReport_ManagePageAdr = '//a[contains(@href,"/dutyreport")]'

    #Special Buttons for Reseller and Full Acces Client (1+2):
    button_Administration_ManagePageId = "administration"
    button_Administration_Roles_ManagePageAdr = "/html/body/app-root/app-main/div/main-side-bar/aside/div/div[4]/div/div/nav/ul/li[15]/ul/li[1]"
    button_Administration_Users_ManagePageAdr = "/html/body/app-root/app-main/div/main-side-bar/aside/div/div[4]/div/div/nav/ul/li[15]/ul/li[2]"

    #Special Buttons for Master Reseller (2)
    button_Billing_ManagePageAdr = '//a[contains(@href,"/billing")]'
    button_BillingReport_ManagePageAdr = '//a[contains(@href,"/billingreport")]'

    title_apollo_Portal_VersionAdr = "/html/body/app-root/app-main/div/main-header/nav/div[2]/div[1]/small"

    #       Variables
    w = WebDriverWait(driver, 10)
    control_Reportfile = 0
    print_Information_Fix = ""
    print_Information_Var = ""

    #       Main

    #       #######################################     DVIR Main functions    ########################################################
    #   ###############################################################################################################################
    #   Page Title on TCReport
    function_Name = "Main Menu options based on Hierarchy User Function"
    tc_reports.function_Init_Page(function_Name, driver_Name)

    title_ManagePage = w.until(EC.presence_of_element_located((By.XPATH, title_ManagePageAdr))).text

    # **************** Test and report results at TCReport  ******************************************************************************************************************
    #       Assert Test and print if assert is fail
    test_Name = "Manage Page Open"
    condition1 = "Manage"
    condition2 = title_ManagePage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Manage page - Manage page open:"
    print_Information_Var = title_ManagePage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    #       Screenshot
    tc_reports.screenshot(driver, driver_Name, test_Name)
    # **************** Test and report results at TCReports END  **************************************************************************************************************

    # Verify User Type
    title_UserType_ManagePage = w.until(EC.presence_of_element_located((By.XPATH, title_UserType_ManagePageAdr))).text
    #       Print User Type
    print_Information_Fix = "User Type:"
    print_Information_Var = title_UserType_ManagePage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    #******************************************
    #Common Buttons - All Users type (14) Test:
    #******************************************
    button_Manage_ManagePage = w.until(EC.presence_of_element_located((By.XPATH, button_Manage_ManagePageAdr))).text
    #       Assert Test and print if assert is fail
    test_Name = "All Users - Option: MANAGE"
    condition1 = "Manage"
    condition2 = button_Manage_ManagePage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "All Users - Option: MANAGE"
    print_Information_Var = button_Manage_ManagePage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    button_LogBooks_ManagePage = w.until(EC.presence_of_element_located((By.XPATH, button_LogBooks_ManagePageAdr))).text
    #       Assert Test and print if assert is fail
    test_Name = "All Users - Option: LOG BOOKS"
    condition1 = "Log Books"
    condition2 = button_LogBooks_ManagePage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "All Users - Option: LOG BOOKS"
    print_Information_Var = button_LogBooks_ManagePage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    button_UnidentifiedLogs_ManagePage = w.until(EC.presence_of_element_located((By.XPATH, button_UnidentifiedLogs_ManagePageAdr))).text
    #       Assert Test and print if assert is fail
    test_Name = "All Users - Option: UNIDENTIFIED LOGS"
    condition1 = "Unidentified Logs"
    condition2 = button_UnidentifiedLogs_ManagePage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "All Users - Option: UNIDENTIFIED LOGS"
    print_Information_Var = button_UnidentifiedLogs_ManagePage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    button_LogEdits_ManagePage = w.until(EC.presence_of_element_located((By.XPATH, button_LogEdits_ManagePageAdr))).text
    #       Assert Test and print if assert is fail
    test_Name = "All Users - Option: LOG EDITS"
    condition1 = "Log Edits"
    condition2 = button_LogEdits_ManagePage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "All Users - Option: LOG EDITS"
    print_Information_Var = button_LogEdits_ManagePage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    button_Dashboards_ManagePage = w.until(EC.presence_of_element_located((By.ID, button_Dashboards_ManagePageId))).text
    #       Assert Test and print if assert is fail
    test_Name = "All Users - Option: DASHBOARD"
    condition1 = "Dashboard"
    condition2 = button_Dashboards_ManagePage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "All Users - Option: DASHBOARD"
    print_Information_Var = button_Dashboards_ManagePage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    button_Violations_ManagePage = w.until(EC.presence_of_element_located((By.XPATH, button_Violations_ManagePageAdr))).text
    #       Assert Test and print if assert is fail
    test_Name = "All Users - Option: VIOLATIONS"
    condition1 = "Violations"
    condition2 = button_Violations_ManagePage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "All Users - Option: VIOLATIONS"
    print_Information_Var = button_Violations_ManagePage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    button_DVIR_ManagePage = w.until(EC.presence_of_element_located((By.XPATH, button_DVIR_ManagePageAdr))).text
    #       Assert Test and print if assert is fail
    test_Name = "All Users - Option: DVIR"
    condition1 = "DVIR"
    condition2 = button_DVIR_ManagePage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "All Users - Option: DVIR"
    print_Information_Var = button_DVIR_ManagePage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    button_WorkOrder_ManagePage = w.until(EC.presence_of_element_located((By.XPATH, button_WorkOrder_ManagePageAdr))).text
    #       Assert Test and print if assert is fail
    test_Name = "All Users - Option: WORK ORDER"
    condition1 = "Work Order"
    condition2 = button_WorkOrder_ManagePage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "All Users - Option: WORK ORDER"
    print_Information_Var = button_WorkOrder_ManagePage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    button_EnhancedIFTA_ManagePage = w.until(EC.presence_of_element_located((By.XPATH, button_EnhancedIFTA_ManagePageAdr))).text
    #       Assert Test and print if assert is fail
    test_Name = "All Users - Option: IFTA"
    condition1 = "IFTA"
    condition2 = button_EnhancedIFTA_ManagePage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "All Users - Option: IFTA"
    print_Information_Var = button_EnhancedIFTA_ManagePage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    button_DriverRecords_ManagePage = w.until(EC.presence_of_element_located((By.XPATH, button_DriverRecords_ManagePageAdr))).text
    #       Assert Test and print if assert is fail
    test_Name = "All Users - Option: DRIVER RECORDS"
    condition1 = "Driver Records"
    condition2 = button_DriverRecords_ManagePage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "All Users - Option: DRIVER RECORDS"
    print_Information_Var = button_DriverRecords_ManagePage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    button_FMCSARecords_ManagePage = w.until(EC.presence_of_element_located((By.XPATH, button_FMCSARecords_ManagePageAdr))).text
    #       Assert Test and print if assert is fail
    test_Name = "All Users - Option: FMCSA Records"
    condition1 = "FMCSA Records"
    condition2 = button_FMCSARecords_ManagePage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "All Users - Option: FMCSA RECORDS"
    print_Information_Var = button_FMCSARecords_ManagePage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)


    button_Shipments_ManagePage = w.until(EC.presence_of_element_located((By.XPATH, button_Shipments_ManagePageAdr))).text
    #       Assert Test and print if assert is fail
    test_Name = "All Users - Option: SHIPMENTS"
    condition1 = "Shipments"
    condition2 = button_Shipments_ManagePage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "All Users - Option: SHIPMENTS"
    print_Information_Var = button_Shipments_ManagePage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    button_EngineDiagnostic_ManagePage = w.until(EC.presence_of_element_located((By.XPATH, button_EngineDiagnostic_ManagePageAdr))).text
    #       Assert Test and print if assert is fail
    test_Name = "All Users - Option: ENGINE DIAGNOSTIC"
    condition1 = "Engine Diagnostic"
    condition2 = button_EngineDiagnostic_ManagePage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "All Users - Option: ENGINE DIAGNOSTIC"
    print_Information_Var = button_EngineDiagnostic_ManagePage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    button_DriverDutyReport_ManagePage = w.until(EC.presence_of_element_located((By.XPATH, button_DriverDutyReport_ManagePageAdr))).text
    #       Assert Test and print if assert is fail
    test_Name = "All Users - Option: DRIVER DUTY REPORT"
    condition1 = "Driver Duty Report"
    condition2 = button_DriverDutyReport_ManagePage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "All Users - Option: DRIVER DUTY REPORT"
    print_Information_Var = button_DriverDutyReport_ManagePage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    # ******************************************
    # Administration Buttons - Resellers and Full Access Client Users type (3) Test:
    # ******************************************

    try:
        button_Administration_ManagePage = w.until(EC.presence_of_element_located((By.ID, button_Administration_ManagePageId))).text
        if title_UserType_ManagePage == "LimitedClient":
            #       Assert Test and print if assert is fail
            test_Name = "ADMINISTRATION Option MUST NOT allowed to user: "
            condition1 = ""
            condition2 = title_UserType_ManagePage
            tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
            #       Print Assert OK
            print_Information_Fix = "ADMINISTRATION Option MUST NOT allowed to user: "
            print_Information_Var = title_UserType_ManagePage
            test_Case_Type = ""
            contol_Reportfile = 1
            tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
        else:
            #       Assert Test and print if assert is fail
            test_Name = "ADMINISTRATION Option is allowed to user: "
            condition1 = title_UserType_ManagePage
            condition2 = title_UserType_ManagePage
            tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
            #       Print Assert OK
            print_Information_Fix = "ADMINISTRATION Option is allowed to user: "
            print_Information_Var = title_UserType_ManagePage
            test_Case_Type = ""
            contol_Reportfile = 1
            tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    except:
        test_Name = "ADMINISTRATION Option MUST NOT allowed to user: "
        condition1 = title_UserType_ManagePage
        condition2 = title_UserType_ManagePage
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
        #       Print Assert OK
        print_Information_Fix = "ADMINISTRATION Option MUST NOT allowed to user: "
        print_Information_Var = title_UserType_ManagePage
        test_Case_Type = ""
        contol_Reportfile = 1
        tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)




    #***************************************************
    # Exclusive Buttons - Master Reseller type (2) Test:
    #***************************************************+
    try:
        button_Billing_ManagePage = w.until(EC.presence_of_element_located((By.XPATH, button_Billing_ManagePageAdr))).text
        if title_UserType_ManagePage == "MasterReseller":
            #       Assert Test and print if assert is fail
            test_Name = "Master Reseller Main Menu - Option: BILLING"
            condition1 = "Billing"
            condition2 = button_Billing_ManagePage
            tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
            #       Print Assert OK
            print_Information_Fix = "Master Reseller Main Menu - Option: BILLING"
            print_Information_Var = button_Billing_ManagePage
            test_Case_Type = ""
            contol_Reportfile = 1
            tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
        else:
            #       Assert Test and print if assert is fail
            test_Name = "BILLING Option is allowed to user: "
            condition1 = "MasterReseller"
            condition2 = title_UserType_ManagePage
            tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
            #       Print Assert OK
            print_Information_Fix = "BILLING Option is allowed to user: "
            print_Information_Var = title_UserType_ManagePage
            test_Case_Type = ""
            contol_Reportfile = 1
            tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    except:
        #       Assert Test and print if assert is fail
        if "MasterReseller" == str(title_UserType_ManagePage):
            #       Assert Test and print if assert is fail
            test_Name = "BILLING Option MUST BE allowed to user: "
            condition1 = ""
            condition2 = title_UserType_ManagePage
            tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
        else:
            #       Assert Test and print if assert is fail
            test_Name = "BILLING Option is NOT allowed to user: "
            condition1 = title_UserType_ManagePage
            condition2 = title_UserType_ManagePage
            tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
            #       Print Assert OK
            print_Information_Fix = "BILLING Option is NOT allowed to user: "
            print_Information_Var = title_UserType_ManagePage
            test_Case_Type = ""
            contol_Reportfile = 1
            tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    try:
        button_BillingReport_ManagePage = w.until(EC.presence_of_element_located((By.XPATH, button_BillingReport_ManagePageAdr))).text
        if title_UserType_ManagePage == "MasterReseller":
            #       Assert Test and print if assert is fail
            test_Name = "Master Reseller Main Menu - Option: BILLING REPORT"
            condition1 = "Billing Report"
            condition2 = button_BillingReport_ManagePage
            tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
            #       Print Assert OK
            print_Information_Fix = "Master Reseller Main Menu - Option: BILLING REPORT"
            print_Information_Var = button_BillingReport_ManagePage
            test_Case_Type = ""
            contol_Reportfile = 1
            tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
        else:
            #       Assert Test and print if assert is fail
            test_Name = "BILLING REPORTOption is allowed to user: "
            condition1 = "MasterReseller"
            condition2 = title_UserType_ManagePage
            tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
            #       Print Assert OK
            print_Information_Fix = "BILLING REPORT Option is allowed to user: "
            print_Information_Var = title_UserType_ManagePage
            test_Case_Type = ""
            contol_Reportfile = 1
            tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    except:
        #       Assert Test and print if assert is fail
        if "MasterReseller" == str(title_UserType_ManagePage):
            #       Assert Test and print if assert is fail
            test_Name = "BILLING REPORT Option MUST BE allowed to user: "
            condition1 = ""
            condition2 = title_UserType_ManagePage
            tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
        else:
            #       Assert Test and print if assert is fail
            test_Name = "BILLING REPORT Option is NOT allowed to user: "
            condition1 = title_UserType_ManagePage
            condition2 = title_UserType_ManagePage
            tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
            #       Print Assert OK
            print_Information_Fix = "BILLING REPORT Option is NOT allowed to user: "
            print_Information_Var = title_UserType_ManagePage
            test_Case_Type = ""
            contol_Reportfile = 1
            tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)


    return ()
