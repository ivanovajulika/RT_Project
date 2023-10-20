import io.appium.java_client.MobileElement;
import io.appium.java_client.android.AndroidDriver;
import io.appium.java_client.remote.MobileCapabilityType;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.testng.annotations.AfterTest;
import org.testng.annotations.BeforeTest;
import org.testng.annotations.Test;

import java.net.MalformedURLException;
import java.net.URL;
import java.util.concurrent.TimeUnit;

public class AutomationAppiumTest {
    static AndroidDriver ad;

        @BeforeTest
        public void setUp() throws MalformedURLException, InterruptedException {
            DesiredCapabilities ds = new DesiredCapabilities();

            ds.setCapability(MobileCapabilityType.DEVICE_NAME, "sdk_gphone64_x86_64");
            ds.setCapability("platformName", "android");
            ds.setCapability("app", "C:\\Users\\User\\Documents\\INMAR\\CTMobileForSalesforce\\app-release.apk");
            ds.setCapability("noReset", true);
            ad = new AndroidDriver(new URL("http://127.0.0.1:4723/wd/hub"), ds);
            ad.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);

        }

        @Test
        public void test() {
            MobileElement el1 = (MobileElement) ad.findElementByXPath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.TextView");
            System.out.println("Test passed");
        }

        @AfterTest
        public void end() {
            ad.quit();
        }

}
