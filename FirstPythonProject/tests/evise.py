# Open browser
# selenium 4
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from pynput.keyboard import Key, Controller

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

wait = WebDriverWait(driver, 30)

# Go to webpage
driver.get("https://172.30.11.78:5001/")

driver.maximize_window()

submit_button_locator = wait.until(EC.visibility_of_element_located((By.ID, "details-button")))
submit_button_locator.click()

submit_button_locator = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "172.30.11.78 sitesine ilerle (güvenli değil)")))
submit_button_locator.click()

agency_locator = wait.until(EC.visibility_of_element_located(
    (By.XPATH, "//body[@id='fullpanel']//dxbl-menu//ul/li[2]/dxbl-menu-item[@class='dxbl-menu-item']/button[@class='dxbl-btn']//span[@class='dxbl-menu-item-text']")))
agency_locator.click()

agency_portal_locator = wait.until(EC.visibility_of_element_located(
    (By.XPATH, "//body[@id='fullpanel']//dxbl-popup-cell[@class='dxbl-popup-cell']/dxbl-itemlist-dropdown"
               "[@class='dxbl-itemlist-dropdown']/dxbl-dropdown-dialog[@role='dialog']//dxbl-menu-item[@class='dxbl-menu-item']/a[@href='agency']")))
agency_portal_locator.click()

time.sleep(5)

username_locator = wait.until(EC.element_to_be_clickable((By.XPATH,"/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/dxbl-form-layout-item[1]/div[1]/dxbl-input-editor[1]/input[1]")))
username_locator.send_keys("*****")


password_locator = wait.until(EC.visibility_of_element_located((By.XPATH,"/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/dxbl-form-layout-item[2]/div[1]/dxbl-input-editor[1]/input[1]")))
password_locator.send_keys("*****")

login_button_locator = wait.until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/dxbl-form-layout-item[5]/div[1]/button[1]")))
login_button_locator.click()

time.sleep(5)

new_application_found = wait.until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/button[1]")))
new_application_found.click()

time.sleep(5)

submit_button_locator = driver.find_element(By.XPATH, " /html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/dxbl-tabs[1]/div[1]/div[1]/div[2]/div[1]/div[1]/dxbl-form-layout-item[2]/div[1]/dxbl-combobox[1]/input[1]")
submit_button_locator.click()
time.sleep(5)

submit_button_locator = driver.find_element(By.XPATH, "/html[1]/body[1]/dxbl-popup-root[1]/dxbl-popup-cell[3]/dxbl-dropdown[1]/dxbl-dropdown-dialog[1]/div[1]/dxbl-listbox[1]/ul[1]/li[1]/div[1]")
submit_button_locator.click()
time.sleep(5)

#visa_type_locator = wait.until(EC.visibility_of_element_located((By.ID, "#id6c7fe650-a955-45b4-843a-794d84a604c1")))
#visa_type_locator.send_keys("STUDENT VISA FOR UNIVERSITIES")

#visa_student_for_universities = wait.until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/dxbl-tabs[1]/div[1]/div[1]/div[2]/div[1]/div[1]/dxbl-form-layout-item[2]/div[1]/dxbl-combobox[1]/div[1]/button[1]")))
#visa_student_for_universities.click()

email_locator = wait.until(EC.visibility_of_element_located(
    (By.XPATH,"/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/dxbl-tabs[1]/div[1]/div[1]/div[2]/div[2]/div[1]/"
              "dxbl-form-layout-item[1]/div[1]/dxbl-input-editor[1]/input[1]")))
email_locator.send_keys("cagla.silakbeg@gmail.com")

time.sleep(5)

first_name_locator = wait.until(EC.visibility_of_element_located(
    (By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/dxbl-tabs[1]/div[1]/div[1]/div[3]/div[1]/div[1]/dxbl-"
               "form-layout-item[1]/div[1]/dxbl-input-editor[1]/input[1]")))
first_name_locator.send_keys("isim")

time.sleep(5)


date_of_birth_locator = wait.until(EC.visibility_of_element_located(
    (By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/dxbl-tabs[1]/div[1]/div[1]/div[3]/div[1]/div[1]/"
               "dxbl-form-layout-item[3]/div[1]/dxbl-date-edit[1]/input[1]")))
date_of_birth_locator.send_keys("08.11.2000")

time.sleep(5)

place_of_birth_locator = wait.until(EC.visibility_of_element_located(
    (By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/dxbl-tabs[1]/div[1]/div[1]/div[3]/div[1]/div[1]/dxbl-"
               "form-layout-item[4]/div[1]/dxbl-input-editor[1]/input[1]")))
place_of_birth_locator.send_keys("******")

time.sleep(5)

#identity_locator = wait.until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/dxbl-tabs[1]/div[1]/div[1]/div[3]/div[1]/div[1]/dxbl-form-layout-item[5]/div[1]/dxbl-input-editor[1]/input[1]")))
#identity_locator.send_keys("*****")

#time.sleep(5)

sex_locator = wait.until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/dxbl-tabs[1]/div[1]/div[1]/div[3]/div[1]/div[1]/dxbl-form-layout-item[6]/div[1]/dxbl-combobox[1]/input[1]")))
sex_locator.click()

time.sleep(5)

male_locator = wait.until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/dxbl-popup-root[1]/dxbl-popup-cell[5]/dxbl-dropdown[1]/dxbl-dropdown-dialog[1]/div[1]/dxbl-listbox[1]/ul[1]/li[2]/div[1]")))
male_locator.click()

time.sleep(5)

martial_status_locator = wait.until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/dxbl-tabs[1]/div[1]/div[1]/div[3]/div[1]/div[1]/dxbl-form-layout-item[7]/div[1]/dxbl-combobox[1]/input[1]")))
martial_status_locator.click()

time.sleep(5)

single_locator = wait.until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/dxbl-popup-root[1]/dxbl-popup-cell[6]/dxbl-dropdown[1]/dxbl-dropdown-dialog[1]/div[1]/dxbl-listbox[1]/ul[1]/li[1]/div[1]")))
single_locator.click()

time.sleep(5)

nationaly_locator = wait.until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/dxbl-tabs[1]/div[1]/div[1]/div[3]/div[1]/div[1]/dxbl-form-layout-item[9]/div[1]/dxbl-combobox[1]/input[1]")))
nationaly_locator.send_keys("INDIA")

time.sleep(5)

india_locator = wait.until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/dxbl-popup-root[1]/dxbl-popup-cell[7]/dxbl-dropdown[1]/dxbl-dropdown-dialog[1]/div[1]/dxbl-listbox[1]/ul[1]/li[2]/div[1]")))
india_locator.click()

time.sleep(5)

document_number_locator = wait.until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/dxbl-tabs[1]/div[1]/div[1]/div[4]/div[1]/div[1]/dxbl-form-layout-item[2]/div[1]/dxbl-input-editor[1]/input[1]")))
document_number_locator.send_keys("U5421920")

time.sleep(5)

date_of_issue_locator = wait.until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/dxbl-tabs[1]/div[1]/div[1]/div[4]/div[1]/div[1]/dxbl-form-layout-item[3]/div[1]/dxbl-date-edit[1]/input[1]")))
date_of_issue_locator.send_keys("31.08.2020")

time.sleep(5)

valid_until_date_locator = wait.until(EC.visibility_of_element_located((By.XPATH,"/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/dxbl-tabs[1]/div[1]/div[1]/div[4]/div[1]/div[1]/dxbl-form-layout-item[4]/div[1]/dxbl-date-edit[1]/input[1]")))
valid_until_date_locator.send_keys("30.08.2030")

time.sleep(5)

place_of_issue = wait.until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/dxbl-tabs[1]/div[1]/div[1]/div[4]/div[1]/div[1]/dxbl-form-layout-item[5]/div[1]/dxbl-input-editor[1]/input[1]")))
place_of_issue.send_keys("CHANDIGARH")

time.sleep(5)

issue_country_locator = wait.until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/dxbl-tabs[1]/div[1]/div[1]/div[4]/div[1]/div[1]/dxbl-form-layout-item[6]/div[1]/dxbl-combobox[1]/input[1]")))
issue_country_locator.send_keys("INDIA")

time.sleep(5)

india_locator = wait.until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/dxbl-popup-root[1]/dxbl-popup-cell[11]/dxbl-dropdown[1]/dxbl-dropdown-dialog[1]/div[1]/dxbl-listbox[1]/ul[1]/li[2]/div[1]")))
india_locator.click()

time.sleep(5)

upload_photo_locator = wait.until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/dxbl-tabs[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]")))
upload_photo_locator.click()

time.sleep(5)

keyboard = Controller()

keyboard.type("pasaport2.pdf")

time.sleep(5)

keyboard.press(Key.enter)
keyboard.release(Key.enter)

time.sleep(10)

purpose_of_stay_locator = wait.until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/dxbl-tabs[1]/div[1]/div[1]/div[5]/div[1]/div[1]/dxbl-form-layout-item[1]/div[1]/dxbl-input-editor[1]/input[1]")))
purpose_of_stay_locator.send_keys("Education")

time.sleep(5)

#[Caption.From]
username_locator = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/dxbl-tabs[1]/div[1]/div[1]/div[5]/div[1]/div[1]/dxbl-form-layout-item[2]/div[1]/dxbl-date-edit[1]/input[1]")
username_locator.send_keys("28.09.2023")
time.sleep(5)

#[Caption.To]
username_locator = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/dxbl-tabs[1]/div[1]/div[1]/div[5]/div[1]/div[1]/dxbl-form-layout-item[3]/div[1]/dxbl-date-edit[1]/input[1]")
username_locator.send_keys("27.11.2023")
time.sleep(5)

#email_locator = wait.until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/dxbl-tabs[1]/div[1]/div[1]/div[6]/div[1]/div[1]/dxbl-form-layout-item[1]/div[1]/dxbl-input-editor[1]/input[1]")))
#email_locator.send_keys("emirince2015@gmail.com")

#time.sleep(5)


phone_number_locator = wait.until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/dxbl-tabs[1]/div[1]/div[1]/div[6]/div[1]/div[1]/dxbl-form-layout-item[2]/div[1]/dxbl-masked-input[1]/input[1]")))
phone_number_locator.send_keys("9")

time.sleep(2)

phone_number_locator = wait.until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/dxbl-tabs[1]/div[1]/div[1]/div[6]/div[1]/div[1]/dxbl-form-layout-item[2]/div[1]/dxbl-masked-input[1]/input[1]")))
phone_number_locator.send_keys("0")

time.sleep(2)

phone_number_locator = wait.until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/dxbl-tabs[1]/div[1]/div[1]/div[6]/div[1]/div[1]/dxbl-form-layout-item[2]/div[1]/dxbl-masked-input[1]/input[1]")))
phone_number_locator.send_keys("553")

time.sleep(2)

phone_number_locator = wait.until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/dxbl-tabs[1]/div[1]/div[1]/div[6]/div[1]/div[1]/dxbl-form-layout-item[2]/div[1]/dxbl-masked-input[1]/input[1]")))
phone_number_locator.send_keys("419")

time.sleep(2)

phone_number_locator = wait.until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/dxbl-tabs[1]/div[1]/div[1]/div[6]/div[1]/div[1]/dxbl-form-layout-item[2]/div[1]/dxbl-masked-input[1]/input[1]")))
phone_number_locator.send_keys("73")

time.sleep(2)

phone_number_locator = wait.until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/dxbl-tabs[1]/div[1]/div[1]/div[6]/div[1]/div[1]/dxbl-form-layout-item[2]/div[1]/dxbl-masked-input[1]/input[1]")))
phone_number_locator.send_keys("53")

time.sleep(5)

adress_locator = wait.until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/dxbl-tabs[1]/div[1]/div[1]/div[6]/div[1]/div[1]/div[1]/dxbl-group-control[1]/dxbl-expandable-container[1]/div[1]/div[1]/dxbl-form-layout-item[1]/div[1]/dxbl-input-editor[1]/input[1]")))
adress_locator.send_keys("address")

time.sleep(5)

city_locator = wait.until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/dxbl-tabs[1]/div[1]/div[1]/div[6]/div[1]/div[1]/div[1]/dxbl-group-control[1]/dxbl-expandable-container[1]/div[1]/div[1]/dxbl-form-layout-item[2]/div[1]/dxbl-input-editor[1]/input[1]")))
city_locator.send_keys("Ist")

time.sleep(5)

town_locator = wait.until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/dxbl-tabs[1]/div[1]/div[1]/div[6]/div[1]/div[1]/div[1]/dxbl-group-control[1]/dxbl-expandable-container[1]/div[1]/div[1]/dxbl-form-layout-item[3]/div[1]/dxbl-input-editor[1]/input[1]")))
town_locator.send_keys("Kucukcekmece")

time.sleep(5)

postal_code_locator = wait.until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/dxbl-tabs[1]/div[1]/div[1]/div[6]/div[1]/div[1]/div[1]/dxbl-group-control[1]/dxbl-expandable-container[1]/div[1]/div[1]/dxbl-form-layout-item[4]/div[1]/dxbl-spinedit[1]/input[1]")))
postal_code_locator.send_keys("34290")

time.sleep(5)

country_locator = wait.until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/dxbl-tabs[1]/div[1]/div[1]/div[6]/div[1]/div[1]/div[1]/dxbl-group-control[1]/dxbl-expandable-container[1]/div[1]/div[1]/dxbl-form-layout-item[5]/div[1]/dxbl-combobox[1]/input[1]")))
country_locator.send_keys("INDIA")

time.sleep(5)

india_locator = wait.until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/dxbl-popup-root[1]/dxbl-popup-cell[14]/dxbl-dropdown[1]/dxbl-dropdown-dialog[1]/div[1]/dxbl-listbox[1]/ul[1]/li[2]/div[1]")))
india_locator.click()

time.sleep(5)

next_button_locator = wait.until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/button[1]")))
next_button_locator.click()

time.sleep(5)

#OK BUTONU
ok_button_locator = wait.until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/dxbl-popup-root[1]/dxbl-popup-cell[15]/dxbl-modal[1]/dxbl-modal-root[1]/dxbl-modal-dialog[1]/div[1]/div[2]/button[1]")))
ok_button_locator.click()

#İkinci Sayfa

#[Caption.Fathers.First.Name]
adress_locator = wait.until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/dxbl-tabs[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/dxbl-group-control[1]/dxbl-expandable-container[1]/div[1]/div[1]/dxbl-form-layout-item[1]/div[1]/dxbl-input-editor[1]/input[1]")))
adress_locator.send_keys("KHAN")
time.sleep(5)


#[Caption.Fathers.Family.Name]
adress_locator = wait.until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/dxbl-tabs[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/dxbl-group-control[1]/dxbl-expandable-container[1]/div[1]/div[1]/dxbl-form-layout-item[2]/div[1]/dxbl-input-editor[1]/input[1]")))
adress_locator.send_keys("YOK")
time.sleep(5)

#[Caption.Fathers.Date.Of.Birth]
adress_locator = wait.until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/dxbl-tabs[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/dxbl-group-control[1]/dxbl-expandable-container[1]/div[1]/div[1]/dxbl-form-layout-item[3]/div[1]/dxbl-date-edit[1]/input[1]")))
adress_locator.send_keys("23.03.1969")
time.sleep(5)

#[Caption.Fathers.Place.Of.Birth]
adress_locator = wait.until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/dxbl-tabs[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/dxbl-group-control[1]/dxbl-expandable-container[1]/div[1]/div[1]/dxbl-form-layout-item[4]/div[1]/dxbl-input-editor[1]/input[1]")))
adress_locator.send_keys("CHANDIGARH")
time.sleep(5)

#[Caption.Fathers.Current.Nationality]
adress_locator = wait.until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/dxbl-tabs[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/dxbl-group-control[1]/dxbl-expandable-container[1]/div[1]/div[1]/dxbl-form-layout-item[5]/div[1]/dxbl-input-editor[1]/input[1]")))
adress_locator.send_keys("INDIA")
time.sleep(5)

#[Caption.Fathers.Place.Of.Residence]
adress_locator = wait.until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/dxbl-tabs[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/dxbl-group-control[1]/dxbl-expandable-container[1]/div[1]/div[1]/dxbl-form-layout-item[6]/div[1]/dxbl-input-editor[1]/input[1]")))
adress_locator.send_keys("CHANDIGARH")
time.sleep(5)

#[Caption.Mothers.First.Name]
adress_locator = wait.until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/dxbl-tabs[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/dxbl-group-control[1]/dxbl-expandable-container[1]/div[1]/div[1]/dxbl-form-layout-item[1]/div[1]/dxbl-input-editor[1]/input[1]")))
adress_locator.send_keys("CHANS")
time.sleep(5)

#[Caption.Mothers.Family.Name]
adress_locator = wait.until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/dxbl-tabs[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/dxbl-group-control[1]/dxbl-expandable-container[1]/div[1]/div[1]/dxbl-form-layout-item[2]/div[1]/dxbl-input-editor[1]/input[1]")))
adress_locator.send_keys("YOK")
time.sleep(5)

#[Caption.Mothers.Date.Of.Birth]
adress_locator = wait.until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/dxbl-tabs[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/dxbl-group-control[1]/dxbl-expandable-container[1]/div[1]/div[1]/dxbl-form-layout-item[3]/div[1]/dxbl-date-edit[1]/input[1]")))
adress_locator.send_keys("27.07.1971")
time.sleep(5)

#[Caption.Mothers.Place.Of.Birth]
adress_locator = wait.until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/dxbl-tabs[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/dxbl-group-control[1]/dxbl-expandable-container[1]/div[1]/div[1]/dxbl-form-layout-item[4]/div[1]/dxbl-input-editor[1]/input[1]")))
adress_locator.send_keys("CHANDIGARH")
time.sleep(5)

#[Caption.Mothers.Current.Nationality]
adress_locator = wait.until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/dxbl-tabs[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/dxbl-group-control[1]/dxbl-expandable-container[1]/div[1]/div[1]/dxbl-form-layout-item[5]/div[1]/dxbl-input-editor[1]/input[1]")))
adress_locator.send_keys("INDIA")
time.sleep(5)

#[Caption.Mothers.Place.Of.Residence]
adress_locator = wait.until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/dxbl-tabs[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/dxbl-group-control[1]/dxbl-expandable-container[1]/div[1]/div[1]/dxbl-form-layout-item[6]/div[1]/dxbl-input-editor[1]/input[1]")))
adress_locator.send_keys("CHANDIGARH")
time.sleep(5)

#[Caption.Occupation.Learned]
next_button_locator = wait.until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/dxbl-tabs[1]/div[1]/div[2]/div[2]/div[1]/div[1]/dxbl-form-layout-item[1]/div[1]/dxbl-combobox[1]/input[1]")))
next_button_locator.click()
time.sleep(5)

#STUDENT BUTONUNA TIKLA
next_button_locator = wait.until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/dxbl-popup-root[1]/dxbl-popup-cell[18]/dxbl-dropdown[1]/dxbl-dropdown-dialog[1]/div[1]/dxbl-listbox[1]/ul[1]/li[1]/div[1]")))
next_button_locator.click()
time.sleep(5)


#NEXT BUTONU
next_button_locator = wait.until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/button[1]")))
next_button_locator.click()
time.sleep(5)


#ÜÇÜNCÜ SAYFA

#REFERANCE OLMADIĞINI DÜŞÜNELİM
#NEXT BUTONU
next_button_locator = wait.until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/button[1]")))
next_button_locator.click()
time.sleep(5)

#DÖRDÜNCÜ SAYFA

#[Declarations]
#[What.are.your.means.of.support.in.the.TRNC]
adress_locator = wait.until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/dxbl-tabs[1]/div[1]/div[4]/div[1]/div[1]/div[1]/dxbl-form-layout-item[1]/div[1]/dxbl-memo-editor[1]/textarea[1]")))
adress_locator.send_keys("EXAMPLE")
time.sleep(5)

#[Intended.place.of.stay.in.the.TRNC]
adress_locator = wait.until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/dxbl-tabs[1]/div[1]/div[4]/div[1]/div[1]/div[1]/dxbl-form-layout-item[3]/div[1]/dxbl-input-editor[1]/input[1]")))
adress_locator.send_keys("ROSJDKL")
time.sleep(5)

#[Address]
#[Caption.Address]
adress_locator = wait.until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/dxbl-tabs[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/dxbl-group-control[1]/dxbl-expandable-container[1]/div[1]/div[1]/dxbl-form-layout-item[1]/div[1]/dxbl-input-editor[1]/input[1]")))
adress_locator.send_keys("IJASKZIAWSMKLOEJASDLMKZ")
time.sleep(5)

#[Caption.Town]
adress_locator = wait.until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/dxbl-tabs[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/dxbl-group-control[1]/dxbl-expandable-container[1]/div[1]/div[1]/dxbl-form-layout-item[2]/div[1]/dxbl-input-editor[1]/input[1]")))
adress_locator.send_keys("INDIA")
time.sleep(5)

#[Caption.Postal.Code]
adress_locator = wait.until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/dxbl-tabs[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/dxbl-group-control[1]/dxbl-expandable-container[1]/div[1]/div[1]/dxbl-form-layout-item[3]/div[1]/dxbl-spinedit[1]/input[1]")))
adress_locator.send_keys("533 699 5614")
time.sleep(5)

#[Caption.City]
next_button_locator = wait.until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/dxbl-tabs[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/dxbl-group-control[1]/dxbl-expandable-container[1]/div[1]/div[1]/dxbl-form-layout-item[3]/div[1]/dxbl-spinedit[1]/input[1]")))
next_button_locator.click()
time.sleep(5)

#GİRNE BUTONUNA TIKLA
next_button_locator = wait.until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/dxbl-popup-root[1]/dxbl-popup-cell[47]/dxbl-dropdown[1]/dxbl-dropdown-dialog[1]/div[1]/dxbl-listbox[1]/ul[1]/li[3]/div[1]")))
next_button_locator.click()
time.sleep(5)

#[How.will.you.be.accommodated]
next_button_locator = wait.until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/dxbl-tabs[1]/div[1]/div[4]/div[1]/div[1]/div[1]/dxbl-form-layout-item[4]/div[1]/dxbl-combobox[1]/input[1]")))
next_button_locator.click()
time.sleep(5)

#HOTEL BUTONUNA TIKLA
next_button_locator = wait.until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/dxbl-popup-root[1]/dxbl-popup-cell[46]/dxbl-dropdown[1]/dxbl-dropdown-dialog[1]/div[1]/dxbl-listbox[1]/ul[1]/li[1]/div[1]")))
next_button_locator.click()
time.sleep(5)

#[Do.family.members.intend.to.accompany.you.which.explain]
adress_locator = wait.until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/dxbl-tabs[1]/div[1]/div[4]/div[1]/div[1]/div[1]/dxbl-form-layout-item[5]/div[1]/dxbl-memo-editor[1]/textarea[1]")))
adress_locator.send_keys("KAJNCSIONAK")
time.sleep(5)

#[Do.you.have.health.insurance.for.a.longer.stay.for.the.TRNC]
next_button_locator = wait.until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/dxbl-tabs[1]/div[1]/div[4]/div[1]/div[1]/div[1]/dxbl-form-layout-item[6]/div[1]/dxbl-check[1]/div[1]/input[1]")))
next_button_locator.click()
time.sleep(5)

#NEXT BUTONUNA TIKLA
next_button_locator = wait.until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/button[1]")))
next_button_locator.click()
time.sleep(5)

#BEŞİNCİ SAYFA

#UPLOAD BUTONUNA TIKLA
next_button_locator = wait.until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/dxbl-tabs[1]/div[1]/div[5]/dxbl-stack-layout[1]/dxbl-stack-layout-root[1]/dxbl-stack-layout-item[1]/dxbl-stack-layout[1]/dxbl-stack-layout-root[1]/dxbl-stack-layout-item[1]/div[1]/div[1]/button[1]")))
next_button_locator.click()
time.sleep(5)


#BİYOMETRİK YÜKLE
keyboard = Controller()

keyboard.type("bioP-1.png")

time.sleep(5)

keyboard.press(Key.enter)
keyboard.release(Key.enter)

time.sleep(10)

#NEXT BUTONUNA TIKLA
next_button_locator = wait.until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/button[1]")))
next_button_locator.click()
time.sleep(5)
