import static com.kms.katalon.core.checkpoint.CheckpointFactory.findCheckpoint
import static com.kms.katalon.core.testcase.TestCaseFactory.findTestCase
import static com.kms.katalon.core.testdata.TestDataFactory.findTestData
import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
import com.kms.katalon.core.checkpoint.Checkpoint as Checkpoint
import com.kms.katalon.core.checkpoint.CheckpointFactory as CheckpointFactory
import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as MobileBuiltInKeywords
import com.kms.katalon.core.model.FailureHandling as FailureHandling
import com.kms.katalon.core.testcase.TestCase as TestCase
import com.kms.katalon.core.testcase.TestCaseFactory as TestCaseFactory
import com.kms.katalon.core.testdata.TestData as TestData
import com.kms.katalon.core.testdata.TestDataFactory as TestDataFactory
import com.kms.katalon.core.testobject.ObjectRepository as ObjectRepository
import com.kms.katalon.core.testobject.TestObject as TestObject
import com.kms.katalon.core.webservice.keyword.WSBuiltInKeywords as WSBuiltInKeywords
import com.kms.katalon.core.webui.driver.DriverFactory as DriverFactory
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUiBuiltInKeywords
import internal.GlobalVariable as GlobalVariable
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI
import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as Mobile
import com.kms.katalon.core.webservice.keyword.WSBuiltInKeywords as WS
import com.kms.katalon.core.testobject.SelectorMethod

import com.thoughtworks.selenium.Selenium
import org.openqa.selenium.firefox.FirefoxDriver
import org.openqa.selenium.WebDriver
import com.thoughtworks.selenium.webdriven.WebDriverBackedSelenium
import static org.junit.Assert.*
import java.util.regex.Pattern
import static org.apache.commons.lang3.StringUtils.join
import org.testng.asserts.SoftAssert
import com.kms.katalon.core.testdata.CSVData
import org.openqa.selenium.Keys as Keys

SoftAssert softAssertion = new SoftAssert();
WebUI.openBrowser('https://www.google.com/')
def driver = DriverFactory.getWebDriver()
String baseUrl = "https://www.google.com/"
selenium = new WebDriverBackedSelenium(driver, baseUrl)
selenium.open("https://vanphongdientu.utc.edu.vn/Login")
selenium.click("link=ng nh­p b±ng e-mail UTC")
selenium.open("https://accounts.google.com/signin/oauth/error?authError=ChVyZWRpcmVjdF91cmlfbWlzbWF0Y2gSgwIKQuG6oW4ga2jDtG5nIHRo4buDIMSRxINuZyBuaOG6rXAgdsOgbyDhu6luZyBk4bulbmcgbsOgeSB2w6wg4bupbmcgZOG7pW5nIGtow7RuZyB0dcOibiB0aOG7pyBjaMOtbmggc8OhY2ggT0F1dGggMi4wIGPhu6dhIEdvb2dsZS4KCk7hur91IGLhuqFuIGzDoCBuaMOgIHBow6F0IHRyaeG7g24gY-G7p2Eg4bupbmcgZOG7pW5nIG7DoHksIGjDo3kgxJHEg25nIGvDvSBVUkkgY2h1eeG7g24gaMaw4bubbmcgdHJvbmcgR29vZ2xlIENsb3VkIENvbnNvbGUuCiAgGm1odHRwczovL2RldmVsb3BlcnMuZ29vZ2xlLmNvbS9pZGVudGl0eS9wcm90b2NvbHMvb2F1dGgyL3dlYi1zZXJ2ZXIjYXV0aG9yaXphdGlvbi1lcnJvcnMtcmVkaXJlY3QtdXJpLW1pc21hdGNoIJADKjYKDHJlZGlyZWN0X3VyaRImaHR0cDovL3ZhbnBob25nZGllbnR1LnV0Yy5lZHUudm4vTG9naW4y9wIIARKDAgpC4bqhbiBraMO0bmcgdGjhu4MgxJHEg25nIG5o4bqtcCB2w6BvIOG7qW5nIGThu6VuZyBuw6B5IHbDrCDhu6luZyBk4bulbmcga2jDtG5nIHR1w6JuIHRo4bunIGNow61uaCBzw6FjaCBPQXV0aCAyLjAgY-G7p2EgR29vZ2xlLgoKTuG6v3UgYuG6oW4gbMOgIG5ow6AgcGjDoXQgdHJp4buDbiBj4bunYSDhu6luZyBk4bulbmcgbsOgeSwgaMOjeSDEkcSDbmcga8O9IFVSSSBjaHV54buDbiBoxrDhu5tuZyB0cm9uZyBHb29nbGUgQ2xvdWQgQ29uc29sZS4KICAabWh0dHBzOi8vZGV2ZWxvcGVycy5nb29nbGUuY29tL2lkZW50aXR5L3Byb3RvY29scy9vYXV0aDIvd2ViLXNlcnZlciNhdXRob3JpemF0aW9uLWVycm9ycy1yZWRpcmVjdC11cmktbWlzbWF0Y2g&flowName=GeneralOAuthFlow&client_id=937307102473-cds1qlqhsp9fjrg953oa399trpbk4efv.apps.googleusercontent.com&as=S-1038997992%3A1791449821177629&aes=AVQXgOBms2vxeFgM4Wvt16-HK4w9")
