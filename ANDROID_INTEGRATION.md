# Yandex Ads Android Entegrasyon Rehberi

Bu dosya, `index.html` içinde yapılan değişikliklerin çalışması için Android projenize eklemeniz gereken Native (Java/Kotlin) kodlarını içerir.

## 1. build.gradle (Module: app)

`dependencies` bloğuna Yandex Mobile Ads SDK'sını ekleyin:

```gradle
dependencies {
    implementation 'com.yandex.android:mobileads:7.0.0' // Veya en güncel sürüm
    // Diğer bağımlılıklar...
}
```

## 2. AndroidManifest.xml

İnternet izninin olduğundan emin olun (genelde vardır ama kontrol edin):

```xml
<uses-permission android:name="android.permission.INTERNET"/>
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>
```

## 3. MainActivity.java

Web arayüzü (`index.html`) ile Android native katmanı arasındaki köprüyü (`WebAppInterface`) kurmanız gerekmektedir.

Aşağıdaki kod yapısını `MainActivity.java` dosyanıza uyarlayın:

```java
import android.webkit.JavascriptInterface;
import android.webkit.WebView;
import com.yandex.mobile.ads.common.MobileAds;
import com.yandex.mobile.ads.interstitial.InterstitialAd;
import com.yandex.mobile.ads.interstitial.InterstitialAdEventListener;
import com.yandex.mobile.ads.rewarded.RewardedAd;
import com.yandex.mobile.ads.rewarded.RewardedAdEventListener;
import com.yandex.mobile.ads.rewarded.Reward;
// Diğer importlar...

public class MainActivity extends AppCompatActivity {
    WebView myWebView;
    private InterstitialAd mInterstitialAd;
    private RewardedAd mRewardedAd;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // SDK Başlatma
        MobileAds.initialize(this, () -> {});

        myWebView = findViewById(R.id.webview);
        myWebView.getSettings().setJavaScriptEnabled(true);

        // Arayüzü Ekle
        myWebView.addJavascriptInterface(new WebAppInterface(this), "Android");

        myWebView.loadUrl("file:///android_asset/index.html");
    }

    // --- Web Arayüzü Sınıfı ---
    public class WebAppInterface {
        Context mContext;

        WebAppInterface(Context c) {
            mContext = c;
        }

        @JavascriptInterface
        public void showRewardedAd(String adUnitId) {
            runOnUiThread(() -> {
                // Yandex Rewarded Ad Yükleme ve Gösterme Mantığı
                // Örnek: loadRewardedAd(adUnitId);
                // Reklam izlendiğinde JS tarafına ödül ver:
                // myWebView.evaluateJavascript("AdManager.onReward()", null);
            });
        }

        @JavascriptInterface
        public void showInterstitial(String adUnitId) {
            runOnUiThread(() -> {
                // Yandex Interstitial Ad Yükleme ve Gösterme Mantığı
            });
        }

        @JavascriptInterface
        public void showNativeAd(String adUnitId) {
            runOnUiThread(() -> {
                // Native reklamı yükle ve nativeAdContainer div'inin üzerine
                // veya Android layout'unda ilgili yere yerleştir.
            });
        }

        // (Opsiyonel) Eski 'showAd' çağrılarını desteklemek için
        @JavascriptInterface
        public void showAd(String adUnitId) {
            showRewardedAd(adUnitId);
        }
    }
}
```

## Önemli Notlar

1.  **ID Eşleşmesi:** `index.html` içindeki `AdManager` objesinde tanımlı ID'ler (`R-M-18543851-1` vb.) `showRewardedAd` fonksiyonuna parametre olarak gelir.
2.  **Ödül Callback:** Ödüllü reklam başarıyla izlendiğinde, Java tarafından `myWebView.evaluateJavascript("AdManager.onReward()", null);` komutu çalıştırılmalıdır. Bu, oyundaki ödül mekanizmasını tetikler.
