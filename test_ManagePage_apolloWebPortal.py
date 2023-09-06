#               Apollo Web Portal - Manage Page
import time


def managePage (driver, driver_Name, driver_Version):



    from selenium.webdriver import ActionChains
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.wait import WebDriverWait
    import tc_reports

#       Carrier details Page Address & Variables
#       Fields Address


    title_ManagePageAdr = "/html/body/app-root/app-main/div/div/breadcrumb/section/div/div/div/h1"

    menuRegion_3linesAdr_ManagePageAdr = "/html/body/app-root/app-main/div/main-header/nav"
    menu_3linesClass_ManagePageAdr = "navbar-nav"
    iframeID_ManagePageID = "hosApp"
    title_apollo_Portal_VersionAdr = "/html/body/app-root/app-main/div/main-header/nav/div[2]/div[1]/small"


#       Variables
    w = WebDriverWait(driver,10)
    control_Reportfile = 0
    print_Information_Fix = ""
    print_Information_Var = ""

#       Main
#       New iframe id="hosApp"
    w.until(EC.frame_to_be_available_and_switch_to_it((By.ID, iframeID_ManagePageID)))

    #print(".................iframe")


    # Report header:
    time.sleep(3)
    title_apollo_Portal_Version = w.until(EC.presence_of_element_located((By.XPATH, title_apollo_Portal_VersionAdr))).text
    contol_Reportfile = 0
    test_Case_Type = ""
    tc_reports.write_reportfile_Header(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version, title_apollo_Portal_Version)





    title_ManagePage = w.until(EC.presence_of_element_located((By.XPATH, title_ManagePageAdr))).text
    #print(title_ManagePage)

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



#       menu 3 Lines - Close / Open buttons menu
#       Open "page" Menu region 3 Lines
    menuRegion_3lines_ManagePage = w.until(EC.presence_of_element_located((By.XPATH, menuRegion_3linesAdr_ManagePageAdr)))
    menu_3lines_ManagePage = WebDriverWait(menuRegion_3lines_ManagePage, 10).until(EC.presence_of_element_located((By.CLASS_NAME, menu_3linesClass_ManagePageAdr)))
    menu_3lines_ManagePage.click()
    time.sleep(1)
    menu_3lines_ManagePage.click()

    return ()

    input("stop manage page")